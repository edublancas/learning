from django.shortcuts import render

from decks import list_decks, load_deck
from deck_parser import parse_md
from django.http import HttpResponse

def index(request):
    context = {'decks': list_decks()}
    return render(request, 'quizzes/index.html', context)

def detail(request, deck_name):
    txt = load_deck(deck_name)
    html = parse_md(txt)
    print(len(html))
    context = {'cards' : html}
    return render(request, 'quizzes/quiz.html', context)