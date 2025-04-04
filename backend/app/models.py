from pydantic import BaseModel
from typing import List, Dict, Optional

class User(BaseModel):
    user_id: str
    name: str
    email: str
    role: str  # e.g., "admin", "participant"

class Event(BaseModel):
    event_id: str
    name: str
    description: str
    date: str
    location: str

class Submission(BaseModel):
    submission_id: str
    user_id: str
    event_id: str
    file_path: str
    timestamp: str

class Review(BaseModel):
    review_id: str
    submission_id: str
    reviewer_id: str
    score: float
    comments: Optional[str] = None

class Config(BaseModel):
    max_submission_size: int
    allowed_file_types: List[str]

# Example constants
DEFAULT_CONFIG = Config(
    max_submission_size=10 * 1024 * 1024,  # 10MB
    allowed_file_types=[".pdf", ".zip"]
)
