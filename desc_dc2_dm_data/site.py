"""
site.py
Extract site info.
"""

import os
import socket
import warnings

__all__ = ["SITE_INFO"]

# We utilize the same environment variable used in https://github.com/LSSTDESC/gcr-catalogs
_DESC_SITE_ENV = "DESC_GCR_SITE"


def get_site_info():
    """
    Return a string which, when executing at a recognized site with
    well-known name, will include the name for that site
    """
    site_from_env = os.getenv(_DESC_SITE_ENV, default="")
    site_from_socket = socket.getfqdn()
    if site_from_env:
        if site_from_socket and site_from_env not in site_from_socket and not (
            site_from_env == "nersc" and site_from_socket.startswith("nid")
        ):
            warnings.warn("Site determined from env variable {} = {}, which differs from node name {}".format(
                _DESC_SITE_ENV, site_from_env, site_from_socket
            ))
        return site_from_env
    return site_from_socket


SITE_INFO = get_site_info()
