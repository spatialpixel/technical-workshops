# Text generation with the HuggingFace Inference API + Client
# 2025 02 05
# Set the HF_TOKEN variable with your Hugging Face access token.
#
# Example of setting token limits for limiting API consumption.

HF_TOKEN = ""

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=HF_TOKEN)

output = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        { "role": "user", "content": "What is space?" }
    ],
    max_tokens=200
)

print(output.choices[0].message.content)
