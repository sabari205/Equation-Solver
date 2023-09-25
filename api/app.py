import base64
import os
import json
import shutil
from io import BytesIO
from starlette.responses import RedirectResponse

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import main
from calculator import calculate
import uvicorn

app = FastAPI(title="Equation Solver", description="Equation Solver API")

# Enable CORS (Cross-Origin Resource Sharing)
origins = ["*"]  # Replace with your front-end's URL(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageData(BaseModel):
    image: str


router = APIRouter()


@app.post("/predict")
async def predict_equation(data: ImageData):
    print("Hey!!")
    if "internals" in os.listdir():
        shutil.rmtree("internals")
    if "segmented" in os.listdir():
        shutil.rmtree("segmented")
    os.mkdir("segmented")
    operation = BytesIO(base64.urlsafe_b64decode(data.image))
    print(operation)
    operation = main(operation)
    print("operation:", operation)
    formatted_equation, solution = calculate(operation)
    os.mkdir("internals")
    shutil.move("segmented", "internals")
    shutil.move("input.png", "internals")
    if "segmented_characters.csv" not in os.listdir():
        raise HTTPException(
            status_code=400,
            detail={"Entered_equation": "", "Formatted_equation": "", "solution": ""},
        )

    shutil.move("segmented_characters.csv", "internals")
    res = {
        "Entered_equation": operation,
        "Formatted_equation": formatted_equation,
        "solution": solution,
    }
    return json.dumps(res)


app.include_router(router)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")
    # A welcome message to test our server
    # return {"message": "Equations Solver"}


if __name__ == "__main__":
    host = os.getenv("API_URL", "http://localhost")
    uvicorn.run(app, host=host, port=8000, debug=True)
