from sentences import get_determiner, get_noun, get_verb, get_preposition
import pytest




def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
def test_get_noun():
    single_noun = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_noun
    plural_noun = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_noun




def test_get_verb():
    present = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in present
    past = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(2, "past")
        assert word in past
    future = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
    for _ in range(4):
        word = get_verb(3, "future")
        assert word in future
    present_plural = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in present_plural

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in preposition

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
