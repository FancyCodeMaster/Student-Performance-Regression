from fastapi import FastAPI,Request, Header, HTTPException
import uvicorn
import gradio as gr
from gradio_app import iface

from prediction import predict_performance
from pydantic import BaseModel

class InputData(BaseModel):
    hrs_std:int
    prev_scores:int
    ex_curr:bool
    sleep_hrs:int
    sam_qns_prac:int

    
app=FastAPI()

@app.post("/predict")
async def predict(input_data:InputData):
    prediction = predict_performance(hours_studied=input_data.hrs_std, previous_scores=input_data.prev_scores,extracurricular=input_data.ex_curr, sleep_hours=input_data.sleep_hrs, sample_questions=input_data.sam_qns_prac)
    
    return {"prediction" : prediction}


app = gr.mount_gradio_app(app, iface, path='/')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
