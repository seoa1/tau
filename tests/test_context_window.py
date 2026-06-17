from pathlib import Path

from tau_agent import AssistantMessage, ToolCall, ToolResultMessage, UserMessage
from tau_coding.context_window import (
    estimate_context_tokens,
    estimate_message_tokens,
    estimate_text_tokens,
    summarize_messages_for_compaction,
)
from tau_coding.tools import create_coding_tools


def test_text_token_estimate_is_deterministic() -> None:
    assert estimate_text_tokens("") == 0
    assert estimate_text_tokens("a") == 1
    assert estimate_text_tokens("abcd") == 1
    assert estimate_text_tokens("abcde") == 2


def test_message_token_estimate_counts_roles_and_tool_calls() -> None:
    tool_call = ToolCall(id="call-1", name="read", arguments={"path": "README.md"})

    user_tokens = estimate_message_tokens(UserMessage(content="hello"))
    assistant_tokens = estimate_message_tokens(
        AssistantMessage(content="using tool", tool_calls=[tool_call])
    )
    tool_tokens = estimate_message_tokens(
        ToolResultMessage(tool_call_id="call-1", name="read", content="contents")
    )

    assert user_tokens > estimate_text_tokens("hello")
    assert assistant_tokens > user_tokens
    assert tool_tokens > estimate_text_tokens("contents")


def test_context_token_estimate_includes_system_messages_and_tools(tmp_path: Path) -> None:
    tools = tuple(create_coding_tools(cwd=tmp_path))

    estimate = estimate_context_tokens(
        system="You are Tau.",
        messages=(UserMessage(content="hello"), AssistantMessage(content="hi")),
        tools=tools,
    )

    assert estimate > estimate_text_tokens("You are Tau.hellohi")


def test_summarize_messages_for_compaction_is_deterministic() -> None:
    tool_call = ToolCall(id="call-1", name="read", arguments={"path": "README.md"})

    summary = summarize_messages_for_compaction(
        (
            UserMessage(content="Read README.md"),
            AssistantMessage(content="I'll inspect it.", tool_calls=[tool_call]),
            ToolResultMessage(tool_call_id="call-1", name="read", content="README contents"),
        )
    )

    assert summary == "\n".join(
        [
            "Automatically compacted 3 prior message(s).",
            "1. user: Read README.md",
            "2. assistant: I'll inspect it. [tool calls: read]",
            "3. tool: read ok: README contents",
        ]
    )
