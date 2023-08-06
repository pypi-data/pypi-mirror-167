import argparse
import etlcli
import sys

def extract():
    print("extract")


def transform():
    print("transform")


def load():
    print("load")


def cli():
    parser = argparse.ArgumentParser(description='Process input arguments')
    parser.add_argument("operation")
    args = vars(parser.parse_args())
    if args["operation"] == "extract":
        extract()
    elif args["operation"] == "transform":
        transform()
    elif args["operation"] == "load":
        load()
    else:
        print("Wrong argument! Supported args: extract | transform | load")



if __name__ == "__main__":
    cli()