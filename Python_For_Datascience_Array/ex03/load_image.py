import matplotlib.image as mpimg


def ft_load(path: str):
    """Load an image from the given path and print its shape.

    Returns the image as a numpy array, or None on error.
    """
    try:
        img = mpimg.imread(path)

        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        return print(e)
