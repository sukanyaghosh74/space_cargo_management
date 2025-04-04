from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Item

router = APIRouter(prefix="/waste", tags=["waste"])

@router.get("/")
def get_waste_items(db: Session = Depends(get_db)):
    """
    Retrieve all items that are marked as waste (expired or discarded).
    """
    waste_items = db.query(Item).filter(Item.is_waste == True).all()
    return {"waste_items": waste_items}

@router.put("/mark/{item_id}")
def mark_as_waste(item_id: int, db: Session = Depends(get_db)):
    """
    Mark an item as waste manually.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item.is_waste = True
    db.commit()
    db.refresh(item)
    return {"message": "Item marked as waste", "item": item}

@router.delete("/remove/{item_id}")
def remove_waste(item_id: int, db: Session = Depends(get_db)):
    """
    Permanently delete a waste item from the database.
    """
    item = db.query(Item).filter(Item.id == item_id, Item.is_waste == True).first()
    if not item:
        raise HTTPException(status_code=404, detail="Waste item not found or not marked as waste")
    
    db.delete(item)
    db.commit()
    return {"message": "Waste item deleted"}

@router.delete("/clear")
def clear_all_waste(db: Session = Depends(get_db)):
    """
    Delete all waste items at once.
    """
    deleted_count = db.query(Item).filter(Item.is_waste == True).delete()
    db.commit()
    return {"message": f"Deleted {deleted_count} waste items"}
