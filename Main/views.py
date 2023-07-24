from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import transcribe
from django.http import JsonResponse
import openai
from decouple import config


openai_api_key = config('OPENAI_API_KEY')
openai.api_key = openai_api_key


# Create your views here.
def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are a Helpful Assistant and Tutor"},
            {"role": "user", "content": message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer


def index(request):
    template = 'index.html'

    if request.method == 'POST':
        user_input_url = request.POST.get('user_input_url')
        transcript = transcribe.process_input(user_input_url)
        request.session['transcript'] = transcript  # Store the transcript in the session
        return redirect('chatTest')  # Redirect to the chat page
    return render(request, 'index.html')
    
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

def chatTest(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    else:
        # Send the initial message from the backend
        initial_message = request.session.get('transcript') #Supposedly pulls from the transcript
        return render(request, 'chatTest.html', {'initial_message': initial_message})