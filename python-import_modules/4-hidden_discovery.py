#!/usr/bin/python3

import importlib.util

def main():
    # Load the compiled .pyc file
    file_path = "./hidden_4.pyc"
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get the names defined in the module and filter out those starting with '__'
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the names and print them one per line
    for name in sorted(filtered_names):
        print(name)

if __name__ == "__main__":
    main()
