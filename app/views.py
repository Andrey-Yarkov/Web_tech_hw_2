from django.shortcuts import render
from django.http import HttpResponse

# global data
QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Question text question text {i}'
        } for i in range(20)
    ]

ANSWERS = [
        {
            'id': i,
            'content': f'Answer text answer text {i}'
        } for i in range(3)
    ]

TAGS = [
    {
        'id': i,
        'name': f'tag{i}'
    } for i in range(3)
]

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', context={'questions': QUESTIONS})

def tag(request, tag_name):
    tag_item = next(item for item in TAGS if item['name'] == tag_name)
    return render(request, 'tag.html', context={'tag': tag_item, 'questions_by_tag': QUESTIONS})

def hot(request):
    return render(request, 'hot.html', context={'hot_questions': QUESTIONS})

def question(request, question_id):
    question_item = QUESTIONS[question_id]
    return render(request, 'question.html', context={'question': question_item, 'answers': ANSWERS})

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')