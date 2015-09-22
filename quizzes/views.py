from django.shortcuts import render

from decks import list_decks, load_deck
from deck_parser import parse_md
from django.http import HttpResponse

from models import Result

#Shows a list of all available decks
def index(request):
    context = {'decks': list_decks()}
    return render(request, 'quizzes/index.html', context)

#Starts a new quiz based on a selected deck
def detail(request, deck_name):
    txt = load_deck(deck_name)
    html = parse_md(txt)
    print(len(html))
    context = {'cards' : html, 'deck_name': deck_name}
    return render(request, 'quizzes/quiz.html', context)

#Saves the result of a quiz in the database (Result)
#quiz_name, quiz_score, date
def save(request):
    if request.method == 'POST':
        #Create new Result object and populate it with the data
        name = request.POST['name']
        score = float(request.POST['score'])
        res = Result(name=name, score=score)
        #Save it
        res.save()
        return HttpResponse('Result saved.')
