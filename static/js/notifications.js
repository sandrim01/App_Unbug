// Socket.io real-time notifications for Unbug ERP
document.addEventListener('DOMContentLoaded', function() {
    // Check if io is defined (from socket.io script)
    if (typeof io !== 'undefined') {
        const socket = io();

        // Listen for new ticket events
        socket.on('new_ticket', function(data) {
            console.log('Novo chamado recebido:', data);
            
            // Show a visual toast in the browser if supported
            if (window.Notification && Notification.permission === "granted") {
                new Notification("Novo Chamado: " + data.title, {
                    body: "Cliente: " + data.client + "\nPrioridade: " + data.priority,
                    icon: "/static/img/unbug_symbol.png"
                });
            } else if (window.Notification && Notification.permission !== "denied") {
                Notification.requestPermission();
            }

            // Optional: Play a subtle sound
            // const audio = new Audio('/static/sounds/notification.mp3');
            // audio.play().catch(e => console.log('Audio play failed'));

            // Refresh dashboards if on dashboard page
            if (window.location.pathname.includes('/dashboard')) {
                // Update open tickets count element by ID if it exists
                const ticketCountEl = document.querySelector('.dashboard-card[style*="#6f42c1"] .card-value');
                if (ticketCountEl) {
                    ticketCountEl.textContent = parseInt(ticketCountEl.textContent) + 1;
                }
            }
        });
    }
});
