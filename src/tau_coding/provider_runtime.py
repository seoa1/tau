"""Runtime provider construction for Tau coding sessions."""

from typing import Protocol

from tau_ai import AnthropicProvider, ModelProvider, OpenAICompatibleProvider
from tau_coding.credentials import FileCredentialStore
from tau_coding.provider_config import (
    AnthropicProviderConfig,
    ProviderConfig,
    anthropic_config_from_provider,
    openai_compatible_config_from_provider,
)


class ClosableModelProvider(ModelProvider, Protocol):
    """Runtime provider object Tau owns and can close."""

    async def aclose(self) -> None:
        """Close any provider-owned resources."""
        ...


def create_model_provider(
    provider: ProviderConfig,
    *,
    credential_store: FileCredentialStore | None = None,
) -> ClosableModelProvider:
    """Create a runtime model provider from durable provider settings."""
    credentials = credential_store or FileCredentialStore()
    if isinstance(provider, AnthropicProviderConfig):
        return AnthropicProvider(
            anthropic_config_from_provider(provider, credential_reader=credentials)
        )
    return OpenAICompatibleProvider(
        openai_compatible_config_from_provider(provider, credential_reader=credentials)
    )
