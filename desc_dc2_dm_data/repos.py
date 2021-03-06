"""
repos.py
paths to current repos
"""

import warnings
from .site import SITE_INFO

__all__ = ['REPOS']

# current available runs at NERSC and IN2P3
_REPOS = {
    "nersc": {
        '1.1p': '/global/cscratch1/sd/desc/DC2/data/Run1.1p/Run1.1/output',
        '1.2p': '/global/cscratch1/sd/desc/DC2/data/Run1.2p/w_2018_39/rerun/coadd-v4',
        '1.2p_v4': '/global/cscratch1/sd/desc/DC2/data/Run1.2p/w_2018_39/rerun/coadd-v4',
        '1.2p_v3': '/global/cscratch1/sd/desc/DC2/data/Run1.2p/w_2018_30/rerun/coadd-all2',
        '1.2i': '/global/cscratch1/sd/desc/DC2/data/Run1.2i/rerun/multiband',
        '2.1i': '/global/cscratch1/sd/desc/DC2/data/Run2.1i/rerun/coadd-dr4-v1',
        '2.1i_v1': '/global/cscratch1/sd/desc/DC2/data/Run2.1i/rerun/coadd-v1',
        '2.1i_dr1a': '/global/cscratch1/sd/desc/DC2/data/Run2.1i/rerun/coadd-v1',
        '2.1i_dr1b': '/global/cscratch1/sd/desc/DC2/data/Run2.1i/rerun/coadd-dr1b-v1',
        '2.1i_dr4': '/global/cscratch1/sd/desc/DC2/data/Run2.1i/rerun/coadd-dr4-v1',
        '2.2i_dr2': '/global/cfs/cdirs/lsst/shared/DC2-prod/Run2.2i/desc_dm_drp/v19.0.0/rerun/run2.2i-dr2-wfd-v1',
        '2.2i_dr2_wfd': '/global/cfs/cdirs/lsst/shared/DC2-prod/Run2.2i/desc_dm_drp/v19.0.0/rerun/run2.2i-dr2-wfd-v1',
        '2.2i_dr2_tract3828': '/global/cscratch1/sd/desc/DC2/data/Run2.2i/rerun/run2.2-coadd-wfd-y1-v1',
        '2.2i_dr3': '/global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/desc_dm_drp/v19.0.0-v1/rerun/run2.2i-coadd-wfd-dr3-v1',
        '2.2i_dia_y2_t3828': '/global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/desc_dm_drp/v19.0.0-v1/rerun/run2.2i-coadd-t3828-dia-y2-v1',
        '2.2i_dr6_wfd': '/global/cfs/cdirs/lsst/shared/DC2-prod/Run2.2i/desc_dm_drp/v19.0.0/rerun/run2.2i-dr6-v2',
        '2.2i_dr6': '/global/cfs/cdirs/lsst/shared/DC2-prod/Run2.2i/desc_dm_drp/v19.0.0/rerun/run2.2i-dr6-v2',
        '2.2i_dr6_v1': '/global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/desc_dm_drp/v19.0.0-v1/rerun/run2.2i-coadd-wfd-dr6-v1',
        'dia_2020Jan': '/global/cscratch1/sd/bos0109/templates_rect',
    },

    "in2p3": {
        '1.2p': '/sps/lsst/dataproducts/desc/DC2/Run1.2p/w_2018_39/rerun/coadd-v4',
        '1.2p_v4': '/sps/lsst/dataproducts/desc/DC2/Run1.2p/w_2018_39/rerun/coadd-v4',
        '1.2p_v3': '/sps/lsst/dataproducts/desc/DC2/Run1.2p/w_2018_30/rerun/coadd-all2',
        '1.2i': '/sps/lsst/dataproducts/desc/DC2/Run1.2i/w_2018_39/rerun/coadd-v1/',
        '2.1i_v1': '/sps/lsst/dataproducts/desc/DC2/Run2.1i/w_2019_19-v1/rerun/coadd-v1',
        '2.1i_dr1a': '/sps/lsst/dataproducts/desc/DC2/Run2.1i/w_2019_19-v1/rerun/coadd-v1',
        '2.1i_dr1b': '/sps/lsst/dataproducts/desc/DC2/Run2.1i/w_2019_19-v1/rerun/coadd-dr1b-v1',
        '2.2i_dr2': '/sps/lssttest/dataproducts/desc/DC2/Run2.2i/v19.0.0-v1/rerun/run2.2i-coadd-wfd-dr2-v1',
        '2.2i_dr2_tract3828': '/sps/lssttest/dataproducts/desc/DC2/Run2.2i/v19.0.0-v1/rerun/run2.2i-coadd-t3828-dia-y2-v1',
        '2.2i_dr3': '/sps/lssttest/dataproducts/desc/DC2/Run2.2i/v19.0.0-v1/rerun/run2.2i-coadd-wfd-dr3-v1',
        '2.2i_dr6_wfd': '/sps/lssttest/dataproducts/desc/DC2/Run2.2i/v19.0.0-v1/rerun/run2.2i-coadd-wfd-dr6-v1',
    },
}


def choose_repos_by_site():
    for site, repos in _REPOS.items():
        if site in SITE_INFO:
            return repos
    warnings.warn("Site '{}' not recognized. Default to nersc.".format(SITE_INFO))
    return _REPOS["nersc"]


REPOS = choose_repos_by_site()
