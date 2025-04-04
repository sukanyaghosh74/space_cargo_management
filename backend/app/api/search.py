from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.models import Item, Container
from app.database import get_db

router = APIRouter()

@router.get("/search_item/")
def search_item(
    item_id: str = Query(None),
    item_name: str = Query(None),
    db: Session = Depends(get_db),
):
    # Search by item ID or name
    if item_id:
        item = db.query(Item).filter(Item.item_id == item_id).first()
    elif item_name:
        item = db.query(Item).filter(Item.name.ilike(f"%{item_name}%")).first()
    else:
        raise HTTPException(status_code=400, detail="Provide item_id or item_name.")

    if not item:
        return {"found": False, "message": "Item not found."}

    # Get container info
    container = db.query(Container).filter(Container.container_id == item.container_id).first()
    position = {
        "startCoordinates": {"width": item.x1, "depth": item.y1, "height": item.z1},
        "endCoordinates": {"width": item.x2, "depth": item.y2, "height": item.z2},
    }

    return {
        "success": True,
        "found": True,
        "item": {
            "itemId": item.item_id,
            "name": item.name,
            "containerId": item.container_id,
            "zone": container.zone,
            "position": position,
        },
    }
