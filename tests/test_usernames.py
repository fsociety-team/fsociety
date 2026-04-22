"""Tests fonctionnels et non-régression - core/usernames.py (T08 à T09)"""

import pytest


# T08 - Cas usuel : ajouter un username et le retrouver
@pytest.mark.functional
def test_add_username_appears_in_get_usernames(temp_install_dir):
    from fsociety.core.usernames import add_username, get_usernames

    add_username("admin")
    usernames = get_usernames()
    assert "admin" in usernames


# T08 - Cas usuel : ajouts multiples
@pytest.mark.functional
def test_add_multiple_usernames(temp_install_dir):
    from fsociety.core.usernames import add_username, get_usernames

    add_username("root")
    add_username("user1")
    usernames = get_usernames()
    assert "root" in usernames
    assert "user1" in usernames


# T09 - Non-régression : get_usernames() retourne [] si le fichier est absent
@pytest.mark.non_regression
def test_get_usernames_returns_empty_list_when_file_missing(temp_install_dir):
    from fsociety.core.usernames import get_usernames

    usernames = get_usernames()
    assert usernames == []
    assert isinstance(usernames, list)
