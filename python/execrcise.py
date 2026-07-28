import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Function to get a response from GPT-3
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" or another model name as needed
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Example usage
user_prompt = "What are the benefits of using AI in healthcare?"
response = chat_with_gpt(user_prompt)
print(response)
