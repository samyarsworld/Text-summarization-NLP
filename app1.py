from text_summarizer.pipeline.target_prediction import TargetPredictionPipeline
import os
import sys
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from text_summarizer.config_manager import ConfigManager
from text_summarizer.exception import CustomException

config = ConfigManager()
prediction_pipeline = TargetPredictionPipeline(config)

app = FastAPI()
# templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost:3000",
    "https://sam-deeplearning.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/index")
async def index(request: Request):
    return "Hello world"

@app.get("/")
async def index():
    return RedirectResponse(url="/index")

# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
    

@app.post("/predict")
async def predict(data: dict):
    try:
        text = data["input"]
        print("PREDICTION STARTED")
        output = prediction_pipeline.run(text)
        print("PREDICTION FINISHED")

        return {"output": output}
    except Exception as e:
        error_message = str(CustomException(e, sys))
        return {"output": error_message}
        # raise HTTPException(status_code=500, detail=f"Internal Server Error: {error_message}")
    

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)

    
    