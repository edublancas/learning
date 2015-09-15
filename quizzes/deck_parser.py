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

def enclose_in_section(slide):
    sides = slide.split("<p>-</p>")
    return '<section><section>'+sides[0]+'</section><section>'+sides[1]+'</section></section>'
