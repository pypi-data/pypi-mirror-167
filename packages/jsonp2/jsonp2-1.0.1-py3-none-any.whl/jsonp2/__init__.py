# -*- coding:utf-8 -*-
import json
import re
from json import JSONDecodeError
r"""JSON (JavaScript Object Notation) <http://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import jsonp2
    >>> jsonp2.tojson('Query1122012033111883315373_1662703989030({"a":1,"b":2}'))
    '{"a":1,"b":2}'

"""
__version__ = '0.0.1'
__all__ = [
    'tojson'
]

__author__ = 'spider_jiang <1243754883@qq.com>'

def tojson(obj):
    pattern = re.compile(r'.*?\((.*)\)$')
    match_info = pattern.match(obj)
    if match_info:
        try:
            retsult = json.loads(match_info.group(1))
        except Exception as err:
            raise JSONDecodeError("not JSON format",obj,1)
        else:
            return retsult
    else:
        raise ValueError(
            "no match content")
