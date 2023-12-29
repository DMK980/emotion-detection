"""
    This module is to interact with 
    the Watson NLP libraries to 
    harness the emotion detection
    capabilites 

"""

# importing required libraries
import requests
import json

def emotion_detector(text_to_analyze):
    """
        This method is for taking a text input from the 
        frontend and passing it into the an API to interact
        with the Watson NLP libraries and recieve a response 
        of the emotion detected form the text

    """

    # Required Parameters 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text = { "raw_document": { "text": text_to_analyze } }

    # calling the api using post
    response = requests.post(url,json=text,headers = header)

    # formatting the text and retrieving the emotions only
    formatted_text = json.loads(response.text)
    emotions = formatted_text["emotionPredictions"][0]["emotion"]
    
    # finding the strongest emotion and its name
    strongest = max(emotions.values())
    emot_name = ""
    
    for emotion in emotions:
        if emotions[emotion] == strongest:
            emot_name = emotion
    
    emotions["dominant_emotion"] = emot_name
    

    # return the result
    return emotions

#emotion_detector("I am so happy i am doing this")
