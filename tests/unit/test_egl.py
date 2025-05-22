import pytest
import os

try:
    from pyrender.platforms import egl
    EGL_SUPPORTED = True
except Exception:
    EGL_SUPPORTED = False


@pytest.mark.skipif(not EGL_SUPPORTED, reason="EGL is not supported on this system")
def test_default_device():
    egl.get_default_device()


@pytest.mark.skipif(not EGL_SUPPORTED, reason="EGL is not supported on this system")
def test_query_device():
    devices = egl.query_devices()
    assert len(devices) > 0


@pytest.mark.skipif(not EGL_SUPPORTED, reason="EGL is not supported on this system")
def test_init_context():
    device = egl.query_devices()[0]
    platform = egl.EGLPlatform(128, 128, device=device)
    platform.init_context()
