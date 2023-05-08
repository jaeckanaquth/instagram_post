import openai
import config

openai.api_key = config.api_key

def post_text(context_for_text):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": context_for_text}
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content


    print(result)
    return result

def image_text(context_for_prompt):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": context_for_prompt}
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(result)
    return result