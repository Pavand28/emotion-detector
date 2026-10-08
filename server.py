from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyse = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyse:
        return "Please enter a text to analyze.", 400

    result = emotion_detector(text_to_analyse)

    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
