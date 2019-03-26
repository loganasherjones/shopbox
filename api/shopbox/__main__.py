# -*- coding: utf-8 -*-
import logging
import signal
import shopbox


def signal_handler(signum, stack_frame):
    logging.getLogger(__name__).info("Received a shutdown request")
    shopbox.stop()


def load_config():
    return {
        "log": {"level": "INFO"},
        "web": {"host": "127.0.0.1", "port": 7467, "debug": False},
    }


def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    config = load_config()
    shopbox.setup_logging(config)
    shopbox.setup_app(config)
    shopbox.run(config)


if __name__ == "__main__":
    main()
