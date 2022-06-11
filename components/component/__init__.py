from kapitan.inputs import kadet

kubelib = kadet.load_from_search_paths("kube")

def main():
    return {
        "component": kubelib.Bar(name="component_name")
    }