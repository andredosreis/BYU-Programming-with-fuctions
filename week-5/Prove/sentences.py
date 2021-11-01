import random

# Create a list of strings and assign
# the list to a variable named words.
#words = ["boy", "girl", "cat", "dog", "bird", "house"]


# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
#words = random.choice(words)

def main():

    tense_1 = 'present'
    tense_2 = 'past'
    tense_3 = 'future'

    # 1 for present and 2 for plural
    number = 1
    second_number = 2

    make_sentences(number, tense_2)
    make_sentences(second_number, tense_2)
    make_sentences(number, tense_1)
    make_sentences(second_number, tense_1)
    make_sentences(number, tense_3)
    make_sentences(second_number, tense_3)
    make_sentences_2(number, tense_2)
    make_sentences_2(second_number, tense_2)
    make_sentences_2(number, tense_1)
    make_sentences_2(second_number, tense_1)
    make_sentences_2(number, tense_3)
    make_sentences_2(second_number, tense_3)

    # article = get_determiner(grammatical_number)
    # noun = get_noun(grammatical_number)
    # verb = get_verb(grammatical_number, tense)
    # preposition = get_preposition()

    # return print(article+" "+noun+" "+verb+""+preposition)

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """

    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if grammatical_number == 1:
        words = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    word = random.choice(words)

    return word


def get_verb(grammatical_number, tense):

    """Return a randomly chosen verb. If tense is "past", this
        function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and grammatical_number is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and grammatical_number is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameter
            grammatical_number: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.

        """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present" and grammatical_number is 1:
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and grammatical_number is not 1:
        verbs = [ "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

 # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    det = get_determiner(quantity)
    phrase =  f"{get_preposition()} {det} {get_noun(quantity)}"

    return phrase

def make_sentences(grammatical_number,tense):
    det = get_determiner(grammatical_number).capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number,tense)
    phrase = (f"{det} {noun} {verb}.")
    print(phrase)

def make_sentences_2(grammatical_number,tense):
    det = get_determiner(grammatical_number).capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number,tense)
    phrase = (f"{det} {noun} {verb}")
    print (phrase, end = ' ')
    make_prepositional(grammatical_number)

def make_prepositional(grammatical_number):
    prepositional = get_prepositional_phrase(grammatical_number)
    print(prepositional)

main()
"""#a.	single	past
main(1, "past")
#b.	plural	past
main(0, "past")
#c.	single	present
main(1, "present")
#d.	plural	present
main(0, "present")
#e.	single	future
main(1, "future")
#f.	plural	future
main(0, "future")"""



