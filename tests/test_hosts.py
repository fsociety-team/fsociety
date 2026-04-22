"""Tests fonctionnels et non-régression - core/hosts.py (T05 à T07)"""

import pytest


# T05 - Cas usuel : ajouter un hôte valide et le retrouver
@pytest.mark.functional
def test_add_host_appears_in_get_hosts(temp_install_dir):
    from fsociety.core.hosts import add_host, get_hosts

    add_host("example.com")
    hosts = get_hosts()
    assert "example.com" in hosts


# T05 - Cas usuel : ajouts multiples
@pytest.mark.functional
def test_add_multiple_hosts(temp_install_dir):
    from fsociety.core.hosts import add_host, get_hosts

    add_host("host1.com")
    add_host("host2.com")
    hosts = get_hosts()
    assert "host1.com" in hosts
    assert "host2.com" in hosts


# T06 - Non-régression : hôte vide doit lever ValueError
@pytest.mark.non_regression
def test_add_empty_host_raises_value_error(temp_install_dir):
    from fsociety.core.hosts import add_host

    with pytest.raises(ValueError):
        add_host("")


# T07 - Non-régression : get_hosts() retourne [] si le fichier est absent
@pytest.mark.non_regression
def test_get_hosts_returns_empty_list_when_file_missing(temp_install_dir):
    from fsociety.core.hosts import get_hosts

    hosts = get_hosts()
    assert hosts == []
    assert isinstance(hosts, list)
