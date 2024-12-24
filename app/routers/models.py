from fastapi import APIRouter, HTTPException
import os
from kidneyDiseaseNet.utils.common import decodeImage
from kidneyDiseaseNet.pipeline.prediction import PredictionPipeline
from ..models.image import ImageRequest
# Initialize FastAPI router
router = APIRouter()

# ClientApp equivalent
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()


@router.post("/train/")
async def train_route():
    try:
        os.system("python ../main.py")  # Adjust as per your setup
        return {"message": "Training done successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")

@router.post("/predict/")
async def predict_route(request: ImageRequest):
    
    decodeImage(request.image, clApp.filename)
    result = clApp.classifier.predict()
    return result
    

