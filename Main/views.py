from django.shortcuts import render
from django.http import HttpResponse
from . import transcribe

# Create your views here.

def index(request):
    template = 'index.html'

    if request.method == 'POST': #POST needed for from submission see docs, if form was submitted
        user_input = request.POST.get('user_input_url', '')  # Get the input value from the POST data
        result = transcribe.process_input(user_input)  # Call the function from transcribe.py
        context = {'result': result} #stored context dict with key result, making it accesible in the template
        return render(request, template, context)
    context = {}
    return render(request, template, context)
    
