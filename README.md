AstraLab — Secure DevOps Tools & Cloud Computing - Global Solutions 4ESR

**AstraCloud** — Plataforma de Coleta Inteligente de Amostras Espaciais

## Integrantes

- Aline Fernandes Zeppelini — RM: 97966
- Camilly Breitbach Ishida — RM: 551474
- Julia Leite Galvão — RM: 550201

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
| `/api/mission-status` | Status operacional completo da missão ativa |
| `/api/samples` | Dados agregados das amostras por tipo e prioridade |
| `/api/regions` | Regiões exploradas com status e radiação |
| `/api/alerts` | Alertas operacionais ativos |
| `/health` | Health check para monitoramento |

## Deploy

Deploy automático via GitHub Actions a cada push na branch `main`.




## Disciplina

SDTCC — Secure DevOps Tools & Cloud Computing  
FIAP — Global Solution 2026 — 4º Ano Engenharia de Software
