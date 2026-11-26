""" Web deployment of the application """

from flask import Flask,render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index():
    """
    Render the template index.html when access to '/' using GET method
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """
    Get textToAnalyze from static file 'mywebscript.js' and sent it to
    emotion_detector function, if response is valid returns the values
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': "
            f"{response['joy']} and 'sadness': {response['sadness']}. The dominant emotion "
            f"is {response['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
