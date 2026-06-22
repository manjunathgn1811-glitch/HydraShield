from flask import Flask, request, jsonify
from flask_cors import CORS

# Layer 1
from layer1_network.network_filter import check_ip

# Layer 2
from layer2_reputation.ip_reputation import reputation_check

# Layer 3
from layer3_protocol.protocol_validator import validate_protocol

# Layer 4
from layer4_dpi.packet_inspector import inspect_payload

# Layer 5
from layer5_waf.waf_engine import waf_check

# Layer 6
from layer6_behavior_ai.anomaly_detector import detect_anomaly

# Layer 7
from layer7_response.auto_response import create_incident

# Layer 8
from layer8_autonomous_intelligence.threat_learning import check_feed

# Honeypot
from deception_engine.honeypot import honeypot_trigger

app = Flask(__name__)
CORS(app)


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return jsonify({
        "project": "HydraShield",
        "status": "running",
        "version": "1.0"
    })


# =========================
# HEALTH
# =========================

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "server": "online",
        "database": "connected"
    })


# =========================
# MAIN SECURITY PIPELINE
# =========================

@app.route("/scan", methods=["GET", "POST"])
def scan():

    if request.method == "GET":
        return jsonify({
            "status": "working",
            "message": "/scan endpoint active"
        })

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON data received"
        }), 400

    ip = data.get("ip", "")
    protocol = data.get("protocol", "")
    payload = data.get("payload", "")

    # -------------------------
    # Layer 1
    # -------------------------
    if not check_ip(ip):

        create_incident(
            "Threat Feed Match",
            "CRITICAL",
            ip
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 1",
            "reason": "Firewall Block"
        })

    # -------------------------
    # Layer 2
    # -------------------------
    if not reputation_check(ip):

        create_incident(
            "Malicious Reputation",
            "HIGH"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 2",
            "reason": "Malicious Reputation"
        })

    # -------------------------
    # Layer 3
    # -------------------------
    if not validate_protocol(protocol):

        create_incident(
            "Invalid Protocol",
            "MEDIUM"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 3",
            "reason": "Invalid Protocol"
        })

    # -------------------------
    # Layer 4 DPI
    # -------------------------
    safe_payload, dpi_msg = inspect_payload(payload)

    if not safe_payload:

        create_incident(
            dpi_msg,
            "HIGH"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 4",
            "reason": dpi_msg
        })

    # -------------------------
    # Layer 5 WAF
    # -------------------------
    safe_waf, waf_msg = waf_check(payload)

    if not safe_waf:

        create_incident(
            waf_msg,
            "HIGH"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 5",
            "reason": waf_msg
        })

    # -------------------------
    # Layer 6 AI
    # -------------------------
    payload_size = len(payload)

    is_anomaly = detect_anomaly(
        10,
        payload_size,
        1
    )

    if is_anomaly:

        create_incident(
            "AI Anomaly Detected",
            "HIGH"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 6",
            "reason": "AI Anomaly Detected"
        })

    # -------------------------
    # Layer 8 Threat Feed
    # -------------------------
    if check_feed(ip):

        create_incident(
            "Threat Feed Match",
            "CRITICAL"
        )

        return jsonify({
            "status": "blocked",
            "layer": "Layer 8",
            "reason": "Threat Feed Match"
        })

    return jsonify({
        "status": "allowed",
        "message": "Traffic Accepted",
        "layers_passed": [
            "Layer 1",
            "Layer 2",
            "Layer 3",
            "Layer 4",
            "Layer 5",
            "Layer 6",
            "Layer 8"
        ]
    })


# =========================
# DASHBOARD STATS
# =========================

from database.db import SessionLocal
from database.models import SecurityEvent

@app.route("/dashboard/stats")
def dashboard_stats():

    db = SessionLocal()

    total_events = db.query(
        SecurityEvent
    ).count()

    blocked_ips = db.query(
        SecurityEvent
    ).filter(
        SecurityEvent.severity == "HIGH"
    ).count()

    anomalies = db.query(
        SecurityEvent
    ).filter(
        SecurityEvent.event_type ==
        "AI Anomaly Detected"
    ).count()

    threat_matches = db.query(
        SecurityEvent
    ).filter(
        SecurityEvent.event_type ==
        "Threat Feed Match"
    ).count()

    honeypots = db.query(
        SecurityEvent
    ).filter(
        SecurityEvent.event_type ==
        "Honeypot Triggered"
    ).count()

    db.close()

    return jsonify({
        "total_events": total_events,
        "blocked_ips": blocked_ips,
        "honeypot_hits": honeypots,
        "anomalies": anomalies,
        "threat_feed_matches": threat_matches
    })

# =========================
# DASHBOARD HEALTH
# =========================

@app.route("/dashboard/health")
def dashboard_health():

    return jsonify({
        "status": "healthy",
        "database": "online",
        "threat_feed": "active",
        "server": "running"
    })


# =========================
# DASHBOARD INCIDENTS
# =========================

@app.route("/dashboard/incidents")
def incidents():

    db = SessionLocal()

    rows = db.query(
        SecurityEvent
    ).order_by(
        SecurityEvent.id.desc()
    ).limit(50).all()

    data = []

    for row in rows:

        data.append({
            "id": row.id,
            "event": row.event_type,
            "severity": row.severity,
            "source_ip": row.source_ip,
            "timestamp": str(
                row.timestamp
            )
        })

    db.close()

    return jsonify(data)

# =========================
# HONEYPOT
# =========================

@app.route("/admin")
def fake_admin():

    hp = honeypot_trigger(
        request.remote_addr
    )

    create_incident(
        "Honeypot Triggered",
        "HIGH"
    )

    return jsonify({
        "message": "honeypot",
        "data": hp
    })


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )