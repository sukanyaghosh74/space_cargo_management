from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import ActionLog
from app.database import get_db

router = APIRouter()

@router.get("/api/logs")
def get_logs(limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(ActionLog).order_by(ActionLog.timestamp.desc()).limit(limit).all()
    return [
        {
            "timestamp": log.timestamp.isoformat(),
            "action": log.action,
            "item_id": log.item_id,
            "message": log.message
        }
        for log in logs
    ]

@router.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    from app.models import Item
    total = db.query(Item).count()
    active = db.query(Item).filter(Item.is_waste == False).count()
    waste = db.query(Item).filter(Item.is_waste == True).count()
    return {
        "totalItems": total,
        "activeItems": active,
        "wasteItems": waste
    }
