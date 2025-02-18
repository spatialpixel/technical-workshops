# Semantic image segmentation with Hugging Face

from transformers import pipeline
from PIL import Image
import requests

HF_TOKEN = ""

# Request an image from a URL.
url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/segmentation_input.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg/1024px-Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg/1024px-St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg"

image_data = requests.get(url, stream=True)
image = Image.open(image_data.raw)

# Or reference an image locally.
# image = Image.open('street.jpg')

# An example using a segmentic image segmentation model trained on the CityScapes dataset.
# This models is tuned on object classes commonly found in photographs of urban streets.
# 
# SegFormer paper: [SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203)
# Model card: https://huggingface.co/nvidia/segformer-b1-finetuned-cityscapes-1024-1024
# CityScapes dataset: https://www.cityscapes-dataset.com/dataset-overview/
semantic_model = "nvidia/segformer-b1-finetuned-cityscapes-1024-1024"  # ≈109.6MB

segmenter = pipeline("image-segmentation", model=semantic_model, token=HF_TOKEN)
results = segmenter(image)

if results is not None:
    for result in results:
        label = result['label']
        
        print(f"Saving result: {label}")
        result['mask'].save(f"semantic-seg-{label}.png")
else:
    print("Hmm, no segmentation results found.")
