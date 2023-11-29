import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer
from transformers import pipeline
from text_summarizer.exception import CustomException
import sys

app = FastAPI()

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

@app.get("/")
async def index():
    return "Hello world"


@app.post("/predict")
async def predict(data: dict):
    try:
        text = data["input"]
        tokenizer = AutoTokenizer.from_pretrained("artifacts/model_trainers/pegasus-cnn_dailymail/tokenizer")
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        model_pipeline = pipeline("summarization", model="artifacts/model_trainers/pegasus-cnn_dailymail/model",tokenizer=tokenizer)

        print("PREDICTION STARTED")

        output = model_pipeline(text, **gen_kwargs)[0]["summary_text"]
        output = output.replace("<n>", "\n")
        output = output.replace(" .", ".")

        print("PREDICTION FINISHED")
        return {"output": output}
    
    except Exception as e:
        error_message = str(CustomException(e, sys))
        return {"output": error_message}
    

# if __name__=="__main__":
    # uvicorn.run(app, host="localhost", port=8080)

