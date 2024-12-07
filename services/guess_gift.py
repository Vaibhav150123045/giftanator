import openai
import config as config

openai.api_key = config.API_KEY

def guess_conversation(gift_to_be_guessed, current_conversation = None, user_guess = None):

    system_message = '''You are an AI host that assist users to find a surprise gift curated for them. The back story
                    behind the game is that \'user1\' has bought a gift for \'user2\' which is a complete surprise for \'user2\'
                    You have to assist \'user2\' to guess the surprise gift curated for them. The gift item name to be guessed by 
                    \'user2\' will be provided to you by \'user1\'. You never reveal the right answer to \'user2\'. 
                    You provide probing clues to identify where \'user2\' might be needing help, provide hints and guidance, 
                    and provide directional feedback to indicate if the user is moving in the right direction.
                    '''
    
    if(user_guess == None):
        current_conversation = [
            {"role": "system", "name":"assistant", "content": system_message},
            {"role": "system", "name":"example_user1", "content": "The gift item to be guessed is: \'Rolex Sabmariner Oyester Watch\'"},
            {"role": "system", "name":"example_assistant", "content": "It is a wearable which can act as a jewellry as well."},
            {"role": "system", "name":"example_user2", "content": "Is it a bracelet?"},
            {"role": "system", "name":"example_assistant", "content": "Well, you have the right idea, can you think of some other thing that can be wore on the wrist?"},
            {"role": "system", "name":"example_user2", "content":"Is it a watch?"},
            {"role": "system", "name":"example_assistant", "content": "Great guess! Yes, it is a watch!! Congratulations! Now let's try to guess the brand of the watch because that's gonna be a great surprise too! The surprise gift is a luxury watch known for its quality and style. It is a popular choice among watch enthusiasts and collectors. It is designed to be durable and reliable, with a sleek and timeless design. Can you think of a specific brand or model that matches this description?"},
            {"role": "system", "name":"example_user2", "content": "Is it Tissot?"},
            {"role": "system", "name":"example_assistant", "content": "Let me give you another clue. The brand of this watch is highly regarded in the watch industry and is synonymous with luxury and prestige. It is known for its craftsmanship, precision, and iconic designs. This particular model is often referred to as the \"king of divers\" and is favored by professionals and adventurers alike. Can you think of any watch that fits this description?"},
            {"role": "system", "name":"example_user2", "content": "Is it a Rolex watch?"},
            {"role": "system", "name":"example_assistant", "content": "Yes, you got it! The surprise gift is indeed a Rolex watch. Specifically, it is the Rolex Submariner Oyster Watch. Congratulations on guessing it correctly! It's a remarkable timepiece known for its elegance, durability, and functionality. Well done! Exiting the program!"},
            {"role": "user", "name": "user1", "content": f"The gift item to be guessed is: {gift_to_be_guessed}"}
          ]
        
        next_question = generate_next_ques(current_conversation, user_guess)

        current_conversation.append({"role": "assistant", "content": next_question})

        print("\n", "AI host:")
        print(next_question)
        print("\n")
    else:
        if "exit" in user_guess.lower():
            print("AI Host: Exiting the program!")
            return False
        if len(current_conversation) <= 20:
            current_conversation.append({"role": "user", "name": "user2", "content": user_guess})
            print("\n", "User:")
            print(user_guess)
            print("\n")

            next_question = generate_next_ques(current_conversation, user_guess)
            current_conversation.append({"role": "assistant", "content": next_question})

            print("\n", "AI host:")
            print(next_question)
            print("\n")
        else:
            ending_string = f"That was a cool game we played, well tried, you were so close to the answer. Let me tell you that the surprise that has been gifted to you is {gift_to_be_guessed}"
            current_conversation.append({"role": "assistant", "content": ending_string})
        
    return current_conversation



def generate_next_ques(prev_messages, user_guess):
    chat_response = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages = prev_messages).choices[0].message.content
    
    return chat_response