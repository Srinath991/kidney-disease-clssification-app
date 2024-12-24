from pydantic import BaseModel

# Request model for prediction
class ImageRequest(BaseModel):
    image: str