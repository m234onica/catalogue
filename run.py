import time
from flask import g
from src import create_app
from config import BASE_URL

app = create_app()


@app.context_processor
def url():
    return {'base_url': g.url, 'version': g.version}

@app.before_request
def before_req():
    g.url = BASE_URL
    g.version = time.time()

if __name__ == '__main__':
    app.run()
