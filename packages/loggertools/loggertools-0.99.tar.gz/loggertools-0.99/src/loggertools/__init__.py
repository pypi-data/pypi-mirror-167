"""
loggertools is a Python port of the Control File Functions of the
Logger Tools Software of Olaf Kolle, MPI-BGC Jena, (c) 2012.

From the Logger Tools Software manual:
"The functions range from simple mathematic operations to more complex
and special procedures including functions for checking data. Most of
the functions have the following appearance: `a = f(b,p1,p2,...,pn)`
where `a` is the variable in which the result of the function `f` is
stored, `b` is the input variable of the function and `p1` to `pn` are
parameters (numbers) of the function. An output variable (result of a
function) may be the same as an input variable. Some functions need
more than one input variable, some functions do not need any parameter
and some functions (`mean`, `mini`, `maxi`) may have a variable number
of input variables."

:copyright: Copyright 2014-2022 Matthias Cuntz, see AUTHORS.rst for details.
:license: MIT License, see LICENSE for details.

Subpackages
===========
.. autosummary::
   loggertools

History
    * Written Jun-Oct 2014 by Matthias Cuntz (mc (at) macu (dot) de)
    * v1.0, initial Github, PyPI, Zenodo commit, Sep 2022, Matthias Cuntz

"""
# version, author
try:  # pragma: no cover
    from ._version import __version__
except ImportError:  # pragma: no cover
    # package is not installed
    __version__ = "0.0.0.dev0"
__author__  = "Matthias Cuntz, Olaf Kolle"

from .loggertools import *
