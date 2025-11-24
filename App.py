from flask import Flask, render_template, request
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_FOLDER = os.path.join(BASE_DIR, "Screenshots")

@app.route("/", methods=["GET", "POST"])
def index():
    screenshots = []

    # load all images from Screenshots folder
    for file in os.listdir(SCREENSHOT_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            screenshots.append(file)

    return render_template("index.html", screenshots=screenshots)

if __name__ == "__main__":
    app.run(debug=True)
