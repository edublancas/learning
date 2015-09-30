from django.shortcuts import render
from django.shortcuts import redirect

from decks import list_decks, load_deck
from deck_parser import parse_md
from django.http import HttpResponse
from django.http import JsonResponse

from models import Result, Deck

def index(request):
    return redirect('/quizzes/list/')

def new(request):
    return render(request, 'quizzes/new.html')

#Shows a list of all available decks
def listing(request):
    #if post request, save new quiz and then show listing
    if request.method == 'POST':
        #Get name and filename
        name = request.POST['deck-name']
        filename = request.POST['deck-filename']
        #Create new entry in db
        deck = Deck(name=name, filename=filename)
        deck.save()

    #Get available decks
    decks = Deck.objects.all()
    #decks = [{'name':name, 'last_result':res} for name,res in zip(decks, r)]
    context = {'decks': decks}
    return render(request, 'quizzes/listing.html', context)

#Starts a new quiz based on a selected deck
def detail(request, deck_id):
    #Load deck based on id
    deck = Deck.objects.get(id=deck_id)
    txt = load_deck(deck.filename)
    html = parse_md(txt)
    print(len(html))
    context = {'cards' : html, 'deck': deck}
    return render(request, 'quizzes/quiz.html', context)

#Saves the result of a quiz in the database (Result)
#quiz_name, quiz_score, date
def save(request):
    if request.method == 'POST':
        #Create new Result object and populate it with the data
        deck_id = request.POST['deck_id']
        score = float(request.POST['score'])
        res = Result(score=score, deck_id=deck_id)
        #Save it
        res.save()
        #Schedule next date
        #...
        return HttpResponse('Result saved.')

#Show the results for a given deck
#loads html and then and ajax request actually fetches the data
def results(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    context = {'deck': deck}
    return render(request, 'quizzes/quiz_results.html', context)

#Fetch results for a given deck
#returns a json response
def fetch_results(request, deck_id):
    #Query the db for the Results for that deck
    r = Result.objects.filter(deck_id=deck_id)
    #Send datetimes and scores as lists
    dates  = map(lambda x: x.date.strftime("%Y-%m-%d %H:%M:%S") , r)
    scores = map(lambda x: x.score, r)
    print dates
    return JsonResponse({'dates':dates, 'scores':scores})