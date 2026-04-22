"""Tests fonctionnels - core/menu.py (T13 à T15, T24 à T25)"""

import pytest

import fsociety.core.utilities


# T13 - Cas usuel : module_name retourne le dernier segment
@pytest.mark.functional
def test_module_name_returns_last_segment():
    import fsociety.information_gathering as ig
    from fsociety.core.menu import module_name

    result = module_name(ig)
    assert result == "information_gathering"


# T13 - Cas usuel : module_name sur le module utilities
@pytest.mark.functional
def test_module_name_on_utilities():
    from fsociety.core.menu import module_name

    result = module_name(fsociety.core.utilities)
    assert result == "utilities"


# T14 - Cas usuel : prompt() sans argument
@pytest.mark.functional
def test_prompt_default():
    from fsociety.core.menu import prompt

    result = prompt()
    assert "fsociety" in result
    assert "#" in result


# T15 - Cas usuel : prompt() avec chemin
@pytest.mark.functional
def test_prompt_with_path():
    from fsociety.core.menu import prompt

    result = prompt("information_gathering")
    assert "information_gathering" in result


# T24 - Cas usuel : autocomplétion avec texte partiel
@pytest.mark.functional
def test_completer_partial_match():
    from fsociety.core.menu import CommandCompleter

    completer = CommandCompleter(["information_gathering", "networking", "web_apps"])
    result = completer.complete("inf", 0)
    assert result == "information_gathering"


# T24 - Cas usuel : autocomplétion retourne uniquement le premier match (état 0)
@pytest.mark.functional
def test_completer_returns_first_match_for_state_zero():
    from fsociety.core.menu import CommandCompleter

    completer = CommandCompleter(["networking", "network_scan"])
    first = completer.complete("net", 0)
    assert first is not None
    assert first.startswith("net")


# T25 - Cas extrême : autocomplétion sans résultat
@pytest.mark.functional
def test_completer_no_match_returns_none():
    from fsociety.core.menu import CommandCompleter

    completer = CommandCompleter(["information_gathering", "networking"])
    result = completer.complete("xyz", 0)
    assert result is None


# T25 - Cas extrême : autocomplétion vide retourne la première option (état 0)
@pytest.mark.functional
def test_completer_empty_text_returns_first_option():
    from fsociety.core.menu import CommandCompleter

    options = ["information_gathering", "networking", "web_apps"]
    completer = CommandCompleter(options)
    # Avec state=0 et texte vide, retourne la première option (liste triée)
    result = completer.complete("", 0)
    assert result in options
