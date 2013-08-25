# crszu

[![Build Status](https://secure.travis-ci.org/marknv/crszu.png)](http://travis-ci.org/marknv/crszu)

Captcha Recognition for Shenzhen University Authentication (https://auth.szu.edu.cn/cas.aspx).

Recognition rate is above 80%. Simple, easy and fast!

## How to use?

```python
from crszu import cr

img = "crszu/images/captcha/gencheckcode.png"
captcha = cr.captcha_regonize(img)

print captcha

#8jh9
```
