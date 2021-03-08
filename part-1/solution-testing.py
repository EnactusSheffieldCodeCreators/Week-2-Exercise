# Simple testing for the count_words function in solution.py.
# Run "pytest solution-testing.py" to run the tests.

# ===== Imports =====
import pytest

from solution import count_words # Method we are testing here.

# ===== Constants =====
# The TEXT_1 is a sample text that is manually broken down in the TEXT_1_COUNT dict.
TEXT_1 = "Hello, my name is Bob! It's a pleasure to meet you. How are you doing?"
TEXT_1_COUNT = {
    "hello": 1,
    "my": 1,
    "name": 1,
    "is": 1,
    "bob": 1,
    "it's": 1,
    "a": 1,
    "pleasure": 1,
    "to": 1,
    "meet": 1,
    "you": 2,
    "how": 1,
    "are": 1,
    "doing": 1,
    "me": 0,
    "oi": 0,
    " lol ": 0,
    " ": 0
    }


def test_count_words_single_words():
    # Testing single word counts.
    for word in TEXT_1_COUNT:
        count = TEXT_1_COUNT[word]
        assert count == count_words([word], TEXT_1)
        # Line below is for debugging.
        # print("{} : {}".format(count, count_words([word], TEXT_1)))

def test_count_words_multiple_words():
    # Testing combinations of 2 words.
    for word1 in TEXT_1_COUNT:
        for word2 in TEXT_1_COUNT:
            if word1 != word2:
                count1 = TEXT_1_COUNT[word1]
                count2 = TEXT_1_COUNT[word2]
                assert (count1 + count2) == count_words([word1, word2], TEXT_1)
