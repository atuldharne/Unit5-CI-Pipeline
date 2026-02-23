from flask import Flask
import random

app = Flask(__name__)


def get_word(word_type):
    """Function to get a random word based on the type."""
    words = {
        'noun': ['fool', 'knave', 'maiden', 'goblet', 'throne'],
        'verb': ['prithee', 'bewitch', 'frolic', 'jest', 'woo'],
        'adjective': ['merry', 'roguish', 'wretched', 'bawdy', 'gallant'],
        'adverb': ['forsooth', 'merrily', 'verily', 'perchance', 'henceforth'],
        'place': ['tavern', 'enchanted forest', 'castle courtyard', 'village square', 'royal court'],
        'exclamation': ['Hark', 'Zounds', 'Fie', 'Prithee', 'Marry'],
    }
    return random.choice(words[word_type])


def create_story():
    """Function to create a random story based on a template."""
    story_template = (
        "{exclamation}! In the {place}, there appeared a most {adjective} {noun}. "
        "'Twas {adverb} attempting to {verb} beneath the moonlight! "
        "Whereupon I, struck with wonder, did resolve to {verb} most heartily in kind. "
        "What {adjective} mischief hath this day wrought!"
    )
    story = story_template.format(
        exclamation=get_word('exclamation'),
        place=get_word('place'),
        adjective=get_word('adjective'),
        noun=get_word('noun'),
        adverb=get_word('adverb'),
        verb=get_word('verb'),
    )
    return story


@app.route('/')
def home():
    return create_story()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
