import random

def welcome_user():
    user_input = input("Welcome to Higher or Lower! Input 'start' to play: ")
    return user_input.lower() == "start"

def play_game(data):
    playing = True
    while playing:
        # Randomly select two entities
        entity1, entity2 = random.sample(data, 2)

        print(f"Compare A: {entity1['name']}, a {entity1['description']} from {entity1['country']}.")
        print(f"Against B: {entity2['name']}, a {entity2['description']} from {entity2['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if (entity1['follower_count'] > entity2['follower_count'] and guess == 'A') or \
           (entity1['follower_count'] < entity2['follower_count'] and guess == 'B'):
            print("Correct!")
        else:
            print("Incorrect!")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            playing = False

# Data list
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 162,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 194,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 289,
        'description': 'Actor and former wrestler',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 233,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 195,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'National Geographic',
        'follower_count': 195,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Narendra Modi',
        'follower_count': 70,
        'description': 'Prime Minister',
        'country': 'India'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 225,
        'description': 'Media personality',
        'country': 'United States'
    }
]

if welcome_user():
    play_game(data)
