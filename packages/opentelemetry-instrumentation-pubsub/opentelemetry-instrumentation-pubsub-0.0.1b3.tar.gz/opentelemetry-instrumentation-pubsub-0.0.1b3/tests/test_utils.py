import importlib_metadata

from pubsub_opentelemetry.utils import _get_distro_version


def test_get_distro_version(mocker):
    mocker.patch('importlib_metadata.version')
    importlib_metadata.version.return_value = '1.2.3'
    v = _get_distro_version('some-package')
    assert v == '1.2.3'


def test_get_not_found_distro_version(mocker):
    mocker.patch('importlib_metadata.version')
    importlib_metadata.version.side_effect = importlib_metadata.PackageNotFoundError()
    v = _get_distro_version('some-package')
    assert v == '0.0'
