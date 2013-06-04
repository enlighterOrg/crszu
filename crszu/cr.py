#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Image, ImageOps
from rmnoise import rmnoise
from edge_detection import find_edges
from match import match
import os

def captcha_regonize(im):
    captcha = ""
    im = Image.open(im)
    gray = ImageOps.grayscale(im)
    biim = gray.point(lambda i : i< 230 and 1 or 255)
    img = rmnoise(biim)
    edges = find_edges(img)
    for e in edges:
        xim = img.crop(e)
        of = "images/crops/char" + str(edges.index(e)) + ".png"
        xim.save(of)
    for n in range(len(os.listdir("images/crops"))):
        char = match("images/crops/char"+ str(n) + ".png")
        captcha += str(char)
    return captcha

if __name__ == "__main__":
    image = "images/captcha/gencheckcode.png"
    print captcha_regonize(image)
