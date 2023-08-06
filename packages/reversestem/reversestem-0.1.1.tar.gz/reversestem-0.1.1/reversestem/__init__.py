from .svc import *
from .dmo import *
from .dto import *

from reversestem.svc import StemFinder

finder = StemFinder()


def unstem(input_text: str, flatten: bool = False) -> dict or list or None:
    return finder.unstem(input_text=input_text, flatten=flatten)
