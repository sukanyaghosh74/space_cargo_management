from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Item, Log
from app.database import get_db
from app.utils import log_action

router = APIRouter()

@router.post("/retrieve_item/")
def retrieve_item(item_id: str, user_id: str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    # Check if item is expired or out of uses
    if item.remaining_uses <= 0:
        return {"success": False, "message": "Item fully used or expired."}

    # Reduce usage count
    item.remaining_uses -= 1
    db.commit()

    # Log retrieval
    log_action(db, "RETRIEVAL", item.item_id, f"Retrieved by {user_id}")

    return {"success": True, "message": "Item retrieved successfully."}
