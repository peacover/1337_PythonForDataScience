import matplotlib.image as mpimg


def ft_load(path: str):
    """Load an image from the given path.

    Returns the image as a numpy array, or None on error.
    """
    try:
        img = mpimg.imread(path)
        return img
    except Exception as e:
        return print(e)


def ft_zoom(path: str, start_x: int, start_y: int, width: int,
            height: int, nb_channels: int):
    """Zoom into a region of an image and return the cropped portion.

    Loads the image, slices the specified region based on coordinates
    and channel count, prints the shape, and returns the zoomed array.
    """
    try:
        img = ft_load(path)

        end_x = start_x + width
        end_y = start_y + height

        new_img = img[start_x:end_x, start_y:end_y, :nb_channels]
        str = f"The shape of image is: {new_img.shape}"
        if nb_channels == 1:
            str += f" or ({width}, {height})"
        print(str)
        print(new_img)
        return new_img
    except Exception as e:
        return print(e)
