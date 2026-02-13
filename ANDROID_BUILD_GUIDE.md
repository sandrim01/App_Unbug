# Guia de Compilação Android - Unbug ERP

Para transformar este ERP em um aplicativo Android profissional, recomendamos o uso do **Capacitor**, que permite envolver a interface web em uma WebView nativa de alta performance.

### 1. Pré-requisitos
- **Node.js** instalado.
- **Android Studio** instalado.

### 2. Configuração Inicial
Na raiz do projeto, execute:
```bash
npm init @capacitor/app android-app
```
*Siga as instruções para nomear o app (ex: Unbug ERP).*

### 3. Sincronização
Como este é um app baseado em Python/Flask, o Android funcionará como um **Thin Client** apontando para o seu servidor (Railway/Local).

No arquivo `capacitor.config.json`, configure a URL do seu servidor:
```json
{
  "appId": "com.unbug.erp",
  "appName": "Unbug ERP",
  "webDir": "static",
  "server": {
    "url": "https://seu-app.up.railway.app",
    "cleartext": true
  }
}
```

### 4. Adicionar Plataforma Android
```bash
npm install @capacitor/android
npx cap add android
```

### 5. Abrir no Android Studio e Gerar APK
```bash
npx cap open android
```
No Android Studio:
1. Vá em **Build > Build Bundle(s) / APK(s) > Build APK(s)**.
2. O APK será gerado e estará pronto para instalação em qualquer celular.

---
### Destaques do App Mobile
- **Navegação Inferior:** O sistema detecta automaticamente o acesso mobile e exibe uma barra de navegação estilo "App Store".
- **Modo Escuro:** Segue a preferência do sistema operacional.
- **Chamados:** Interface otimizada para abertura rápida de tickets pelo celular.
