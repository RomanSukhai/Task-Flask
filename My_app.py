from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

VARIANT_NUMBER = 20

@app.route(f"/api/v1/hello-world-{VARIANT_NUMBER}")
def hello_world():
    """
    Hello World endpoint
    ---
    responses:
      200:
        description: A simple hello world
    """
    return jsonify(message=f"Hello World {VARIANT_NUMBER}"), 200

if __name__ == "__main__":
    app.run()
