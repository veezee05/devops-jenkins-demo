"""Tiny application built and tested by Jenkins."""
import platform
from datetime import datetime


def add(a, b):
    return a + b


def greet(name):
    return f"Hello, {name}! Welcome to the DevOps demo."


if __name__ == "__main__":
    print(greet("Jenkins"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Built on {platform.node()} with Python {platform.python_version()}")
    print(f"Build time: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("Build successful!")
