"""
    Deploying the emotion detection for 
    users to be able to interaact with it

"""

#imports required
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

#instantiating the app
app = Flask("Emotion-Detector")

@app.route("/")
def index():
    """
        This method renders the page for the user to input
        the text and recieve a response from 
    """
    return render_template("index.html")

@app.route("/emotionDetector",methods=["GET"])
def detecting_emotion():
    """
        This method interacts with the javascript API
        to be able to access the users input and feed it 
        to the Emotion detector then return a response

    """
    # getting the text to be analyzed
    textToBeAnalyzed = request.args.get["textToAnalyze"]
    
    # getting the emotions from the emotion detector application
    response = emotion_detector(textToBeAnalyzed)

    # formatting he response to desired specification
    ans = "For the given statement,"
    for key,value in response.items():

        if key == "dominant_emotion":
            ans += f". The dominant emotion is {value}."
            break

        ans += f" ' {key}': {value},"

    return ans

if __name__ == "__main__":

    app.run(host="0.0.0.0",port=5000,debug=True)