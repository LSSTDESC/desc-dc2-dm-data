"""
butler.py
convenient function to get the butler of a specific run
"""

from lsst.daf.persistence import Butler
from .repos import REPOS
from . import fix_stack
del fix_stack

__all__ = ['get_butler']

def get_butler(run):
    """
    A convenient function to get the butler of a specific run.

    Parameters
    ----------
    run : str
        run name (e.g. "1.1p")

    Returns
    -------
    butler : lsst.daf.persistence.Butler instance

    """
    if run not in REPOS:
        raise KeyError('Run {} is not available'.format(run))
    return Butler(REPOS[run])
