#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Image, ImageOps
from rmnoise import rmnoise
from edge_detection import find_edges

if __name__ == "__main__":
    im = Image.open("images/captcha/gencheckcode3.png")
    gray = ImageOps.grayscale(im)
    biim = gray.point(lambda i : i< 200 and 1 or 255)
    img = rmnoise(biim)
    edges = find_edges(img)
    i = 1
    for e in edges:
        xim = img.crop(e)
        of = "images/crops/char" + str(i)
        i += 1
        xim.save(of+".png","PNG")
