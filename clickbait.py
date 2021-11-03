import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['Kansas', 'Missouri', 'Nebraska', 'Iowa', 'North Dakota', 'South Dakota', 'Illinois', 'Ohio', 'Wisconsin',
          'Minnesota', 'Michigan', 'Indiana']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def get_headline_count():
    headline_entry = input(
        "Our website needs to trick people into looking at our ads!"
        "\nEnter the number of clickbait headlines to generate: >")
    try:
        headline_count = int(headline_entry)
        return headline_count
    except Exception as ex:
        print("Please enter a valid number")
        get_headline_count()


def headline_generation(count):
    for i in range(count):
        generation_value = random.randint(1, 7)
        if generation_value == 1 or generation_value == 0:
            headline = generate_are_millennials_killing_headline()
        elif generation_value == 2:
            headline = generate_what_you_dont_know_headline()
        elif i == 3:
            headline = generate_big_companies_hate_her_headline()
        elif i == 4:
            headline = generate_gift_idea_headline()
        elif i == 5:
            headline = generate_job_automated_headline()
        elif i == 6:
            headline = generate_you_dont_want_to_know_headline()
        elif i == 7:
            headline = generate_you_wont_believe_headline()
        elif i == 8:
            headline = generate_reasons_why_headline()
        print(headline)

    website = random.choice(['website', 'blog', 'Facebook', 'Google', 'Twitter', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print(f'\nPost these to our {website}, {when} or you\'re fired!')

def generate_you_wont_believe_headline():
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}"

def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'

def generate_you_dont_want_to_know_headline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return f'What {plural_noun1} Don\'t Want You To Know About {plural_noun2}.'

def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}.'

def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS)
    number2 = random.randint(1, number1)
    return f'{number1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)'

def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.'

def generate_are_millennials_killing_headline():
    noun = random.choice(NOUNS)
    return f'Are Millennials Killing the {noun} Industry?'

def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could Kill You {when}'

def main():
    print("Clickbait Headline Generator")
    headline_count = get_headline_count()
    headline_generation(headline_count)


if __name__ == '__main__':
    main()
