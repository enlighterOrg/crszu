#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

import nose.tools

from crszu import rmnoise, cr
from crszu.errors import InvalidSizeError, SizeTypeError

_DIR = os.path.dirname(os.path.abspath(__file__))
img = cr.preprocess(_DIR + "/images/captcha/gencheckcode.png")


@nose.tools.raises(InvalidSizeError)
def test_invalid_size_error():
    """Test size invalid exception."""
    rmnoise.rmnoise(img, size=-1)
    rmnoise.rmnoise(img, size=0)
    rmnoise.rmnoise(img, size=2)
    rmnoise.rmnoise(img, size=200)


@nose.tools.raises(SizeTypeError)
def test_size_type_error():
    """Test size type error exception."""
    rmnoise.rmnoise(img, size=6.27)
    rmnoise.rmnoise(img, size="omg")
    rmnoise.rmnoise(img, size=[1, 2, 3])
    rmnoise.rmnoise(img, size=(1, 2, 3))
    rmnoise.rmnoise(img, size={1: 'a', 2: 'b', 3: 'c'})
    rmnoise.rmnoise(img, size=None)
