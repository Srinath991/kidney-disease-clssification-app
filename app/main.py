from fastapi import FastAPI, Request
from .routers import models
from fastapi.templating import Jinja2Templates

# Initialize the Jinja2 template directory
templates = Jinja2Templates(directory="app/templates")

# Initialize the FastAPI app
app = FastAPI()

# Registration of all the routers
app.include_router(
    models.router,
    tags=["models"],
)

@app.get("/")
async def home(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})
