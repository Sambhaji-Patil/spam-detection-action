# test_detect_spam.py
import pytest
import json
from detect_spam import model # Import the trained model

def test_spam_detection():
    spam_comment = "This is a spam comment with lots of links and bad words."
    ham_comment = "This is a genuine comment about the project."

    assert model.predict([spam_comment])[0] == 1 # Or True, depending on your model's output
    assert model.predict([ham_comment])[0] == 0 # Or False