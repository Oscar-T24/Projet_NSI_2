# create.py


import json
import os
from pathlib import Path
import openai
from datetime import date
now = date.today()

def create():
    PROMPT = input(' \n entrer un descriptif d"image à créer \n')

    DATA_DIR = Path.cwd() / "responses"


    #DATA_DIR.mkdir(exist_ok=True)


    openai.api_key = "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"


    response = openai.Image.create(

        prompt=PROMPT,

        n=1,

        size="256x256",

        response_format="b64_json",

    )


    #file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
    nom = 'image_open_AI_generee-le_str'+str(now)+".json"
    file_name = DATA_DIR / nom


    with open(file_name, mode="w", encoding="utf-8") as file:

        json.dump(response, file)
'''
def variation(image):
    response = openai.Image.create_variation(
    image=open("corgi_and_cat_paw.png", "rb"),
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
'''