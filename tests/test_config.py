"""Tests fonctionnels - core/config.py (T01 à T04)"""

from configparser import RawConfigParser

import pytest


# T01 - Cas usuel : lecture config existante
@pytest.mark.functional
def test_get_config_returns_valid_config(fresh_config):
    assert fresh_config is not None
    assert isinstance(fresh_config, RawConfigParser)
    assert fresh_config.has_section("fsociety")


# T01 - Cas usuel : toutes les clés par défaut présentes
@pytest.mark.functional
def test_get_config_has_all_default_keys(fresh_config):
    import fsociety.core.config as cfg

    for key in cfg.DEFAULT_CONFIG:
        assert fresh_config.has_option("fsociety", key), f"Clé manquante : {key}"


# T02 - Cas extrême : création config quand INSTALL_DIR n'existe pas
@pytest.mark.functional
def test_get_config_creates_install_dir(tmp_path, monkeypatch):
    import fsociety.core.config as cfg

    new_dir = tmp_path / "new_fsociety"
    monkeypatch.setattr(cfg, "INSTALL_DIR", str(new_dir))
    monkeypatch.setattr(cfg, "CONFIG_FILE", str(new_dir / "fsociety.cfg"))

    config = cfg.get_config()
    assert new_dir.exists()
    assert (new_dir / "fsociety.cfg").exists()
    assert config.has_section("fsociety")


# T03 - Non-régression : clé manquante dans config → ajout automatique
@pytest.mark.non_regression
def test_check_config_adds_missing_key(temp_install_dir):
    from configparser import RawConfigParser

    import fsociety.core.config as cfg

    # Créer un config sans la clé 'ssh_clone'
    config = RawConfigParser()
    config["fsociety"] = {
        k: v for k, v in cfg.DEFAULT_CONFIG.items() if k != "ssh_clone"
    }
    with open(cfg.CONFIG_FILE, "w", encoding="utf-8") as f:
        config.write(f)

    config.read(cfg.CONFIG_FILE)
    assert not config.has_option("fsociety", "ssh_clone")

    cfg.check_config(config)
    assert config.has_option("fsociety", "ssh_clone")
    assert config.get("fsociety", "ssh_clone") == cfg.DEFAULT_CONFIG["ssh_clone"]


# T04 - Cas usuel : write_config persiste les modifications
@pytest.mark.functional
def test_write_config_persists_changes(fresh_config):
    import fsociety.core.config as cfg

    fresh_config.set("fsociety", "agreement", "true")
    cfg.write_config(fresh_config)

    reloaded = RawConfigParser()
    reloaded.read(cfg.CONFIG_FILE)
    assert reloaded.get("fsociety", "agreement") == "true"
