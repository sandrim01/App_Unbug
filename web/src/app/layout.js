import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
    title: "Unbug ERP | Dashboard",
    description: "Sistema Moderno de Gestão - Unbug Solutions TI",
};

export default function RootLayout({ children }) {
    return (
        <html lang="pt-BR">
            <body className={`${inter.className} min-h-screen bg-[#020617]`}>
                <div className="flex h-screen overflow-hidden">
                    {/* Main Content Area */}
                    <main className="flex-1 overflow-y-auto overflow-x-hidden pt-4 px-6">
                        {children}
                    </main>
                </div>
            </body>
        </html>
    );
}
