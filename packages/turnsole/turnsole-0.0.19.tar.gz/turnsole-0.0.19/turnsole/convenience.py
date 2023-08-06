import cv2
import numpy as np

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

def resize_with_pad(image, target_width, target_height):
    """Resuzes and pads an image to a target width and height.

    Resizes an image to a target width and height by keeping the aspect ratio the same 
    without distortion. 
    ratio must be less than 1.0.
    width and height will pad with zeroes.

    Args:
        image (Array): RGB/BGR
        target_width (Int): Target width.
        target_height (Int): Target height.

    Returns:
        Array: Resized and padded image. The image paded with zeroes.
        Float: Image resized ratio. The ratio must be less than 1.0.
    """
    height, width, _ = image.shape

    min_ratio = min(target_height/height, target_width/width)
    ratio = min_ratio if min_ratio < 1.0 else 1.0

    # To shrink an image, it will generally look best with INTER_AREA interpolation.
    resized = cv2.resize(image, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
    h, w, _ = resized.shape
    canvas = np.zeros((target_height, target_width, 3), image.dtype)
    canvas[:h, :w, :] = resized
    return canvas, ratio
