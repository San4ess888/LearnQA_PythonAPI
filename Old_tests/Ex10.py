import pytest
class Phrase:
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Phrase >=15"

