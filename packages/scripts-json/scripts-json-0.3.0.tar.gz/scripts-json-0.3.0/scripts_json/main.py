import json
import os
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Run scripts from a scripts.json file!"
    )
    parser.add_argument(
        "script", help="The name of the script (default: start)", default="start"
    )
    parser.add_argument(
        "--file",
        help="The scripts.json file (default: scripts.json)",
        default="scripts.json",
    )
    args = parser.parse_args()

    try:
        with open(args.file) as file:
            scripts = json.load(file)
    except:
        print("Could not open file: '{args.file}'".format(args=args))
        exit(1)

    if not hasattr(scripts, args.script):
        all_scripts = "\n".join(scripts.keys())
        print(
            "Script '{args.script}' not found out of: {all_scripts}".format(
                args=args, all_scripts=all_scripts
            )
        )
        exit(1)

    os.system(str(scripts.get(args.script)))


if __name__ == "__main__":
    main()
