import os
from flask import Flask, render_template, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

# Configuração - secret do Azure Key Vault via App Service Configuration
MISSION_API_KEY = os.environ.get("MISSION_API_KEY", "dev-key-local")
APP_VERSION = "1.2.0"


@app.route("/")
def index():
    """Landing page principal do AstraCloud."""
    return render_template("index.html")


@app.route("/api/mission-status")
def mission_status():
    """Status operacional completo da missão ativa."""
    return jsonify({
        "mission": "AstraLab-01",
        "status": "active",
        "samples_collected": 47,
        "samples_pending": 12,
        "priority_critical": 3,
        "battery_level": 72,
        "radiation_avg": 0.45,
        "regions_explored": 8,
        "uptime_hours": 1847,
        "api_authenticated": MISSION_API_KEY != "dev-key-local",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/samples")
def samples():
    """Dados agregados das amostras coletadas."""
    return jsonify({
        "total": 47,
        "by_type": {
            "rocha_comum": 12,
            "solo_arenoso": 8,
            "solo_escuro": 7,
            "gelo": 5,
            "contaminada": 3,
            "capsula_integra": 9,
            "capsula_danificada": 3
        },
        "by_priority": {
            "critica": 3,
            "alta": 14,
            "media": 18,
            "baixa": 12
        },
        "success_rate": 0.89,
        "last_collection": "2026-06-05T21:32:00Z"
    })


@app.route("/api/regions")
def regions():
    """Dados das regiões exploradas na missão."""
    return jsonify({
        "total_regions": 8,
        "regions": [
            {"id": "R1", "name": "Cratera Norte", "samples": 8, "radiation": 0.32, "status": "completed"},
            {"id": "R2", "name": "Planície Central", "samples": 12, "radiation": 0.28, "status": "completed"},
            {"id": "R3", "name": "Vale Sombrio", "samples": 6, "radiation": 0.67, "status": "completed"},
            {"id": "R4", "name": "Cordilheira Leste", "samples": 5, "radiation": 0.41, "status": "completed"},
            {"id": "R5", "name": "Bacia de Gelo", "samples": 7, "radiation": 0.19, "status": "completed"},
            {"id": "R6", "name": "Depósito Sul", "samples": 4, "radiation": 0.53, "status": "in_progress"},
            {"id": "R7", "name": "Crista Vulcânica", "samples": 3, "radiation": 0.72, "status": "in_progress"},
            {"id": "R8", "name": "Campo de Detritos", "samples": 2, "radiation": 0.38, "status": "planned"}
        ]
    })


@app.route("/api/alerts")
def alerts():
    """Alertas operacionais ativos da missão."""
    return jsonify({
        "active_alerts": 2,
        "alerts": [
            {
                "id": "ALT-007",
                "severity": "high",
                "type": "contamination_risk",
                "message": "Amostra #44 apresenta risco de contaminação elevado na região R6",
                "timestamp": "2026-06-05T20:15:00Z"
            },
            {
                "id": "ALT-008",
                "severity": "medium",
                "type": "battery_warning",
                "message": "Nível de bateria abaixo de 75% — considerar retorno à base",
                "timestamp": "2026-06-05T21:02:00Z"
            }
        ]
    })


@app.route("/health")
def health():
    """Health check para Application Insights e monitoramento."""
    return jsonify({
        "status": "healthy",
        "module": "AstraCloud",
        "version": APP_VERSION,
        "environment": "production" if MISSION_API_KEY != "dev-key-local" else "development",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
