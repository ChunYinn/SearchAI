from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the frontend URL if different
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a model for the request body
class RequestData(BaseModel):
    data: list[str]

@app.post("/generateclick")
async def generate_click(data: RequestData):
    # Log each URL
    for url in data.data:
        print(f"URL: {url}")
    
    # Process the request data here
    response = {"message": f"Received data", "urls": data.data}
    return response

# If you need to run the app directly for development
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
