from kapitan.inputs.kadet import load_from_search_paths

base = load_from_search_paths("base")

class Bar(base.Foo):
    def new(self):
        self.need("name", "name string needed")

    def body(self):
        self.root.spec.metadata.name = self.kwargs.name