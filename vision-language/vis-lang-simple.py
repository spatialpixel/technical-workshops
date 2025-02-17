# Simple vision-language completion using the Hugging Face inference API and client.
# 2025 02 11


from huggingface_hub import InferenceClient

HF_TOKEN = ""

client = InferenceClient(api_key=HF_TOKEN)

# Model card: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct
model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
bee_flower = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"

output = client.chat_completion(
    model=model,
    messages=[
        { "role": "user", 
          "content": [
            {   "type": "image_url",
                "image_url": {
                    "url": bee_flower,  # URL to the image
                    "detail": "low"
                }
            },
            {   "type": "text",
                "text": "Can you describe this image?"  # Text prompt
            }]
        }
    ],
    max_tokens=300
)

print(output.choices[0].message.content)
