import random



def generate():
    adjectives = ['Hungry', 'Loving', 'Sad']
    nouns = ['Lion', 'Zebra', 'Ninja']

    return (f"{adjectives[random.randint(0, len(adjectives) - 1)]}{nouns[random.randint(0, len(nouns) - 1)]}")  