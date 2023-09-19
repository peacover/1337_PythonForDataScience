import matplotlib.image as mpimg

def ft_load(path: str):
    try:
        img = mpimg.imread(path)
        return img
    except Exception as e:
        return print(e)

def ft_zoom(path: str,start_x: int, start_y: int, width: int, height: int, nb_channels: int, pixel_content: str):
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