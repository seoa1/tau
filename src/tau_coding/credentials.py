"""Local credential storage for Tau provider API keys."""

from json import dumps, loads
from pathlib import Path

from tau_coding.paths import TauPaths


class CredentialStoreError(ValueError):
    """Raised when Tau credential storage cannot be read or written."""


class FileCredentialStore:
    """Small JSON-backed API key store under Tau home."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or credentials_path()

    def get(self, name: str) -> str | None:
        """Return a stored credential value by name."""
        return self._load().get(name)

    def set(self, name: str, value: str) -> None:
        """Store a credential value by name."""
        if not name.strip():
            raise CredentialStoreError("Credential name must not be empty")
        if not value.strip():
            raise CredentialStoreError("Credential value must not be empty")
        data = self._load()
        data[name.strip()] = value.strip()
        self._save(data)

    def delete(self, name: str) -> None:
        """Delete a stored credential value by name."""
        data = self._load()
        data.pop(name, None)
        self._save(data)

    def _load(self) -> dict[str, str]:
        if not self.path.exists():
            return {}
        raw = loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CredentialStoreError("Tau credentials must be a JSON object")
        credentials: dict[str, str] = {}
        for key, value in raw.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise CredentialStoreError("Tau credential names and values must be strings")
            credentials[key] = value
        return credentials

    def _save(self, data: dict[str, str]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        self.path.chmod(0o600)


def credentials_path(paths: TauPaths | None = None) -> Path:
    """Return Tau's local provider credential path."""
    return (paths or TauPaths()).home / "credentials.json"
