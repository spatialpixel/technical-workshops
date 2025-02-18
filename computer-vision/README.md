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


## Image Segmentation

Image segmentation takes an image and produces one or more images that represent
the probabilities that pixels in the original image represent one or more classes.
It has applications in medical imaging, autonomous vehicle navigation, and others.

- https://huggingface.co/tasks/image-segmentation
- https://huggingface.co/docs/transformers/tasks/semantic_segmentation

There are three types of image segmentation noted here:

1. **Semantic segmentation** → For each pixel in an image, return the probabilities 
that it represents a particular class.
2. **Instance segmentation** → Isolate individual objects in a given image.
3. **Panoptic segmentation** → Segment by instance and object class.

There are a number of models available for image segmentation on Hugging Face,
found here:

- https://huggingface.co/models?pipeline_tag=image-segmentation

The code for the image segmentation examples are nearly identical, since the
selected _model_ determines the type of image segmentation performed as well
as the _classes_ of objects segmented.

For example, in the file `03-image-seg-semantic-urban.py`, the provided model
is a "SegFormer" _semantic segmentation_ model trained on the "CityScapes" dataset.

- https://huggingface.co/models?other=segformer
