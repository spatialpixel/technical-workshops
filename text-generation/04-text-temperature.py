# Text generation with the HuggingFace Inference API + Client
# 2025 02 12
# Set the HF_TOKEN variable with your Hugging Face access token.
#
# Set the temperature for influencing the token selection, loosely related to
# an AI-based notion of "creativity" or "originality."

HF_TOKEN = ""

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=HF_TOKEN)

output = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        { "role": "user", "content": "What is space?" }
    ],
    max_tokens=300,
    temperature=0.8 # try 0.0, then 2.0, then numbers inbetween.
)

print(output.choices[0].message.content)
