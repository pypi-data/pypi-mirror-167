import argparse
import json

from etlcli.extractor import Extractor
from etlcli.loader import Loader
from etlcli.transformer import Transformer


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
    elif args["operation"] == "load":
        loader = Loader(args["database"])
        loader.load_data(args["input"], args["target"])
        loader.close_conn()
    elif args["operation"] == "transform":
        transformer = Transformer(args["database"])
        transformer.transform_data(args["sql"],
                                   args["params"],
                                   args["target"])
    else:
        print("Wrong argument! Supported args: extract | transform | load")


if __name__ == "__main__":
    cli()