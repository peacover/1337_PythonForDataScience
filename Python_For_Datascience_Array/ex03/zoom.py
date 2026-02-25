from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(path: str, start_x: int, start_y: int, width: int, height: int,
            nb_channels: int, pixel_content: str):
    try:
        img = ft_load(path)
        print(img)

        end_x = start_x + width
        end_y = start_y + height

        new_img = img[start_x:end_x, start_y:end_y, :nb_channels]
        str = f"The shape after slicing: {new_img.shape}"
        if nb_channels == 1:
            str += f" or ({width}, {height})"
        print(str)
        print(new_img)

        plt.figure()
        plt.imshow(new_img, cmap=pixel_content)
        plt.show()
    except Exception as e:
        return print(e)


if __name__ == "__main__":
    ft_zoom("animal.jpeg", 100, 450, 400, 400, 1, "gray")
