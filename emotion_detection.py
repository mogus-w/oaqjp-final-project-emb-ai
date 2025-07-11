import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key = emotion.get )

        return {
            'anger': emotion['anger'],
            'disgust': emotion['disgust'],
            'fear': emotion['fear'],
            'joy': emotion['joy'],
            'sadness': emotion['sadness'],
            'dominant_emotion': dominant_emotion
        }
    return f"Request failed with status code {response.status_code}: {response.text}"
