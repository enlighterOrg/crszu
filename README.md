# crszu

Capthca Regonization for SZU Authentication (https://auth.szu.edu.cn/cas.aspx).

Recognition rate is above 80%.

## How to use?

```python
from crszu import cr

img = "crszu/images/captcha/gencheckcode.png"
captcha = cr.captcha_regonize(img)
print captcha

#8jh9
```
