"""Tests fonctionnels - base64 et utilitaires (T10 à T12)"""

from base64 import b64decode

import pytest


# T10 - Cas usuel : décodage base64 valide
@pytest.mark.functional
def test_base64_decode_valid_string():
    result = b64decode("aGVsbG8=")
    assert result == b"hello"


# T10 - Cas usuel : décodage d'une chaîne plus longue
@pytest.mark.functional
def test_base64_decode_longer_string():
    result = b64decode("ZnNvY2lldHk=")
    assert result == b"fsociety"


# T11 - Cas extrême : décodage base64 avec padding ajouté manuellement
@pytest.mark.functional
def test_base64_decode_with_manual_padding():
    # Ajouter le padding manquant avant décodage
    encoded = "aGVsbG8"
    padded = encoded + "=" * (-len(encoded) % 4)
    result = b64decode(padded)
    assert result == b"hello"


# T12 - Cas d'erreur : chaîne non-base64 invalide
@pytest.mark.functional
def test_base64_decode_invalid_raises():
    with pytest.raises(Exception):
        b64decode("!!invalid!!", validate=True)


# Test de l'instanciation de la classe Utility
@pytest.mark.functional
def test_utility_str_returns_class_name():
    from fsociety.core.utilities import base64_decode, host2ip, spawn_shell

    assert str(base64_decode()) == "base64_decode"
    assert str(host2ip()) == "host2ip"
    assert str(spawn_shell()) == "spawn_shell"


# Test que chaque utilitaire a une description
@pytest.mark.functional
def test_utility_has_description():
    from fsociety.core.utilities import base64_decode, host2ip, suggest_tool

    assert base64_decode().description is not None
    assert host2ip().description is not None
    assert suggest_tool().description is not None
