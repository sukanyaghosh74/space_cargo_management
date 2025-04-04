from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Item, Container
from app.database import get_db
from app.utils import bin_packing, log_action

router = APIRouter()

@router.post("/place_item/")
def place_item(item_data: dict, db: Session = Depends(get_db)):
    # Extract item information
    item = Item(**item_data)
    db.add(item)
    db.commit()

    # Fetch available containers
    containers = db.query(Container).all()
    placement_result = bin_packing(item, containers)

    if not placement_result["success"]:
        raise HTTPException(status_code=400, detail="No suitable container found.")

    # Log placement action
    log_action(db, "PLACEMENT", item.id, f"Placed in {placement_result['container_id']}")

    return {"message": "Item placed successfully", "container_id": placement_result["container_id"]}
