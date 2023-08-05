from .ed25519_dalek import *

__doc__ = ed25519_dalek.__doc__
if hasattr(ed25519_dalek, "__all__"):
    __all__ = ed25519_dalek.__all__