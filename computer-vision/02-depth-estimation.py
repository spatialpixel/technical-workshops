# Depth Estimation with Hugging Face

# Provide your HF access token in the HF_TOKEN variable.
# 
# Several sample images are provided by default. Just provide the image you want to check
# in the estimator() constructor below. Any public URL to any image can be used.
#
# Similarly, there are several models already coded below with the variables model1, model2, etc.
# model1 is specified by default.
# 
# Note that when you run this script, it will download the model to your machine,
# which can be many GB.
#
# The result is a PNG image saved to disk, the name of which is specified in the .save() method.


from transformers import pipeline

HF_TOKEN = ""

# Some sample images
cats = "http://images.cocodataset.org/val2017/000000039769.jpg"
bee_flower = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"
theater = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Tianjin_Grand_Theater_Concert_Hall.jpg/1024px-Tianjin_Grand_Theater_Concert_Hall.jpg"

# Models that seem to work well
model1 = "depth-anything/Depth-Anything-V2-base-hf"   # ≈390MB
model2 = "depth-anything/Depth-Anything-V2-Large-hf"  # ≈1.34GB
model3 = "Intel/dpt-large"    # ≈2.74GB

estimator = pipeline(task="depth-estimation", model=model1, token=HF_TOKEN)
result = estimator(images=theater)
result["depth"].save("depth-theater.png")
