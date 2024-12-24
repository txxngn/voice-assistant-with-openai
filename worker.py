from openai import OpenAI
import requests

openai_client = OpenAI()

#1.
def speech_to_text(audio_binary):
    #Set up Watson Speech-to-Text HTTP Api url
    base_url = 'https://sn-watson-stt.labs.skills.network'
    api_url = base_url+'/speech-to-text/api/v1/recognize'

    #Set up parameters for HTTP request (select language)
    params = {
        'model': 'en-US_Multimedia'
    }

    #Set up body of HTTP request
    body = audio_binary

    #Send a HTTP Post request
    requests.post(api_url, params=params, data=audio_binary).json()

    #Parse the response to get transcribed text
    text = 'null'
    while bool(response.get('results')): #check if the response contains any results
        print('speech to text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text: ', text)
        return text

#3.
def text_to_speech(text, voice=""):
    #Set up Watson tts HTTP Api url
    base_url='https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    #Adding voice as parameter to the api_url if it's not empty or not default (the user has selected a preferred voice)
    if voice != "" and voice != "default":
        api_url += "&voice=" +voice  #append a voice parameter to the api_url if the user has sent a preferred voice

    #Set the headers dictionary for HTTP request
    headers = {
        'Accept': 'audio/wav', #tells Watson i'm sending an audio having wav format
        'Content-Type': 'application/json',
    }

    #Set the body of HTTP request, this text will then be processed and converted to a speech.
    json_data = {
        'text': text,
    }

    #Send a http Post request to Watson Text-to-Speech Service
    response = requests.port(api_url, headers=headers, json=json_data)
    print('text to speech resonse:', response)
    return response.content

#2.
#Take in a prompt and pass it to OpenAI's GPT-3 API
def openai_process_message(user_message): 
    #Set the prompt for OpenAI Api
    #This prompt based on my preference, this case telling model to become a personal assistant, giving it specific tasks its capable of doing, can be modified
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    
    #Call the OpenAI Api to process prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_token=4000
    )
    print("openai response:", openai_response)
    
    #Parse the response to get the response message for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text
