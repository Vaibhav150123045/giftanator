from guess_gift import guess_conversation
from recommend_gift import recommend_gifts
import json

def test_recommend_gifts():
    # relationship, closesness(out of 100), ocassion, importance of occasion (out of 100)
    user_responses = "Sister", "50", "Birthday", "60"
    gift_list_string = ''.join(recommend_gifts(user_responses))
    print(gift_list_string)

def test_guess_conversation():
    gift_to_be_guessed = 'Rolex Submariner Watch'
    conv1 = guess_conversation(gift_to_be_guessed)
    conv2 = guess_conversation(gift_to_be_guessed, conv1, "a bracelet?")
    conv3 = guess_conversation(gift_to_be_guessed, conv2, "Watch?")
    conv4 = guess_conversation(gift_to_be_guessed, conv3, "Apple Watch?")
    conv5 = guess_conversation(gift_to_be_guessed, conv4, "Rolex Watch?")
    print(conv5)


test_guess_conversation()