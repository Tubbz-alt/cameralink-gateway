from setuptools import setup, find_packages

# use softlinks to make the various "board-support-package" submodules
# look like subpackages of TimeTool.  Then __init__.py will modify
# sys.path so that the correct "local" versions of surf etc. are
# picked up.  A better approach would be using relative imports
# in the submodules, but that's more work.  -cpo

subpackages = ['surf/python/surf','lcls-timing-core/python/LclsTimingCore','lcls2-pgp-fw-lib/python/lcls2_pgp_fw_lib','l2si-core/python/l2si_core','axi-pcie-core/python/axipcie','clink-gateway-fw-lib/python/ClinkFeb']

import os
print(os.path.dirname(os.path.realpath(__file__)))

for pkgpath in subpackages:
    pkgname = pkgpath.split('/')[-1]
    linkname = os.path.join('cameralink_gateway',pkgname)
    if os.path.islink(linkname): os.remove(linkname)
    os.symlink(os.path.join('../../submodules',pkgpath),linkname)

setup(
    name = 'cameralink_gateway',
    description = 'CLink gateway package',
    packages = find_packages(),
)
