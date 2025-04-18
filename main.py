import sys

sys.dont_write_bytecode = True

import argparse
import os
import json
import traceback
import PackageViewer
import basic_view


parser = argparse.ArgumentParser(description="Whistle of Wind command line")
parser.add_argument("conf", type=str, nargs="?", help="Path to the configuration file")

args = parser.parse_args()

config_file = "config.json"
if args.conf:
    if os.path.isfile(args.conf):
        config_file = args.conf
    else:
        basic_view.show_message(
            "Whistle of Wind",
            f"Please, provide a valid configuration file {config_file}",
            icon=3,
        )
elif not os.path.isfile(config_file):
    basic_view.show_message(
        "Whistle of Wind",
        f"Please, provide a valid configuration file {config_file}",
        icon=3,
    )

if config_file:
    conf = []
    with open(config_file) as f:
        conf = json.load(f)

    try:
        startup_pack = "viewer"
        startup_pack_conf = conf["global"] if "global" in conf else None
        startup_pack = (
            startup_pack_conf["startup_package"]
            if "startup_package" in startup_pack_conf
            else startup_pack
        )
        pv = PackageViewer.PackageViewer(conf)
        startup_package = pv.instance().packages[startup_pack]
        startup_package.view()
    except:
        basic_view.show_message(
            "Whistle of Wind",
            f"""Oops! Unhandled error during execution:
{traceback.format_exc()}""",
            icon=3,
        )
