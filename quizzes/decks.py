import quizzes
import os

def list_decks():
    pth = quizzes.__path__[0]
    files = os.listdir(pth+'/decks')
    files = filter(lambda x: not x.startswith('.'), files)
    return files

def load_deck(deck_name):
    pth = quizzes.__path__[0]
    #Read md file with slides
    f = open(pth+'/decks/'+deck_name)
    txt = f.read()
    return txt