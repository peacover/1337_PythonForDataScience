import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def ft_load(path: str):
    try:
        img = mpimg.imread(path)
        # plt.figure()
        # plt.imshow(img)
        # plt.show()

        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        return print(e)