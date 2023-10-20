from __future__ import print_function
from tempfile import NamedTemporaryFile
from unittest import TestCase
import functools
import myers

diff = functools.partial(myers.diff, format=True)

diff('abce','bcde')