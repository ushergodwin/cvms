#!/usr/bin/env python
"""Administrative user account command line utility"""


def main():
    try:
        from covidvms.user import run_cl
        run_cl(True)
    except ImportError:
        raise ImportError("Failed to import the user module. Make sure that the module exits")


if __name__ == '__main__':
    main()
