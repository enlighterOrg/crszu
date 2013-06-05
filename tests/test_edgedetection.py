#!/usr/bin/env python
#-*- coding:utf-8 -*-

from crszu import cr
from crszu.edge_detection import find_edges

img = cr.rmnoise(cr.preprocess("tests/images/captcha/gencheckcode.png"))

def test_find_edges():
    """Test find edges method"""
    assert find_edges(img) == [(25, 9, 35, 29), (42, 11, 49, 36), (64, 11, 78,
        30), (85, 13, 98, 32)]
