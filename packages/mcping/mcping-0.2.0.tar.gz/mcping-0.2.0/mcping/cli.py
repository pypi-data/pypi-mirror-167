"""The CLI for mcping"""
import argparse
import orjson

from . import __version__, status as mc_status
from .exceptions import MCPingException


def main():
    parser = argparse.ArgumentParser(
        prog="mcping",
        description="a cli to get minecraft server statuses",
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.add_argument(
        "ip",
        type=str,
        help=(
            "the ip address to ping. "
            "optionally include a port separated by a colon, eg. example.com:1234"
        ),
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=5,
        help="the time to wait for the server to respond",
    )

    parser.add_argument(
        "-r",
        "--raw",
        action="store_true",
        help="print raw json instead of a table. also applies for error messages",
    )

    parser.add_argument(
        "-i",
        "--ignore-key",
        action="append",
        nargs="*",
        help="specify a key to exclude from output",
    )

    args = parser.parse_args()

    if ":" in args.ip:
        ip, port = args.ip.split(":")
        port = int(port)
    else:
        ip = args.ip
        port = 25565

    try:
        status = mc_status(ip, port, args.timeout)
    except MCPingException as e:
        if args.raw:
            error = type(e).__name__
            reason = str(e)
            print(orjson.dumps({"error": error, "reason": reason}).decode())
            return
        else:
            raise e

    if args.ignore_key:
        # argparse decides to put each option in its own array, so flatten it
        args.ignore_key = list(map(lambda arr: arr[0], args.ignore_key))

        wanted_items = filter(
            lambda entry: entry[0] not in args.ignore_key, status.items()
        )
        status = {k: v for k, v in wanted_items}

    if args.raw:
        print(orjson.dumps(status).decode())
        return

    longest_key = max(len(k) for k in status)

    # Have to do this ugly stuff with f-strings and .format
    # so that longest_key can be used in the formatting specifier
    print(f"{{:<{longest_key}}} Value".format("Key"))
    for k, v in sorted(status.items()):
        print(f"{{:<{longest_key}}} {{}}".format(k, v))
