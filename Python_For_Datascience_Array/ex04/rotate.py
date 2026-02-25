from load_image import ft_zoom
import matplotlib.pyplot as plt
import numpy as np


def ft_transpose(img):
    rows, cols = len(img), len(img[0])
    new_img = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_img[j][i] = img[i][j]
    new_img = np.array(new_img)
    reformed_img = []
    for i in range(len(new_img)):
        reformed_img.append(new_img[i].flatten())
    return np.array(reformed_img)


def rotate(path: str):
    try:
        START_X = 100
        START_Y = 450
        WIDTH = 400
        HEIGHT = 400
        NB_CHANNELS = 1
        PIXEL_CONTENT = "grey"
        img = ft_zoom(path, START_X, START_Y, WIDTH,
                      HEIGHT, NB_CHANNELS, PIXEL_CONTENT)

        new_img = ft_transpose(img)
        print(f"New shape after Transpose: {new_img.shape}")
        print(new_img)
        plt.figure()
        plt.imshow(new_img, cmap=PIXEL_CONTENT)
        plt.show()
    except Exception as e:
        return print(e)


if __name__ == '__main__':
    rotate("animal.jpeg")
