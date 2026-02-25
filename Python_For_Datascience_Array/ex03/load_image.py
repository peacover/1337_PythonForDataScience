import matplotlib.image as mpimg


def ft_load(path: str):
    try:
        img = mpimg.imread(path)

        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        return print(e)
