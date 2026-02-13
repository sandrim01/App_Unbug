from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app
from flask_login import login_required, current_user
from extensions import db, socketio
from models import Ticket, Client, Employee, ServiceOrder, ActivityLog
from datetime import datetime

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')

@tickets_bp.route('/')
@login_required
def index():
    status_filter = request.args.get('status', '')
    query = Ticket.query
    
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    tickets = query.order_by(Ticket.created_at.desc()).all()
    return render_template('tickets/index.html', tickets=tickets, current_status=status_filter)

@tickets_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_ticket():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        client_id = request.form.get('client_id')
        priority = request.form.get('priority', 'medium')
        
        if not title or not description or not client_id:
            flash('Por favor, preencha todos os campos obrigatórios.', 'danger')
            return redirect(url_for('tickets.new_ticket'))
            
        ticket = Ticket(
            title=title,
            description=description,
            client_id=client_id,
            priority=priority,
            status='open'
        )
        
        db.session.add(ticket)
        db.session.commit()
        
        # Emit real-time notification
        try:
            socketio.emit('new_ticket', {
                'id': ticket.id,
                'title': ticket.title,
                'client': ticket.client.name,
                'priority': ticket.priority
            })
        except Exception as e:
            current_app.logger.error(f"Error emitting socket event: {str(e)}")
        
        ActivityLog.log_activity(
            username=current_user.username,
            activity=f'Criou novo chamado: {title}',
            ip_address=request.remote_addr,
            user_id=current_user.id,
            category='chamados'
        )
        
        flash('Chamado aberto com sucesso!', 'success')
        return redirect(url_for('tickets.index'))
        
    clients = Client.query.filter_by(active=True).all()
    return render_template('tickets/ticket_form.html', clients=clients, title="Novo Chamado")

@tickets_bp.route('/view/<int:id>')
@login_required
def view_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    employees = Employee.query.filter_by(active=True).all()
    return render_template('tickets/view.html', ticket=ticket, employees=employees)

@tickets_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    
    if request.method == 'POST':
        ticket.title = request.form.get('title')
        ticket.description = request.form.get('description')
        ticket.priority = request.form.get('priority')
        ticket.status = request.form.get('status')
        ticket.assigned_to_id = request.form.get('assigned_to_id') or None
        
        db.session.commit()
        flash('Chamado atualizado com sucesso!', 'success')
        return redirect(url_for('tickets.view_ticket', id=ticket.id))
        
    clients = Client.query.filter_by(active=True).all()
    employees = Employee.query.filter_by(active=True).all()
    return render_template('tickets/ticket_form.html', ticket=ticket, clients=clients, employees=employees, title="Editar Chamado")

@tickets_bp.route('/convert/<int:id>', methods=['POST'])
@login_required
def convert_to_os(id):
    ticket = Ticket.query.get_or_404(id)
    
    if ticket.service_order_id:
        flash('Este chamado já possui uma Ordem de Serviço vinculada.', 'warning')
        return redirect(url_for('tickets.view_ticket', id=ticket.id))
        
    # Create Service Order from Ticket
    os = ServiceOrder(
        title=f"OS: {ticket.title}",
        description=ticket.description,
        client_id=ticket.client_id,
        status='open',
        priority=ticket.priority,
        employee_id=ticket.assigned_to_id or current_user.employee.id if current_user.employee else None
    )
    
    db.session.add(os)
    db.session.flush() # Get OS ID
    
    ticket.service_order_id = os.id
    ticket.status = 'in_progress'
    
    db.session.commit()
    
    ActivityLog.log_activity(
        username=current_user.username,
        activity=f'Converteu chamado #{ticket.id} em OS #{os.id}',
        ip_address=request.remote_addr,
        user_id=current_user.id,
        category='chamados'
    )
    
    flash(f'Chamado convertido em OS #{os.id} com sucesso!', 'success')
    return redirect(url_for('orders.edit_order', id=os.id))

@tickets_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_ticket(id):
    if not current_user.can_delete():
        flash('Você não tem permissão para excluir chamados.', 'danger')
        return redirect(url_for('tickets.index'))
        
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    
    flash('Chamado excluído com sucesso!', 'success')
    return redirect(url_for('tickets.index'))
