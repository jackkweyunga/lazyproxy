# out of flask
from app import app
import requests


# flask imports
from flask import redirect, url_for, request


@app.route("/", methods=["POST", "GET"])
def root():
    return {"status": "working"}

@app.route("/nin/<nin>", methods=["POST", "GET"])
def nida(nin):

    if get_resource(nin):

        return {
            "status":"ok",
            "results":get_resource(nin)
        }
    return {
            "status":"not ok",
            "results":get_resource(nin)
        }


def get_resource(nin):

    url = f"https://ors.brela.go.tz/um/load/load_nida/{nin}"
   
    headers = {
        'Content-Type': 'application/json',
    }
    rq = requests.post(
        url = url,
        headers=headers
        )

    return rq.json()
