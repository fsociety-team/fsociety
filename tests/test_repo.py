"""Tests fonctionnels et non-régression - core/repo.py (T16 à T20)"""

import pytest


# Classe concrète minimale pour tester GitHubRepo (qui est abstract)
class ConcreteRepo:
    """Sous-classe minimale de GitHubRepo pour les tests."""

    def __init__(self, path):
        from fsociety.core.repo import GitHubRepo

        self._base = GitHubRepo.__new__(GitHubRepo)
        self._base.path = path
        self._base.name = path.split("/")[-1]
        self._base.full_path = f"/tmp/fsociety_test/{self._base.name}"
        self._base.description = "Test tool"

    def installed(self):
        import os

        return os.path.exists(self._base.full_path)

    def __str__(self):
        return self._base.name.lower().replace("-", "_")


# T16 - Cas usuel : outil installé (chemin existe)
@pytest.mark.functional
def test_repo_installed_true_when_path_exists(tmp_path):
    from fsociety.core.repo import GitHubRepo

    class TestRepo(GitHubRepo):
        def run(self):
            return 0

    repo = TestRepo.__new__(TestRepo)
    repo.full_path = str(tmp_path)
    assert repo.installed() is True


# T17 - Cas usuel : outil non installé (chemin absent)
@pytest.mark.functional
def test_repo_installed_false_when_path_missing():
    from fsociety.core.repo import GitHubRepo

    class TestRepo(GitHubRepo):
        def run(self):
            return 0

    repo = TestRepo.__new__(TestRepo)
    repo.full_path = "/nonexistent/path/that/does/not/exist"
    assert repo.installed() is False


# T18 - Cas usuel : __str__ retourne nom en minuscules avec underscores
@pytest.mark.functional
def test_repo_str_lowercases_and_replaces_hyphens():
    from fsociety.core.repo import GitHubRepo

    class TestRepo(GitHubRepo):
        def run(self):
            return 0

    repo = TestRepo.__new__(TestRepo)
    repo.path = "owner/My-Tool"
    repo.name = "My-Tool"
    assert str(repo) == "my_tool"


# T18 - Cas usuel : nom sans tiret reste inchangé (en minuscules)
@pytest.mark.functional
def test_repo_str_no_hyphens():
    from fsociety.core.repo import GitHubRepo

    class TestRepo(GitHubRepo):
        def run(self):
            return 0

    repo = TestRepo.__new__(TestRepo)
    repo.path = "owner/mytool"
    repo.name = "mytool"
    assert str(repo) == "mytool"


# T19 - Cas usuel : print_pip_deps avec une liste
@pytest.mark.functional
def test_print_pip_deps_with_list(capsys):
    from fsociety.core.repo import print_pip_deps

    # Ne doit pas lever d'exception
    print_pip_deps(["requests", "rich", "GitPython"])


# T20 - Non-régression : print_pip_deps avec type invalide lève ValueError
@pytest.mark.non_regression
def test_print_pip_deps_invalid_type_raises_value_error():
    from fsociety.core.repo import print_pip_deps

    with pytest.raises(ValueError):
        print_pip_deps(42)
