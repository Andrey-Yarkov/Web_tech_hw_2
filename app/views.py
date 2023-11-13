from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        } for i in range(10)
    ]

TAGS = [
    {
        'id': i,
        'name': f'tag{i}'
    } for i in range(3)
]

def paginate(object, page, per_page=5):
    paginator = Paginator(object, per_page)
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        # If the page is empty, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    return page_obj

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', context={'questions': paginate(QUESTIONS, page)})

def tag(request, tag_name):
    page = request.GET.get('page', 1)
    tag_item = next(item for item in TAGS if item['name'] == tag_name)
    return render(request, 'tag.html', context={'tag': tag_item, 'questions_by_tag': paginate(QUESTIONS, page)})

def hot(request):
    page = request.GET.get('page', 1)
    return render(request, 'hot.html', context={'hot_questions': paginate(QUESTIONS, page)})

def question(request, question_id):
    question_item = QUESTIONS[question_id]
    page = request.GET.get('page', 1)
    return render(request, 'question.html', context={'question': question_item, 'answers': paginate(ANSWERS, page)})

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')