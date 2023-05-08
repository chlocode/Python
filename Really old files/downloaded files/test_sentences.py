from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #test single nouns
    single_noun = [ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_noun
    
    #test plural nouns
    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_noun

def test_get_verb():
    #test past tense verb
    past_tense_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):

        # Call the get_verb function which
        # should return a verb in past tense.
        word = get_verb("past", 2)

        # Verify that the word returned from get_verb
        # is one of the words in the past tense verb list.
        assert word in  past_tense_verb 
    
    #test present tense verb
    present_tense_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):

        # Call the get_verb function which
        # should return a verb in present tense.
        word = get_verb("present", 1)

        # Verify that the word returned from get_verb
        # is one of the words in the present tense verb list.
        assert word in  present_tense_verb 
    
    #test present tense, plural verb
    present_tense_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):

        # Call the get_verb function which
        # should return a verb in present tense for a plural noun.
        word = get_verb("present", 2)

        # Verify that the word returned from get_verb
        # is one of the words in the present tense, plural verb list.
        assert word in  present_tense_verb 
    
    #test future tense verb
    future_tense_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):

        # Call the get_verb function which
        # should return a verb in future tense.
        word = get_verb("future", 2)

        # Verify that the word returned from get_verb
        # is one of the words in the futureTense_verb list.
        assert word in  future_tense_verb 

def test_get_preposition():
    #test preposition
    preposition=[ "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    
    for _ in range(4):
         word= get_preposition()
         assert word in preposition

def test_get_prepositional_phrase():
    #test prepostional phrase
    phrase1=get_preposition(), get_determiner(1), get_noun(1)
    phrase2=get_preposition(), get_determiner(2), get_noun(2)
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a random prepositional phrase 
        word = get_prepositional_phrase(phrase1)
        word2=get_prepositional_phrase(phrase2)

        # Verify that the word returned from get_prepositional_phrase
        # is one of the words in the get_preposition, get_determiner and get_noun list.
        assert word in  phrase1 
        assert word2 in phrase2
    return
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])