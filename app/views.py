from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tag(request):
    return render(request, 'tag.html')

def hot(request):
    return render(request, 'hot.html')

def question(request):
    return render(request, 'question.html')

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')