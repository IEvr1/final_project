import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector (text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        # Extracting sentiment label and score from the response
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        result = {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    
                }
        
        dominant_emotion = max(result, key=result.get)
        result['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
         result = {
                                'anger': None,
                                'disgust': None,
                                'fear': None,
                                'joy': None,
                                'sadness': None,
                                
                            }
         result['dominant_emotion'] = None
    return result
