# pydiff 

Myers diff of two lists or files
---------------------------------

Inspired by
https://gist.github.com/adamnew123456/37923cf53f51d6b9af32a539cdfa7cc4

API
===

``myers.diff(a, b, context=None, format=None)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(`myers.py, 25-60 <https://github.com/rec/myers/blob/master/myers.py#L25-L60>`_)

Return the Myers diff of two lists.

The result is a list of (action, line) pairs,
where ``action`` is one of ``KEEP``, ``INSERT``, ``REMOVE``, or ``OMIT``
(which happen to be the characters k, i, r, and o).

ARGUMENTS:
   ``a``, ``b``:
     The two files to compare

   ``context``:
     How many lines of context to keep between blocks of changes?
     ``None``, the default, means keep all unchanged lines.
     ``0`` means throw away all the unchanged lines.

   ``format``:
     If a dictionary, it is used to format
     each diff entry.  If true, the default dictionary above is
     used to format the diff entries.  Otherwise they are returned as-is.

(automatically generated by `doks <https://github.com/rec/doks/>`_ on 2020-11-07T12:19:33.047064)


Installation 
`python3 -m pip install -e src`