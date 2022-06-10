# from kapitan.inputs.kadet import BaseObj
import sys
sys.path.append("..")
from ..base.foo import Foo

class Baz(Foo):
    def new(self):
        self.need("name", "name string needed")

    def body(self):
        self.root.spec.metadata.name = self.kwargs.name