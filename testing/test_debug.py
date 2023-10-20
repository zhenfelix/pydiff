from __future__ import print_function
from tempfile import NamedTemporaryFile
from unittest import TestCase
import functools
import myers

diff = functools.partial(myers.diff, format=True)

diff('abce','bcde')

class Record:    
    def __init__(self, entry = None) -> None:
        self.entry = entry 
        self.pre = None
    def goback(self) -> []:
        return [self.entry]+(self.pre.goback() if self.pre else [])
a = Record('a')
b = Record('b')
b.pre = a 
print(b.goback())