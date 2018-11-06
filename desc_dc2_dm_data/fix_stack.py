"""
fix_stack.py
a quick hack to make the new stack backward compatable
"""

import sys
import warnings

try:
    import lsst.obs.lsst.phosim
except ImportError:
    warnings.warn(
        '`lsst.obs.lsst` not available\n'
        'You are using an older kernel or you are not using the desc-stack kernel!\n'
        'Log in to cori.nersc.gov and run: `/global/common/software/lsst/common/miniconda/kernels/setup.sh`\n'
        'If you only need the repo paths, you can simply ignore this warning.'
    )
else:
    sys.modules['lsst.obs.lsstCam.lsstCamMapper'] = lsst.obs.lsst.phosim
