# Computer Vision with Hugging Face

These examples use Hugging Face's `transformers` framework to run various
vision models, such as depth estimation, image segmentation, etc.


## Prerequisites

Like all the Hugging Face tutorials, you'll need an access token for the Hugging Face API.

Follow the Python install in the root-level README file. Enable the virtual environment.


## Sources for Images

While any public URL for an image will likely work for these examples, here are a
few free sources that may work well for testing:

- https://cocodataset.org/#explore
- https://huggingface.co/datasets/huggingface/documentation-images
- https://commons.wikimedia.org/wiki/Main_Page


## Depth Estimation

Depth estimation takes an image as input and produces another image, each pixel 
of which represents an estimation of the distance from the original image's 
"camera" to that pixel in space.

References from the Hugging Face docs:

- https://huggingface.co/tasks/depth-estimation
- https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation

