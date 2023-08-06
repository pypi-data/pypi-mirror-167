import uvicorn
from .v1.app import app as api


def uvicorn_local(**kwargs):
    uvicorn.run(api, **kwargs)


def gunicorn_full():
    print("Starting Gunicorn... NOT")
    pass


def main():
    gunicorn_full()
