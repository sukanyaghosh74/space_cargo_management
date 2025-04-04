from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Item, Container
from app.database import get_db
from app.utils import log_action, optimize_container

router = APIRouter()

@router.post("/rearrange_items/")
def rearrange_items(container_id: str, db: Session = Depends(get_db)):
    container = db.query(Container).filter(Container.container_id == container_id).first()

    if not container:
        raise HTTPException(status_code=404, detail="Container not found.")

    # Fetch all items in the container
    items = db.query(Item).filter(Item.container_id == container_id).all()
    
    # Optimize item placement in container
    updated_positions = optimize_container(items)

    # Update positions in DB
    for item in updated_positions:
        db.query(Item).filter(Item.item_id == item["item_id"]).update(
            {
                "x1": item["start_x"],
                "y1": item["start_y"],
                "z1": item["start_z"],
                "x2": item["end_x"],
                "y2": item["end_y"],
                "z2": item["end_z"],
            }
        )
    db.commit()

    log_action(db, "REARRANGEMENT", container_id, "Rearranged and optimized container.")
    return {"success": True, "message": "Container rearranged successfully."}
