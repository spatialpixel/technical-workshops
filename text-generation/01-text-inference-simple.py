# Text generation with the HuggingFace Inference API + Client
# 2025 02 05

HF_TOKEN = ""

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=HF_TOKEN)

output = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        { "role": "user", "content": "What is space?" }
    ]
)

print(output.choices[0].message.content)
