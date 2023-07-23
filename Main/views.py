from django.shortcuts import render
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

    if request.method == 'POST': #POST needed for from submission see docs, if form was submitted
        user_input = request.POST.get('user_input_url', '')  # Get the input value from the POST data
        result = transcribe.process_input(user_input)  # Call the function from transcribe.py
        context = {'result': result} #stored context dict with key result, making it accesible in the template
        return render(request, template, context)
    context = {}
    return render(request, template, context)
    
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
        