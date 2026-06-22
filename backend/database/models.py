from sqlalchemy import (
Column,
Integer,
String,
DateTime,
Text
)

from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()

class AttackLog(Base):
    __tablename__ = "attack_logs"
    id = Column(Integer, primary_key=True)
    source_ip = Column(String(100))
    attack_type = Column(String(100))
    severity = Column(Integer)
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class HoneypotLog(Base):
    __tablename__  = "honeypot_logs"
    id = Column(Integer, primary_key=True)
    attacker_ip = Column(String(100))
    event = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Incident(Base):
    __tablename__  = "incidents"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    status = Column(String(50))
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class SecurityEvent(Base):
    __tablename__ = "security_events"
    id = Column(Integer, primary_key=True)
    event_type = Column(String(100))
    severity = Column(String(50))
    source_ip = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
