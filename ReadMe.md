ClassDictMeta.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[![GitLab Build Status](https://gitlab.com/KOLANICH/ClassDictMeta.py/badges/master/pipeline.svg)](https://gitlab.com/KOLANICH/ClassDictMeta.py/pipelines/master/latest)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/ClassDictMeta.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/ClassDictMeta.py.svg)](https://libraries.io/github/KOLANICH/ClassDictMeta.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Just a metaclass allowing you to create some dicts easier. Like

```python
class a(metaclass=ClassDictMeta):
	a = "b"
	c = 0xD
# equivalent to a = {"a": "b", "c": 0xD}
```
