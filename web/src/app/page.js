'use client'

import { motion } from 'framer-motion';
import {
    BarChart3,
    Users,
    Settings,
    Package,
    FileText,
    Wallet,
    Ticket,
    ChevronRight,
    Plus
} from 'lucide-react';

const StatCard = ({ title, value, icon: Icon, color }) => (
    <motion.div
        whileHover={{ scale: 1.02 }}
        className="glass-card rounded-2xl p-5 flex items-center justify-between"
    >
        <div>
            <p className="text-slate-400 text-sm font-medium">{title}</p>
            <h3 className="text-white text-2xl font-bold mt-1">{value}</h3>
        </div>
        <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${color}`}>
            <Icon className="text-white w-6 h-6" />
        </div>
    </motion.div>
);

const QuickAction = ({ label, icon: Icon }) => (
    <button className="flex flex-col items-center justify-center gap-2 p-4 rounded-2xl glass hover:bg-white/10 transition-all duration-300">
        <div className="w-10 h-10 rounded-full bg-primary/20 flex items-center justify-center text-primary">
            <Icon size={20} />
        </div>
        <span className="text-sm font-medium text-slate-200">{label}</span>
    </button>
);

export default function Dashboard() {
    return (
        <div className="max-w-7xl mx-auto pb-10">
            {/* Header */}
            <div className="flex justify-between items-center mb-10">
                <div>
                    <h1 className="text-3xl font-bold text-white tracking-tight">Painel de Controle</h1>
                    <p className="text-slate-400 mt-1">Bem-vindo de volta, Administrador.</p>
                </div>
                <button className="premium-gradient px-6 py-2.5 rounded-xl font-semibold flex items-center gap-2 text-white shadow-lg shadow-primary/20 hover:shadow-primary/40 transition-all">
                    <Plus size={18} />
                    Nova OS
                </button>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                <StatCard
                    title="OS Pendentes"
                    value="12"
                    icon={FileText}
                    color="bg-amber-500/20 text-amber-500"
                />
                <StatCard
                    title="Faturamento (Mês)"
                    value="R$ 15.420"
                    icon={Wallet}
                    color="bg-emerald-500/20 text-emerald-500"
                />
                <StatCard
                    title="Clientes Ativos"
                    value="158"
                    icon={Users}
                    color="bg-indigo-500/20 text-indigo-500"
                />
                <StatCard
                    title="Tickets Abertos"
                    value="5"
                    icon={Ticket}
                    color="bg-rose-500/20 text-rose-500"
                />
            </div>

            {/* Main Sections */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Recent Activity */}
                <div className="lg:col-span-2 space-y-6">
                    <div className="glass-card rounded-3xl p-6">
                        <h2 className="text-xl font-bold text-white mb-6">Ordens de Serviço Recentes</h2>
                        <div className="space-y-4">
                            {[1, 2, 3].map((i) => (
                                <div key={i} className="flex items-center justify-between p-4 rounded-xl hover:bg-white/5 transition-colors border border-white/5">
                                    <div className="flex items-center gap-4">
                                        <div className="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center">
                                            <Settings size={20} className="text-slate-400" />
                                        </div>
                                        <div>
                                            <p className="text-white font-medium">Manutenção Servidor Dell - OS #420{i}</p>
                                            <p className="text-xs text-slate-500">Cliente: TechCorp Solutions</p>
                                        </div>
                                    </div>
                                    <div className="flex items-center gap-6">
                                        <span className="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-500">
                                            Concluído
                                        </span>
                                        <ChevronRight className="text-slate-600" size={18} />
                                    </div>
                                </div>
                            ))}
                        </div>
                        <button className="w-full mt-6 text-indigo-400 text-sm font-semibold hover:text-indigo-300 transition-colors">
                            Ver Todas as Ordens
                        </button>
                    </div>
                </div>

                {/* Sidebar Sections */}
                <div className="space-y-6">
                    {/* Quick Actions */}
                    <div className="glass-card rounded-3xl p-6">
                        <h2 className="text-lg font-bold text-white mb-6">Ações Rápidas</h2>
                        <div className="grid grid-cols-2 gap-4">
                            <QuickAction label="Estoque" icon={Package} />
                            <QuickAction label="Relatórios" icon={BarChart3} />
                            <QuickAction label="Usuários" icon={Users} />
                            <QuickAction label="Config" icon={Settings} />
                        </div>
                    </div>

                    {/* Low Stock Alert */}
                    <div className="glass-card rounded-3xl p-6 border-l-4 border-l-rose-500">
                        <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                            <Package size={20} className="text-rose-500" />
                            Alerta de Estoque
                        </h2>
                        <div className="space-y-3">
                            <div className="flex justify-between text-sm">
                                <span className="text-slate-300">SSD 240GB Kingston</span>
                                <span className="text-rose-500 font-bold">2 unid</span>
                            </div>
                            <div className="flex justify-between text-sm">
                                <span className="text-slate-300">Cabo de Rede CAT6</span>
                                <span className="text-amber-500 font-bold">15m</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
