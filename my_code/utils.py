import math
import numpy as np
import matplotlib.pyplot as plt

def plot_images(images, layout='square', layout_size=(), figsize=(16, 16), filename=None):
    h, w, c = images.shape[1:]
    
    if layout == 'square':
        hgrid_size = wgrid_size = math.ceil(np.sqrt(images.shape[0]))
    elif layout == 'rectangle':
        hgrid_size = layout_size[0]
        wgrid_size = layout_size[1]

    images = (images + 1) / 2. * 255.
    images = images.astype(np.uint8)
    images = (images.reshape(hgrid_size, wgrid_size, h, w, c)
              .transpose(0, 2, 1, 3, 4)
              .reshape(hgrid_size*h, wgrid_size*w, c))
    
    plt.figure(figsize=figsize)
    if filename != None:
        plt.imsave(filename, images)
    plt.imshow(images)
    plt.show()