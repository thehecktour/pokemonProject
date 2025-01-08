from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_pokemon_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "abilities": [

    ]})


@app.post("/pokemon", response_class=HTMLResponse)
async def fetch_pokemon_abilities(request: Request, pokemon_name: str = Form(...)):
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = await client.get(url)
        if response.status_code == 200:
            response_data = response.json()
            abilities = [
                ability['ability']['name'] for ability in response_data['abilities']
            ]
            abilities = sorted(abilities)
        else:
            abilities = ["Pokémon not found"]

    context = {"request": request, "abilities": abilities}
    return templates.TemplateResponse("index.html", context)
