import nvjpeg
import numpy as np
from time import time
import os
from typing import *
import pathlib
from matplotlib import cm as matplotlib_color_map
from utils import *

from bokeh.layouts import column
from bokeh.models import Slider
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.mappers import LogColorMapper
from nvjpeg import NvJpeg
import cv2
from matplotlib import pyplot as plt


memmap_path = '/home/kushal/meso-data/020ee829-b1ea-4a25-bb2f-ba9625cb8915-m1_els__d1_512_d2_512_d3_1_order_F_frames_11200_.mmap'
Yr, dims, T = load_memmap(memmap_path)
images = np.reshape(Yr.T, [T] + list(dims), order='F')

max_img_val = 9300 # approximate max value in the image, upper limit of cmap
lut = np.zeros(shape=((max_img_val), 1, 3), dtype=np.uint8)
cmap = np.vstack(auto_colormap(n_colors=(max_img_val), cmap='gnuplot2'))
lut[:, 0, :] = cmap[:, :-1] * 255

nj = NvJpeg()

def to_jpeg(img, quality=50):
    img = img - 2000 # lower limit of the cmap
    j_img = nj.encode(lut[img.astype(int)][:, :, 0, :], quality)
    # return nj.decode(j0)
    return cv2.cvtColor(nj.decode(j_img), cv2.COLOR_BGR2BGRA)


p = figure(plot_height=512, plot_width=512)#, output_backend='webgl')
p.grid.grid_line_width = 0

j = to_jpeg(images[0])
j = j.view(dtype=np.uint32).reshape((512, 512))

g = p.image_rgba([j], x=0, y=0, dw=10, dh=10, level="image")

def update(attr, old, val):
    frame = to_jpeg(images[val])
    frame = frame.view(dtype=np.uint32).reshape((512, 512))
    g.data_source.data['image'] = [frame]

s = Slider(start=0, end=11000, value=1, step=10, title="Frame index:")
s.on_change('value', update)
    
curdoc().add_root(column(p, s))
