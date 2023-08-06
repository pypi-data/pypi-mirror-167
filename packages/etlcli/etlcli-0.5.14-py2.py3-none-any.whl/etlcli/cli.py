import argparse
import json

from etlcli.extractor import Extractor

def extract():
    print("extract")


def transform():
    print("transform")


def load():
    print("load")


def cli():
    parser = argparse.ArgumentParser(description='Process input arguments')
    parser.add_argument("operation")
    parser.add_argument("--database")
    parser.add_argument("--sql")
    parser.add_argument("--params", type=json.loads)
    parser.add_argument("--target")
    parser.add_argument("--input")
    args = vars(parser.parse_args())

    if args["operation"] == "extract":
        extractor = Extractor(args["database"])
        extractor.execute_query(args["sql"], args["params"])
        extractor.save_to_csv(args["target"])
        extractor.close_conn()
    elif args["operation"] == "transform":
        transform()
    elif args["operation"] == "load":
        load()
    else:
        print("Wrong argument! Supported args: extract | transform | load")



if __name__ == "__main__":
    cli()