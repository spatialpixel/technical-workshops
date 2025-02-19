# Basic object detection with Hugging Face

from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests

HF_TOKEN = ""

# Request an image from a URL.
url = "http://images.cocodataset.org/val2017/000000039769.jpg"  # cats on a couch
# url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/segmentation_input.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg/1024px-Kowloon_Waterfront%2C_Hong_Kong%2C_2013-08-09%2C_DD_05.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg/1024px-St_Andrew%27s_Street_-_geograph.org.uk_-_5553498.jpg"
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Slow_Life_in_A_Tea_House_01_edited.jpg/1024px-Slow_Life_in_A_Tea_House_01_edited.jpg"

image_data = requests.get(url, stream=True)
image = Image.open(image_data.raw)

# you can specify the revision tag if you don't want the timm dependency
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm", token=HF_TOKEN)
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm", token=HF_TOKEN)

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.9
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
        f"Detected {model.config.id2label[label.item()]} with confidence "
        f"{round(score.item(), 3)} at location {box}"
    )

# A successful output on the cats-on-a-couch image will look like this:
#
# Detected remote with confidence 0.998 at location [40.16, 70.81, 175.55, 117.98]
# Detected remote with confidence 0.996 at location [333.24, 72.55, 368.33, 187.66]
# Detected couch with confidence 0.995 at location [-0.02, 1.15, 639.73, 473.76]
# Detected cat with confidence 0.999 at location [13.24, 52.05, 314.02, 470.93]
# Detected cat with confidence 0.999 at location [345.4, 23.85, 640.37, 368.72]
#
# Note that you may have to press CTRL+C to cancel the script as it sometimes hangs.
