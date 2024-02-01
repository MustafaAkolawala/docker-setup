#!pip3 install openai==0.28.1 -q
#!pip3 install tiktoken -q

import openai

openai.api_key = 'wl5Hy3CDpJWAKBbovXOOeoZZv7XQhgv5'
openai.api_base = "https://api.deepinfra.com/v1/openai"

system_role = """
    You're James Bond, a Sales Agent at XYZ Bank. Your goal is to pitch our credit card.
    Confirm the user's name, ask the location, and whether they are interest in a credit card.
    If interested, mention that a colleague will contact them for details and end the conversation.
    If the user asks about features, provide a brief response in 20 words.
    If the user expresses doubts, address them briefly in 20 words.
    After each response, ask if they're ready to proceed.
    End the conversation when they confirm yes or no. Say goodbye at the end.
"""
user_role =  """ Hello, please ask me about whether interested in credit card or not.
                 if I ask anything provide details in just about 20 words only?
                 """
# Function to call the OpenAI API
def chat_with_openai(messages):

    response = openai.ChatCompletion.create(
        model="meta-llama/Llama-2-7b-chat-hf",
        messages=messages,
        temperature= 0.2
    )
    return response.choices[0].message['content'].strip()

def main():

    name = input('Name: ')
# Initial system message to set the role of the assistant
    messages = [
        {"role": "system", "content" : system_role},
        {"role": "user", "content"   : user_role },
    ]
    assistant_role = 'Hello I am James Bond an AI calling from XYZ Bank am I talking to ' + name
    print("Assistant:", assistant_role)
    messages.append({"role": "assistant", "content": assistant_role })
    user_response = input("You: ")
    messages.append({"role": "user", "content": user_response })
    assistant_response = chat_with_openai(messages)
    print("Assistant:", assistant_response)

    # Assistant asks the user for their name and residence
    while 'bye' not in assistant_response.lower():
      messages.append({"role": "assistant", "content": assistant_response})
      user_response = input("You: ")
      messages.append({"role": "user", "content": user_response})
      assistant_response = chat_with_openai(messages)
      print("Assistant:", assistant_response)

if __name__ == "__main__":
    main()