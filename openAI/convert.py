# convert.py


import json
from base64 import b64decode
from pathlib import Path
from datetime import date

now = date.today()

def convert():
    DATA_DIR = Path.cwd() / "responses"

    #JSON_FILE = DATA_DIR / '/Users/oscartesniere/Documents/GitHub/Projet_NSI_2/responses/image_AI.json'
    nom = '/Users/oscartesniere/Documents/GitHub/Projet_NSI_2/responses/image_open_AI_generee-le_'+str(now)+'.json'
    JSON_FILE = DATA_DIR / nom
    IMAGE_DIR = Path.cwd() / "images" #/ JSON_FILE.stem


    #IMAGE_DIR.mkdir(parents=True, exist_ok=True)


    with open(JSON_FILE, mode="r", encoding="utf-8") as file:

        response = json.load(file)


    for index, image_dict in enumerate(response["data"]):

        image_data = b64decode(image_dict["b64_json"])

        image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"

        with open(image_file, mode="wb") as png:

            png.write(image_data)