'''
Análise de sentimentos
Link de estudo --> https://www.youtube.com/watch?v=K4rRyAIn0R0
'''
from typing import Dict

from fastapi import Depends, FastAPI
from pydantic import BaseModel

#from classifier.model import Model, get_model
from classifier.model import Model
from classifier.model import get_model

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment=sentiment, confidence=confidence, probabilities=probabilities
    )
    