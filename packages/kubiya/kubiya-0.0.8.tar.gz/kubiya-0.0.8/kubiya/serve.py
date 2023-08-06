from kubiya import action_store
from kubiya.http import serve, discover
from kubiya.loader import load_action_store
from sys import argv, exit
from os import environ

def serve_all(filename=None):
    instances = action_store.ActionStore._instances
    if not instances:
        print("No stores found")
        exit(1)
    if len(instances) > 1:
        print("Multiple stores found: {instances}")
        exit(1)
    serve(instances[0], filename)


def discover_all(filename=None):
    instances = action_store.ActionStore._instances
    if not instances:
        print("No stores found")
        exit(1)
    if len(instances) > 1:
        print("Multiple stores found: {instances}")
        exit(1)
    discover(instances[0], filename)

if __name__ == "__main__":    
    if len(argv) != 2:
        print("Usage: python3 -m kubiya.serve <action_store_file.py>")
        exit(1)
    
    store_file = load_action_store(argv[1])
    if environ.get("KUBIYA_DISCOVER"):
        discover_all(store_file)
    else:
        serve_all(store_file)   
