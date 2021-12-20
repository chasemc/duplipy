import logging

# If {rich} is installed use it, otherwise.... don't
try:
    from rich.logging import RichHandler

    # https://rich.readthedocs.io/en/stable/logging.html
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    log = logging.getLogger("rich")

except ImportError as e:
    log = logging.getLogger()


# https://blog.hay-kot.dev/fastapi-and-rich-tracebacks-in-development/
# https://coralogix.com/blog/python-logging-best-practices-tips/
