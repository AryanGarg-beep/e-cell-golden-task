from fastapi import FastAPI
from fastapi.responses import JSONResponse
from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="app/apisc.env")
TOKEN = os.getenv("API")

client = ApifyClient(TOKEN)
app = FastAPI()

@app.get("/profiles")
def get_profiles():
    run_input = { "usernames": ["humansofny", "Aryan"] }
    run = client.actor("dSCLg0C3YEZ83HzYX").call(run_input=run_input)

    results = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    # sort by followers
    results.sort(key=lambda x: x.get("followersCount", 0), reverse=True)

    return JSONResponse(content=results)

from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    run_input = { "usernames": ["humansofny", "archlinux", "finlatics", "corizo.in", "srm_munsoc", "srmist_dsa", "robocraze", "robu.in_", "ecell_srmist", "raspberrypi"] }
    run = client.actor("dSCLg0C3YEZ83HzYX").call(run_input=run_input)

    results = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    results.sort(key=lambda x: x.get("followersCount", 0), reverse=True)

    return templates.TemplateResponse("dashboard.html", {"request": request, "profiles": results})
