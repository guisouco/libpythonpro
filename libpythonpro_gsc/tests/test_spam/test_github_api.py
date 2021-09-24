from unittest.mock import Mock

import pytest as pytest

from libpythonpro_gsc import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/89437136?v=4'
    resp_mock.json.return_value = {
        "login": "guisouco", "id": 89437136,
        "avatar_url": url,
    }
    get_mock=mocker.patch('libpythonpro_gsc.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url

def test_buscar_avatar(avatar_url):
    url=github_api.buscar_avatar('guisouco')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url=github_api.buscar_avatar('guisouco')
    assert 'https://avatars.githubusercontent.com/u/89437136?v=4'== url
