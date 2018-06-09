from greeter import Greeter
from insult_comic import InsultComic

if __name__ == "__main__":
    people  = (Greeter(), InsultComic())
    for peeps in people:
        peeps.speak()
