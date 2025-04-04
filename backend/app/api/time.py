from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models import Item
from app.database import get_db
from app.utils import log_action

router = APIRouter()

@router.post("/api/time/simulate")
def simulate_time(days: int, db: Session = Depends(get_db)):
    """Simulate the passage of time and update item usage and expiry."""
    simulated_date = datetime.utcnow() + timedelta(days=days)
    expired_items = []
    depleted_items = []

    items = db.query(Item).all()
    for item in items:
        if item.usage_limit > 0:
            item.usage_limit -= 1  # Simulate one usage per day
            if item.usage_limit == 0:
                item.is_waste = True
                depleted_items.append(item.item_id)

        if item.expiry_date and datetime.fromisoformat(item.expiry_date) <= simulated_date:
            item.is_waste = True
            expired_items.append(item.item_id)

    db.commit()
    log_action(db, "TIME SIMULATION", None, f"Simulated {days} days forward.")
    return {
        "success": True,
        "simulatedDate": simulated_date.isoformat(),
        "depletedItems": depleted_items,
        "expiredItems": expired_items
    }
