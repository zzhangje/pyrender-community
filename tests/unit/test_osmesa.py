import os
import pytest


try:
    from pyrender.platforms import osmesa
    OSMESA_SUPPORTED = True
except Exception:
    OSMESA_SUPPORTED = False


@pytest.mark.skipif(not OSMESA_SUPPORTED, reason="OSMesa is not supported on this system")
def tmp_test_init_context():
    platform = osmesa.OSMesaPlatform(1, 1)
    platform.init_context()
    assert platform._context is not None
    assert platform._buffer is not None


@pytest.mark.skipif(not OSMESA_SUPPORTED, reason="OSMesa is not supported on this system")
def tmp_test_make_current():
    platform = osmesa.OSMesaPlatform(1, 1)
    platform.init_context()
    platform.make_current()
    assert platform._context is not None
