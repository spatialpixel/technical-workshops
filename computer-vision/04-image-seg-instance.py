# Semantic image segmentation with Hugging Face

from transformers import pipeline
from PIL import Image
import requests

HF_TOKEN = ""

# Request an image from a URL.
# url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/segmentation_input.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg/1024px-Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg"
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg/1024px-St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg"

image_data = requests.get(url, stream=True)
image = Image.open(image_data.raw)

# Or reference an image locally.
# image = Image.open('street.jpg')

# https://huggingface.co/facebook/mask2former-swin-large-cityscapes-instance
instance_model = "facebook/mask2former-swin-large-cityscapes-instance"  # ≈866MB

segmenter = pipeline("image-segmentation", model=instance_model, token=HF_TOKEN)
results = segmenter(image)

if results is not None:
    # Keep count of the number of instances of each class so we can save them each to disk.
    result_counts = {}
    
    for result in results:
        label = result['label']
        score = result['score']
        
        if label in result_counts:
            result_counts[label] += 1
        else:
            result_counts[label] = 1
        result_count = result_counts[label]
        
        print(f"Saving result: {label} number {result_count}, score {score}")
        result['mask'].save(f"instance-seg-{label}-{result_count}.png")
else:
    print("Hmm, no segmentation results found.")
