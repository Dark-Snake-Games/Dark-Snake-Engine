__version__ = "0.0.1-alpha"
__license__ = "MIT"

import contextlib

with contextlib.redirect_stdout(None):
  import sys
  import pygame as pg
  from .etypes import *
  from .animated import *
  from .gui import *
  from .saving import *
  from .tiles import *
  from .scenes import *
  from .camera import *

pg.init()

print(
  f"Dark Snake Engine {__version__}",
  f"python {sys.version.split()[0]}  pygame-ce {pg.version.ver}",
  f"© 2023 Dark Snake Games, GitHub contributors,",
  f"licensed under {__license__}",
  sep="\n",
  end="\n\n"
)
print("*** DEBUG INFORMATION ***")