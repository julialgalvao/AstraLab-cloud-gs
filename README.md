# 🚀 AstraCloud — Módulo Cloud & DevOps

**AstraLab** — Plataforma de Coleta Inteligente de Amostras Espaciais

## Sobre

O **AstraCloud** é o módulo de infraestrutura em nuvem do projeto AstraLab. Hospeda o painel de controle da missão, APIs de consulta de amostras e sistema de monitoramento operacional.

## Stack

- **Backend:** Python 3.11 + Flask
- **Cloud:** Microsoft Azure (App Service, Key Vault, Application Insights)
- **CI/CD:** GitHub Actions
- **Segurança:** GitHub Secrets + Azure Key Vault

## Arquitetura

```
GitHub (código) → GitHub Actions (CI/CD) → Azure App Service (aplicação)
                                          → Azure Key Vault (secrets)
                                          → Application Insights (monitoramento)
```

## Endpoints

| Rota | Descrição |
|------|-----------|
| `/` | Landing page com dashboard da missão |
| `/api/mission-status` | Status atual da missão |
| `/api/samples` | Dados das amostras coletadas |
| `/health` | Health check |

## Deploy

Deploy automático via GitHub Actions a cada push na branch `main`.

## Equipe

- Aline Fernandes Zeppelini — RM: 97966
- Camilly Breitbach Ishida — RM: 551474
- Julia Leite Galvão — RM: 550201

## Disciplina

SDTCC — Secure DevOps Tools & Cloud Computing  
FIAP — Global Solution 2026 — 4º Ano Engenharia de Software
