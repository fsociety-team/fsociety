from configparser import RawConfigParser

import pytest


@pytest.fixture
def temp_install_dir(monkeypatch, tmp_path):
    """Provide a temporary INSTALL_DIR to avoid touching the real user config."""
    install_dir = tmp_path / ".fsociety"
    install_dir.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))

    import fsociety.core.config as cfg
    import fsociety.core.hosts as hosts_mod
    import fsociety.core.usernames as usernames_mod

    original_install = cfg.INSTALL_DIR
    original_config_file = cfg.CONFIG_FILE
    original_hosts_path = hosts_mod.full_path
    original_usernames_path = usernames_mod.full_path

    cfg.INSTALL_DIR = str(install_dir)
    cfg.CONFIG_FILE = str(install_dir / "fsociety.cfg")
    hosts_mod.full_path = str(install_dir / "hosts.txt")
    usernames_mod.full_path = str(install_dir / "usernames.txt")

    yield install_dir

    cfg.INSTALL_DIR = original_install
    cfg.CONFIG_FILE = original_config_file
    hosts_mod.full_path = original_hosts_path
    usernames_mod.full_path = original_usernames_path


@pytest.fixture
def fresh_config(temp_install_dir):
    """Return a freshly created config using the temp install dir."""
    import fsociety.core.config as cfg

    config = RawConfigParser()
    config["fsociety"] = cfg.DEFAULT_CONFIG.copy()
    with open(cfg.CONFIG_FILE, "w", encoding="utf-8") as f:
        config.write(f)
    return cfg.get_config()
