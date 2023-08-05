"""The HAMSTER"""
import sys
from hamsay import hamster, pervert, halp, sebi  # damn pylint

__version__ = "0.1.1"


def main():
    """The main issue"""

    if len(sys.argv) == 1:
        hamster("EL ABURRIDO DEL PUEBLO")
        sys.exit()
    elif "--version" in sys.argv[1:]:
        print(__version__)
        sys.exit()
    elif "--help" in sys.argv[1:]:
        print(halp())
        sys.exit()
    elif "--sebi" in sys.argv[1:]:
        print(sebi())
        sys.exit()
    elif "--pervert" in sys.argv[1:]:
        pervert(sys.argv[2:])
        sys.exit()
    elif "--hamster" in sys.argv[1:]:
        hamster(sys.argv[2:])
        sys.exit()
    else:
        hamster(sys.argv[1:])
        sys.exit()


if __name__ == "__main__":
    main()
