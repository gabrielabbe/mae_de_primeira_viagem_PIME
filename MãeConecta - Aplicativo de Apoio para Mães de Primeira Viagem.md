# MãeConecta - Aplicativo de Apoio para Mães de Primeira Viagem

## 📱 Sobre o Projeto

O **MãeConecta** é um aplicativo móvel desenvolvido em Flutter que oferece suporte personalizado para mães de primeira viagem. O aplicativo fornece dicas validadas por pediatras, calculadora de amamentação baseada na idade do bebê, sistema de registro de mamadas e notificações inteligentes.

### 🎯 Objetivos

- Reduzir a ansiedade materna através de informações confiáveis
- Fornecer orientações personalizadas baseadas na idade do bebê
- Facilitar o acompanhamento da alimentação e desenvolvimento infantil
- Criar uma ponte entre conhecimento pediátrico e cuidados cotidianos

### 👥 Público-Alvo

Mães de primeira viagem no Brasil que possuem smartphone e buscam uma fonte segura de orientação para os cuidados com seus bebês no primeiro ano de vida.

## ✨ Funcionalidades Principais

### 🍼 Calculadora de Amamentação
- Recomendações personalizadas baseadas na idade do bebê
- Volume por mamada e frequência diária
- Intervalos entre mamadas
- Diretrizes da Sociedade Brasileira de Pediatria

### 💡 Sistema de Dicas Personalizadas
- Dicas organizadas por categorias (alimentação, sono, higiene, desenvolvimento, saúde, segurança)
- Conteúdo validado por pediatras
- Dica do dia personalizada
- Busca por palavras-chave

### 📊 Registro de Mamadas
- Acompanhamento de alimentação do bebê
- Estatísticas e relatórios
- Histórico completo
- Gráficos de progresso

### 🔔 Sistema de Notificações
- Lembretes de mamadas
- Dicas diárias
- Marcos de desenvolvimento
- Configurações personalizáveis

### 👶 Perfil do Bebê
- Cadastro completo das informações
- Cálculo automático de idade e categoria
- Recomendações baseadas na faixa etária
- Acompanhamento do crescimento

## 🛠️ Tecnologias Utilizadas

- **Flutter 3.10+**: Framework principal
- **Dart 3.0+**: Linguagem de programação
- **Provider**: Gerenciamento de estado
- **GoRouter**: Navegação declarativa
- **SharedPreferences**: Armazenamento local
- **SQLite**: Banco de dados local
- **Flutter Local Notifications**: Sistema de notificações
- **Intl**: Internacionalização

## 📁 Estrutura do Projeto

```
maeconecta_flutter/
├── lib/
│   ├── main.dart                    # Arquivo principal
│   ├── models/                      # Modelos de dados
│   │   ├── user.dart
│   │   ├── baby.dart
│   │   ├── feeding_record.dart
│   │   └── tip.dart
│   ├── screens/                     # Telas do aplicativo
│   │   ├── splash_screen.dart
│   │   ├── login_screen.dart
│   │   ├── register_screen.dart
│   │   ├── home_screen.dart
│   │   ├── baby_profile_screen.dart
│   │   ├── feeding_calculator_screen.dart
│   │   ├── tips_screen.dart
│   │   ├── feeding_log_screen.dart
│   │   └── profile_screen.dart
│   ├── services/                    # Serviços e lógica de negócio
│   │   ├── auth_service.dart
│   │   ├── baby_service.dart
│   │   ├── feeding_service.dart
│   │   ├── tips_service.dart
│   │   └── notification_service.dart
│   ├── widgets/                     # Componentes reutilizáveis
│   └── utils/                       # Utilitários e helpers
├── assets/                          # Recursos do aplicativo
│   ├── images/
│   └── fonts/
├── pubspec.yaml                     # Dependências do projeto
├── DOCUMENTACAO_TECNICA.md          # Documentação técnica completa
├── MANUAL_DO_USUARIO.md             # Manual para usuários finais
├── GUIA_DEPLOYMENT_FLUTTERFLOW.md   # Guia para FlutterFlow
└── README.md                        # Este arquivo
```

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Flutter SDK 3.10 ou superior
- Dart 3.0 ou superior
- Android Studio / VS Code
- Dispositivo físico ou emulador

### Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd maeconecta_flutter
   ```

2. **Instale as dependências**
   ```bash
   flutter pub get
   ```

3. **Execute o aplicativo**
   ```bash
   flutter run
   ```

### Configuração para Desenvolvimento

1. **Configurar emulador Android/iOS**
2. **Verificar dependências**
   ```bash
   flutter doctor
   ```
3. **Executar testes**
   ```bash
   flutter test
   ```

## 📱 Deployment no FlutterFlow

Para importar e fazer deployment no FlutterFlow, consulte o arquivo `GUIA_DEPLOYMENT_FLUTTERFLOW.md` que contém instruções detalhadas sobre:

- Preparação do projeto
- Processo de importação
- Configuração de funcionalidades
- Deployment para lojas de aplicativos
- Solução de problemas

## 📚 Documentação

### Para Desenvolvedores
- **DOCUMENTACAO_TECNICA.md**: Documentação técnica completa
- Arquitetura do sistema
- Modelos de dados
- Serviços e APIs
- Guias de manutenção

### Para Usuários
- **MANUAL_DO_USUARIO.md**: Manual completo para usuários finais
- Como usar todas as funcionalidades
- Dicas de uso
- Solução de problemas
- FAQ

### Para Deployment
- **GUIA_DEPLOYMENT_FLUTTERFLOW.md**: Guia específico para FlutterFlow
- Importação de código
- Configurações necessárias
- Processo de publicação

## 🔒 Segurança e Privacidade

- **Armazenamento Local**: Todos os dados são armazenados localmente no dispositivo
- **Sem Coleta de Dados**: Não coletamos informações pessoais
- **Criptografia**: Dados sensíveis são criptografados
- **Validações**: Todas as entradas são validadas e sanitizadas

## 🏥 Validação Médica

Todas as dicas e recomendações são baseadas em:
- Diretrizes da Sociedade Brasileira de Pediatria (SBP)
- Caderneta da Criança do Ministério da Saúde
- Consensos médicos atualizados
- Revisão por profissionais de saúde

## 🧪 Testes

### Estratégia de Testes
- Testes unitários para modelos e serviços
- Testes de widget para componentes
- Testes de integração para fluxos principais
- Validação manual em dispositivos reais

### Executar Testes
```bash
# Testes unitários
flutter test

# Testes de integração
flutter drive --target=test_driver/app.dart
```

## 📊 Performance

### Otimizações Implementadas
- Lazy loading de dicas
- Cache de dados frequentemente acessados
- Compressão de imagens
- Minimização de rebuilds desnecessários

### Métricas Alvo
- Tempo de inicialização: < 2 segundos
- Resposta de interface: < 200ms
- Uso de memória otimizado
- Bateria eficiente

## 🔧 Configuração de Desenvolvimento

### Variáveis de Ambiente
```dart
// Configurações de desenvolvimento
const bool kDebugMode = true;
const String kAppVersion = '1.0.0';
```

### Dependências Principais
```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.5
  go_router: ^10.1.2
  shared_preferences: ^2.2.0
  sqflite: ^2.3.0
  flutter_local_notifications: ^15.1.0
  intl: ^0.18.1
```

## 🐛 Solução de Problemas

### Problemas Comuns

**Erro de Build**
```bash
flutter clean
flutter pub get
flutter run
```

**Problemas de Dependências**
```bash
flutter pub deps
flutter pub upgrade
```

**Problemas de Emulador**
```bash
flutter doctor
flutter devices
```

## 📈 Roadmap

### Versão 1.1
- [ ] Gráficos de crescimento
- [ ] Integração com dispositivos de saúde
- [ ] Modo offline completo
- [ ] Backup na nuvem

### Versão 1.2
- [ ] Comunidade de mães
- [ ] Chat com especialistas
- [ ] Consultas virtuais
- [ ] Múltiplos bebês

### Versão 2.0
- [ ] Inteligência artificial
- [ ] Reconhecimento de padrões
- [ ] Alertas preditivos
- [ ] Integração com pediatras

## 🤝 Contribuição

### Para Luis e Grupo PIME

Este projeto foi desenvolvido especificamente para vocês. Para contribuir:

1. **Leia toda a documentação** antes de fazer alterações
2. **Mantenha os comentários** em português no código
3. **Teste todas as alterações** antes de fazer commit
4. **Atualize a documentação** quando necessário
5. **Siga as convenções** estabelecidas no código

### Diretrizes de Código
- Use nomes descritivos em português
- Adicione comentários explicativos
- Mantenha consistência no estilo
- Teste todas as funcionalidades

## 📞 Suporte

### Contato
- **Equipe de Desenvolvimento**: Disponível através das configurações do app
- **Documentação**: Consulte os arquivos .md incluídos
- **Issues**: Use o sistema de issues do repositório

### Recursos Úteis
- [Flutter Documentation](https://flutter.dev/docs)
- [FlutterFlow Documentation](https://docs.flutterflow.io)
- [Dart Language Tour](https://dart.dev/guides/language/language-tour)

## 📄 Licença

Este projeto foi desenvolvido especificamente para o Projeto Integrador Multidisciplinar Extensionista (PIME) do curso de Análise e Desenvolvimento de Sistemas do Centro Universitário Belas Artes de São Paulo composto por Bruno P. S., Gabriel A. da S., Jefferson de L. P. e Luiz R. M. Todos os direitos reservados.

## 🙏 Agradecimentos

- **Sociedade Brasileira de Pediatria**: Pelas diretrizes utilizadas e outras fontes pesquisadas.
- **Ministério da Saúde**: Pela Caderneta da Criança e outras fontes pesquisadas.
- **Comunidade Flutter**: Pelo framework e recursos
- **Mães de primeira viagem**: Pela inspiração do projeto

---

**Desenvolvido com ❤️ para apoiar mães de primeira viagem**

**Versão**: 1.0.0  
**Data**: Dezembro 2024  
**Compatibilidade**: Flutter 3.10+, Android 5.0+, iOS 11.0+

