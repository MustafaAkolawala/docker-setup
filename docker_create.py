import openai

openai.api_key = 'wl5Hy3CDpJWAKBbovXOOeoZZv7XQhgv5'
openai.api_base = "https://api.deepinfra.com/v1/openai"

system_role = """
    You're James Bond, a Sales Agent at XYZ Bank. Your goal is to pitch our credit card.
    Confirm the user's name, ask the location, and whether they are interested in a credit card.
    If interested, mention that a colleague will contact them for details and end the conversation.
    If the user asks about features, provide a brief response in 20 words.
    If the user expresses doubts, address them briefly in 20 words.
    After each response, ask if they're ready to proceed.
    End the conversation when they confirm yes or no. Say goodbye at the end.
"""
user_role = """ Hello, please ask me about whether interested in a credit card or not.
                 If I ask anything, provide details in just about 20 words only?
             """

# Function to call the OpenAI API
def chat_with_openai(messages):
    response = openai.ChatCompletion.create(
        model="meta-llama/Llama-2-7b-chat-hf",
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message['content'].strip()

def lambda_handler(event, context):
    name = event.get('name', '')  # Extracting 'name' parameter from event

    # Initial system message to set the role of the assistant
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": user_role},
    ]
    assistant_role = f'Hello, I am James Bond, an AI calling from XYZ Bank. Am I talking to {name}?'
    messages.append({"role": "assistant", "content": assistant_role})
    user_response = event.get('user_input', '')  # Extracting 'user_input' parameter from event
    messages.append({"role": "user", "content": user_response})
    assistant_response = chat_with_openai(messages)

    # Assistant asks the user for their name and residence
    while 'bye' not in assistant_response.lower():
        messages.append({"role": "assistant", "content": assistant_response})
        user_response = event.get('user_input', '')  # Extracting 'user_input' parameter from event
        messages.append({"role": "user", "content": user_response})
        assistant_response = chat_with_openai(messages)

    return assistant_response  # Returning response as the output of the Lambda function
