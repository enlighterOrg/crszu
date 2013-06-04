#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Image, ImageOps
from rmnoise import rmnoise

if __name__ == "__main__":
    im = Image.open("images/captcha/gencheckcode.png")
    gray = ImageOps.grayscale(im)
    biim = gray.point(lambda i : i< 200 and 1 or 255)
    biim.show()
    rmnoise(biim)
    biim.show()
