from fastapi import FastAPI
from app.api import placement, retrieval, waste, simulation, logs

app = FastAPI(title="ISS Cargo Management System")

# Include API routers
app.include_router(placement.router, prefix="/api/placement", tags=["Placement"])
app.include_router(retrieval.router, prefix="/api/search", tags=["Search"])
app.include_router(waste.router, prefix="/api/waste", tags=["Waste"])
app.include_router(simulation.router, prefix="/api/simulate", tags=["Simulation"])
app.include_router(logs.router, prefix="/api/logs", tags=["Logs"])

@app.get("/")
def read_root():
    return {"message": "ISS Cargo Management API is running 🚀"}
