import requests
import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPALSH_KEY = os.environ.get("UNSPLASH_KEY", "")

if not UNSPALSH_KEY:
    raise EnvironmentError(
        "Please create .env.local file and insert the UNSPLASH_KEY")

app = Flask(__name__)


@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": "Client-ID " + UNSPALSH_KEY
    }
    params = {"query": word}

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
