import imageio.v2 as iio

def ft_load(path: str):
    try:
        img = iio.imread(path)
        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        return print(e)


# print(ft_load("landscape.jpg"))