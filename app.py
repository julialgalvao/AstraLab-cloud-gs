import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Configuração - o secret vem do Azure Key Vault (via App Service Configuration)
MISSION_API_KEY = os.environ.get("MISSION_API_KEY", "dev-key-local")


@app.route("/")
def index():
    """Landing page principal do AstraCloud."""
    return render_template("index.html")


@app.route("/api/mission-status")
def mission_status():
    """API endpoint - status da missão (demonstra funcionamento)."""
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
        "api_authenticated": MISSION_API_KEY != "dev-key-local"
    })


@app.route("/api/samples")
def samples():
    """API endpoint - dados de amostras coletadas."""
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
        "success_rate": 0.89
    })


@app.route("/health")
def health():
    """Health check para Application Insights."""
    return jsonify({"status": "healthy", "module": "AstraCloud"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
