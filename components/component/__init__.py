from kapitan.inputs import kadet

kubelib = kadet.load_from_search_paths("kube")

def main():
    return {
        "component": kubelib.Baz(name="component_name")
    }