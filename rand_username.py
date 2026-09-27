import random



def generate():
    adjectives = ['Hungry', 
    'Loving', 
    'Sad', 
    'Master', 
    'Enchanted', 
    'Peachy', 
    'Major', 
    'Slimy', 
    'Chunky', 
    'Burrowing', 
    'Commander', 
    'Suspicious',
    'Chilly',
    'Sleepy',
    'GuyWithThe',
    'DJ',
    'Musical',
    'Von',
    'Shmaloogling',
    'Dr',
    'Cerulean',
    'Dancing',
    'Smart',
    'Baron',
    'Raging']

    nouns = ['Lion', 
    'Zebra', 
    'Ninja', 
    'Fox', 
    'Penguin', 
    'Buddy', 
    'Champ', 
    'Ghost', 
    'Hunter', 
    'Toucan', 
    'Koala', 
    'Observer', 
    'Unicorn',
    'Owl',
    'Skull',
    'Peasant',
    'Shmaloogle',
    'Digger',
    'Junior'
    'Doom',
    'Rabbit',
    'Monster',
    'Hippo',
    'Giraffe',
    'Wabbit']

    return (f"{adjectives[random.randint(0, len(adjectives) - 1)]}{nouns[random.randint(0, len(nouns) - 1)]}")  