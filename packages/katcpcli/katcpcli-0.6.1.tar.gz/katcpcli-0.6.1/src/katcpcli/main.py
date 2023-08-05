#!/usr/bin/python3
"""
KATCPcli - a text client for KATCP devices.
"""

import asyncio
import logging
import sys
import argparse

import katcpcli.app

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s - %(name)s - %(filename)s:"
    "%(lineno)s - %(levelname)s - %(message)s",
)

_log = logging.getLogger("katcpcli")

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 1235


async def async_main():
    """
    Run katcpcli program.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-a",
        "--host",
        help="Host Device to connect to. Updates device setting if both are given.",
    )
    parser.add_argument(
        "-p",
        "--port",
        help="Port to connect to. Updates device setting if both are given.",
    )
    parser.add_argument(
        "device",
        nargs="?",
        help="Device to connect to [ip:port]",
        default=f"{DEFAULT_HOST}:{DEFAULT_PORT}",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print debug output"
    )
    parser.add_argument("--nofs", action="store_true", help="Start as full screen app.")

    args = parser.parse_args()
    if args.verbose:
        _log.setLevel("DEBUG")

    if ":" in args.device:
        host, port = args.device.split(":")
    else:
        host = args.device
        port = DEFAULT_PORT

    if args.host:
        host = args.host
    if args.port:
        port = args.port

    dispatcher, app = katcpcli.app.create_app_and_dispatcher(args.nofs)
    asyncio.create_task(dispatcher.connect(host, port))

    await app.run_async()


def main():
    """
    Run asyncio main
    """
    print("Starting katcp CLI ... ")
    asyncio.run(async_main())
    print("Exiting katcp CLI ...")


if __name__ == "__main__":
    main()
