from flask import Flask

app = Flask(__name__)

VARIANT_NUMBER = 20

@app.route(f"/api/v1/hello-world-{VARIANT_NUMBER}")
def hello_world():
    return f"Hello World {VARIANT_NUMBER}", 200

if __name__ == "__main__":
    app.run()
