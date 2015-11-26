from bottle import Bottle, run

import sae

app = Bottle()

@app.route('/')
def hello():
    return "Hey, dude!"

application = sae.create_wsgi_app(app)