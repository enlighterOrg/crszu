#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os

from crszu import cr
from crszu.rmnoise import count_neighbors

_DIR = os.path.dirname(os.path.abspath(__file__))
img = cr.preprocess(_DIR + "/images/captcha/gencheckcode.png")
w, h = img.size
data = img.load()


def test_count_neighbors():
    """Test count neighbors method"""
    assert count_neighbors(data, w, h, 35, 23, size=3) == 2
    assert count_neighbors(data, w, h, 35, 23, size=5) == 6
    assert count_neighbors(data, w, h, 75, 20, size=3) == 3
    assert count_neighbors(data, w, h, 75, 20, size=5) == 8
