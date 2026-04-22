"""Tests fonctionnels - __main__.py : navigation menu et accord (T21 à T23)"""

from unittest.mock import patch

import pytest


# T21 - Cas d'erreur : commande invalide dans le menu principal
@pytest.mark.functional
def test_mainloop_invalid_command_prints_warning(fresh_config, monkeypatch):
    import fsociety.__main__ as main_mod
    from fsociety.console import console

    monkeypatch.setattr(main_mod, "config", fresh_config)
    fresh_config.set("fsociety", "agreement", "true")

    messages = []
    original_print = console.print

    def capture_print(*args, **kwargs):
        messages.append(str(args[0]) if args else "")
        return original_print(*args, **kwargs)

    with patch("builtins.input", return_value="nonexistent_command"), patch.object(
        console, "print", side_effect=capture_print
    ):
        main_mod.mainloop()

    assert any("Invalid Command" in m for m in messages)


# T22 - Cas extrême : commande vide dans le menu
@pytest.mark.functional
def test_mainloop_empty_command_prints_warning(fresh_config, monkeypatch):
    import fsociety.__main__ as main_mod
    from fsociety.console import console

    monkeypatch.setattr(main_mod, "config", fresh_config)
    fresh_config.set("fsociety", "agreement", "true")

    messages = []

    def capture_print(*args, **kwargs):
        messages.append(str(args[0]) if args else "")

    with patch("builtins.input", return_value=""), patch.object(
        console, "print", side_effect=capture_print
    ):
        main_mod.mainloop()

    assert any("Invalid Command" in m for m in messages)


# T23 - Cas usuel : agreement déjà acceptée → pas d'affichage des CGU
@pytest.mark.functional
def test_agreement_skipped_when_already_accepted(fresh_config, monkeypatch):
    import fsociety.__main__ as main_mod

    monkeypatch.setattr(main_mod, "config", fresh_config)
    fresh_config.set("fsociety", "agreement", "true")

    # Si agreement() n'appelle pas input(), le test passe sans bloquer
    with patch(
        "builtins.input", side_effect=AssertionError("input() ne doit pas être appelé")
    ):
        main_mod.agreement()  # Ne doit pas lever d'exception
