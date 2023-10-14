import typing
from collections import OrderedDict
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/ClassDictMeta.py, read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

class ClassDictMeta(type):
	cls = dict

	def __new__(cls: typing.Type["ClassDictMeta"], className: str, parents: tuple, attrs: typing.Dict[str, typing.Any], *args, **kwargs) -> dict:
		newAttrs = type(attrs)(attrs)
		return cls.cls((k, v) for k, v in newAttrs.items() if k[0] != "_")


class OrderedClassDictMeta(ClassDictMeta):
	cls = OrderedDict
