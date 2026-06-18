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
        models=(
            "gpt-5.5",
            "gpt-5.5-pro",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.3-codex",
            "gpt-5.2",
            "gpt-5.1",
            "gpt-5",
            "gpt-5-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
        ),
        default_model="gpt-5.5",
        docs_url="https://platform.openai.com/docs",
    ),
    ProviderCatalogEntry(
        name="anthropic",
        display_name="Anthropic",
        kind="anthropic",
        base_url="https://api.anthropic.com/v1",
        api_key_env="ANTHROPIC_API_KEY",
        credential_name="anthropic",
        models=(
            "claude-sonnet-4-6",
            "claude-opus-4-8",
            "claude-haiku-4-5",
        ),
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
        models=(
            "openai/gpt-5.5",
            "openai/gpt-5.4",
            "openai/gpt-5.3-codex",
            "anthropic/claude-sonnet-4.6",
            "anthropic/claude-opus-4.8",
            "google/gemini-3.5-pro",
            "deepseek/deepseek-r1",
            "qwen/qwen3-coder",
        ),
        default_model="openai/gpt-5.5",
        docs_url="https://openrouter.ai/docs",
    ),
    ProviderCatalogEntry(
        name="huggingface",
        display_name="Hugging Face Inference Providers",
        kind="openai-compatible",
        base_url="https://router.huggingface.co/v1",
        api_key_env="HF_TOKEN",
        credential_name="huggingface",
        models=(
            "openai/gpt-oss-120b",
            "Qwen/Qwen3-Coder",
            "Qwen/Qwen3-Coder-Next",
            "deepseek-ai/DeepSeek-R1",
            "moonshotai/Kimi-K2-Instruct",
            "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
        ),
        default_model="Qwen/Qwen3-Coder",
        docs_url="https://huggingface.co/inference/get-started",
    ),
)


def builtin_provider_entry(name: str) -> ProviderCatalogEntry | None:
    """Return a built-in catalog entry by provider name."""
    for entry in BUILTIN_PROVIDER_CATALOG:
        if entry.name == name:
            return entry
    return None
