from random import shuffle
import mistune

def parse_md(txt, shuffle_slides=True):
    md = mistune.Markdown()
    #Split each slide (Separator: \n--\n)
    slides = txt.split('\n--\n')
    slides = map(md, slides)
    slides = map(enclose_in_section, slides)
    if shuffle_slides:
        shuffle(slides)
    return slides

#Enclose in section tags
#also add data tag so frontend knows if it's question or answer
def enclose_in_section(slide):
    sides = slide.split("<p>-</p>")
    return '<section><section data-type="question">'+sides[0]+'</section><section data-type="answer">'+sides[1]+'</section></section>'
