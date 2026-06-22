from database.db import SessionLocal
from database.models import SecurityEvent

def create_incident(
        event,
        severity,
        source_ip="unknown"
):

    db = SessionLocal()

    incident = SecurityEvent(
        event_type=event,
        severity=severity,
        source_ip=source_ip
    )

    db.add(incident)

    db.commit()

    db.close()

    return True