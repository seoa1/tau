"""Built-in provider catalog for Tau login/setup flows."""

from dataclasses import dataclass
from typing import Literal

ProviderKind = Literal["openai-compatible", "anthropic"]


@dataclass(frozen=True, slots=True)
class ProviderCatalogEntry:
    """A built-in provider Tau can present during login."""

    name: str
    display_name: str
    kind: ProviderKind
    base_url: str
    api_key_env: str
    credential_name: str
    models: tuple[str, ...]
    default_model: str
    docs_url: str


BUILTIN_PROVIDER_CATALOG: tuple[ProviderCatalogEntry, ...] = (
    ProviderCatalogEntry(
        name="openai",
        display_name="OpenAI",
        kind="openai-compatible",
        base_url="https://api.openai.com/v1",
        api_key_env="OPENAI_API_KEY",
        credential_name="openai",
        models=("gpt-4.1-mini", "gpt-4.1", "gpt-4o-mini"),
        default_model="gpt-4.1-mini",
        docs_url="https://platform.openai.com/docs",
    ),
    ProviderCatalogEntry(
        name="anthropic",
        display_name="Anthropic",
        kind="anthropic",
        base_url="https://api.anthropic.com/v1",
        api_key_env="ANTHROPIC_API_KEY",
        credential_name="anthropic",
        models=("claude-sonnet-4-6", "claude-opus-4-8", "claude-haiku-4-5"),
        default_model="claude-sonnet-4-6",
        docs_url="https://docs.anthropic.com",
    ),
    ProviderCatalogEntry(
        name="openrouter",
        display_name="OpenRouter",
        kind="openai-compatible",
        base_url="https://openrouter.ai/api/v1",
        api_key_env="OPENROUTER_API_KEY",
        credential_name="openrouter",
        models=("openai/gpt-4.1-mini", "anthropic/claude-sonnet-4.5"),
        default_model="openai/gpt-4.1-mini",
        docs_url="https://openrouter.ai/docs",
    ),
    ProviderCatalogEntry(
        name="huggingface",
        display_name="Hugging Face Inference Providers",
        kind="openai-compatible",
        base_url="https://router.huggingface.co/v1",
        api_key_env="HF_TOKEN",
        credential_name="huggingface",
        models=("openai/gpt-oss-120b",),
        default_model="openai/gpt-oss-120b",
        docs_url="https://huggingface.co/inference/get-started",
    ),
)


def builtin_provider_entry(name: str) -> ProviderCatalogEntry | None:
    """Return a built-in catalog entry by provider name."""
    for entry in BUILTIN_PROVIDER_CATALOG:
        if entry.name == name:
            return entry
    return None
