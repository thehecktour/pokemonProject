from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_pokemon_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "abilities": []})

@app.post("/pokemon", response_class=HTMLResponse)
async def fetch_pokemon_abilities(request: Request, pokemon_name: str = Form(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            response_data = response.json()
            abilities = sorted([ability['ability']['name'] for ability in response_data['abilities']])
        else:
            abilities = ["Pokémon not found"]

    return templates.TemplateResponse("index.html", {"request": request, "abilities": abilities})
