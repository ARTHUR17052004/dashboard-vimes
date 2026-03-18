# Dashboard de Monitoramento das VIMEs

Sistema de monitoramento automatizado das VIMEs com coleta de dados no AppCondominial/Bankline, armazenamento em JSON e SQLite e visualização em dashboard com Streamlit.

## Objetivo
Automatizar a coleta e a análise das informações das VIMEs, permitindo acompanhar ocupação, vazios, adimplência, inadimplência e histórico das coletas.

## Tecnologias utilizadas
- Python
- Selenium
- Streamlit
- Pandas
- SQLite
- Matplotlib
- XlsxWriter
- WebDriver Manager

## Funcionalidades
- Login automático no sistema Bankline
- Seleção automática das VIMEs
- Extração de dados das unidades
- Geração de arquivo JSON com os dados atuais
- Salvamento do histórico em banco SQLite
- Dashboard com:
  - filtros por condomínio
  - filtro por adimplência
  - busca por unidade ou responsável
  - indicadores de ocupação
  - resumo por condomínio
  - gráfico de ocupados x vazios
  - gráfico de pizza com distribuição dos ocupados
  - histórico das coletas
  - tabela detalhada
  - exportação para Excel

## Estrutura do projeto
- `login_bankline.py` → automação e coleta de dados
- `dashboard.py` → dashboard em Streamlit
- `database.py` → criação e gravação no banco
- `dados_unidades.json` → dados atuais
- `dashboard.db` → histórico das coletas
- `assets/` → logos e imagens

## Como executar

### 1. Ativar o ambiente virtual
No Windows PowerShell:
```bash
venv\Scripts\Activate.ps1
