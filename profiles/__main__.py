import sys

if sys.version_info < (3, 9):
    print("REJECTED: Persona Generator requires Python 3.9 or newer", file=sys.stderr)
    raise SystemExit(2)

from .compiler import main
raise SystemExit(main())
