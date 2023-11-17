from text_summarizer.pipeline.target_prediction import TargetPredictionPipeline
import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from starlette.responses import RedirectResponse


app = FastAPI()

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    

@app.post("/predict")
async def predict_route(input: str):
    try:
        prediction_pipeline = TargetPredictionPipeline()
        output = prediction_pipeline.predict(input)
        return output
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)