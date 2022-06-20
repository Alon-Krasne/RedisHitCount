import logging
import sys
import time
from flask import Flask
import redis

app = Flask(__name__)
rd = redis.Redis.from_url(url='redis://redis:6379/', db=0)
logger: logging.Logger


def configure_logger(name: str) -> logging.Logger:
    global logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


@app.route("/")
def hit_counter() -> str:
    start_time = time.perf_counter()
    hit_count = rd.incr("counter")
    logger.debug("Hit!, count is %s. Wow!!! Redis is ⚡ fast - the set / get method took %f seconds.",
                 hit_count, (time.perf_counter() - start_time))
    return f"<p>Hit count is {hit_count}</p>"


def main():
    global logger
    logger = configure_logger(__package__)

    try:
        logger.debug('Connected to redis, setting counter to 0')
        rd.set("counter", 0)
        logger.debug('Starting server')
        app.run(host='0.0.0.0', port=3000)
    except KeyboardInterrupt:
        logger.info('Shutting down')
        return 0
    except Exception:
        logger.exception('Unhandled exception')
        return 1


if __name__ == "__main__":
    exit(main())
