## The problem is loading the Foo from base "module"
from base.foo import Foo

class Bar(Foo):
    def new(self):
        self.need("name", "name string needed")

    def body(self):
        self.root.spec.metadata.name = self.kwargs.name