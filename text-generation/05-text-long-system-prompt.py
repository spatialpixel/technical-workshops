# Text generation with the HuggingFace Inference API + Client
# 2025 02 12
# Set the HF_TOKEN variable with your Hugging Face access token.
# 
# This example uses a text file, "system-example.txt", to contain a longer
# system prompt for this chat. To use this script, do the following:
#
# 1. Add your Access Token in the HF_TOKEN variable, between the quotes.
# 2. Edit system-example.txt with your system context and save it.
# 3. Edit the "user_prompt" variable below with your prompt, between the triple quotes.
# 4. Run this file.

HF_TOKEN = ""

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=HF_TOKEN)

with open('system-example.txt', 'r') as file:
    system_prompt = file.read()

user_prompt = """
What is space?
"""

output = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": user_prompt }
    ],
    max_tokens=300,
    temperature=1.0
)

print(output.choices[0].message.content)
