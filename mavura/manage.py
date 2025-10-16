#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import importlib
import os
import sys

settings_module = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mavura.settings")

try:
    settings_module_lib = importlib.import_module(settings_module)

except ImportError as IE:
    raise ImportError("Cannot import the setting module") from IE

BASE_DIR = getattr(settings_module_lib, "BASE_DIR")

PID_FILE = os.path.join(BASE_DIR, "server.pid")


def main():
    """Run administrative tasks."""

    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
