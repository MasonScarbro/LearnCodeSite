import assemblyai as aai
import requests
import json
import time

#Problems with youtube links, API error claim of text only and no audio on youtube videos

aai.settings.api_key = "12c5dc58090349efb7d970b4a783d539"

headers = {
    "authorization": "12c5dc58090349efb7d970b4a783d539"
} 
transcriber = aai.Transcriber() #transcriber model

def process_input(user_input):

    base_url = "https://api.assemblyai.com/v2"
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    response = requests.post(base_url + "/upload",
                             headers=headers,
                             data=user_input)
    upload_url = response.json()["upload_url"]

    data = {
    "audio_url": upload_url 
}

    response = requests.post(transcript_endpoint, json=data, headers=headers)

    transcript_id = response.json()['id']
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    # run until transcription is done 
    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()
        
        if transcription_result['status'] == 'completed':
            return transcription_result['text']
            

        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        else:
            time.sleep(3)

