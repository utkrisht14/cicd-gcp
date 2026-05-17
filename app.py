from fastapi import FastAPI
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
async def wish():
    name = os.environ.get("NAME")
    message = f"Happy Birthday! {name}"
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)