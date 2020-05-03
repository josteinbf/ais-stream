import json
import sys
import argparse
import socket
from contextlib import nullcontext, contextmanager

import ais.stream


def nmea_to_json(stream_in, stream_out, *, num_messages=None):
    i = 0
    for i, msg in enumerate(ais.stream.decode(stream_in)):
        if num_messages is not None and i >= num_messages:
            break
        stream_out.write(json.dumps(msg) + '\n')


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description='Convert AIS messages in NMEA format to JSON',
    )
    parser.add_argument(
        '--num-messages', '-n', default=None, type=int,
        help='number of messages to convert (default: infinite)',
    )
    parser.add_argument(
        '--socket', '-s', type=str, default=None,
        help='read input from socket at host:port',
    )
    args = parser.parse_args(argv[1:])

    if args.socket is not None:
        host, port_str = args.socket.split(':')
        address = (host, int(port_str))

        @contextmanager
        def stream_in_ctxmgr():
            conn = socket.create_connection(address)
            yield conn.makefile(mode='r', encoding='ascii')
            conn.close()

        stream_in_ctx = stream_in_ctxmgr()

    else:
        stream_in_ctx = nullcontext(sys.stdin)

    with stream_in_ctx as stream_in:
        nmea_to_json(stream_in, sys.stdout, num_messages=args.num_messages)


if __name__ == '__main__':
    sys.exit(main())
