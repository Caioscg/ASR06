# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.3

from __future__ import annotations
import IcePy

from Ice.UserException import UserException

from dataclasses import dataclass


@dataclass
class DivisionByZero(UserException):
    """
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::Demo::DivisionByZero``.
    """
    reason: str = ""

    _ice_id = "::Demo::DivisionByZero"

_Demo_DivisionByZero_t = IcePy.defineException(
    "::Demo::DivisionByZero",
    DivisionByZero,
    (),
    None,
    (("reason", (), IcePy._t_string, False, 0),))

setattr(DivisionByZero, '_ice_type', _Demo_DivisionByZero_t)

__all__ = ["DivisionByZero", "_Demo_DivisionByZero_t"]
