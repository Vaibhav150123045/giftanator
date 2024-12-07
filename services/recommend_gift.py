import openai
import config as config
import json
import os

openai.api_key = config.API_KEY

def recommend_gifts(user_responses):

    # Open and read the JSON file
    with open('./gift_items.json', 'r') as file:
        gifts_set = json.load(file)

    ques_1 = f"What type of relationship do you have with the person?"
    ans_1 = user_responses[0]
    ques_2 = f"How close are you to your {ans_1}?"
    ans_2 = user_responses[1]
    ques_3 = f"What is the occasion?"
    ans_3 = user_responses[2]
    ques_4 = f"How important is this {ans_3} to you?"
    ans_4 = user_responses[3]

    base_instruction = f'''
            The backstory behind the task is that, \'user1\' is trying to get gift recommendations
            for \'user2\'.
            You are an assistant who will recommend gifts to \'user1\' from the set of gifts provided
            to you. You will recieve details about \'user2\', their relationship with \'user1\' and 
            what is the occasion. And you have to provide gift suggestions according to these details 
            provided below: Provide your answer in the format [\'Gift 1\', \'Gift 2\', \'Gift 3\']'

            Questions and \'user1\'s\' responses to them are given as below -
            Question_1: {ques_1}
            Answer_1: {ans_1}
            Question_2: {ques_2}
            Answer_2: {ans_2}
            Question_3: {ques_3}
            Answer_3: {ans_3}
            Question_4: {ques_4}
            Answer_4: {ans_4}
            According to the answers to above questions you have to provide 3 gift suggestions for \'user2\'.

            The set of gifts from which you have to recommend is:
            ''' + str(gifts_set)

    message = [{"role": "user", "name": "user1", "content": base_instruction}]

    chat_response = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=message,
        max_tokens=1000,
        temperature=0.5,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0)

    return list(chat_response.choices[0].message.content)
