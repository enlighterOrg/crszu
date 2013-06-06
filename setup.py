from setuptools import setup

setup(
      name="crszu",
      packages=["crszu"],
      version="0.0.1",
      install_requires=["pillow"],
      description="captcha regonization for SZU authentication.",
      author="MarkNV",
      author_email="marknv@live.com",
      url="https://github.com/marknv/crszu",
      test_suite="nose.collector",
      tests_require=["nose"],
      include_package_data = True
)
