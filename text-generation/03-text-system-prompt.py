# Text generation with the HuggingFace Inference API + Client
# 2025 02 12
# Set the HF_TOKEN variable with your Hugging Face access token.
#
# Example for providing a system context / prompt for added control over inference.

HF_TOKEN = ""

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=HF_TOKEN)

output = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        { "role": "system", "content": "Always speak in rhymes" },
        { "role": "user", "content": "What is space?" }
    ],
    max_tokens=300
)

print(output.choices[0].message.content)
