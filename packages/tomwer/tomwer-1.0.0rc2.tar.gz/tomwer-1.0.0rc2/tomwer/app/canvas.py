import sys
from tomwer.app.canvas_launcher.mainwindow import OMain as QMain
from tomwer.core.utils.resource import increase_max_number_file
import tomwer.version
import tomoscan.version

try:
    import nxtomomill.version
except ImportError:
    has_nxtomomill = False
else:
    has_nxtomomill = True
try:
    import nabu
except ImportError:
    has_nabu = False
else:
    has_nabu = True


def print_versions():
    print(f"tomwer version is {tomwer.version.version}")
    print(f"tomoscan version is {tomoscan.version.version}")
    if has_nxtomomill:
        print(f"nxtomomill version is {nxtomomill.version.version}")
    if has_nabu:
        print(f"nabu version is {nabu.version}")


def main(argv=None):
    print_versions()
    increase_max_number_file()
    return QMain().run(argv)


if __name__ == "__main__":
    sys.exit(main())
