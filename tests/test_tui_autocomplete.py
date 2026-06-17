from pathlib import Path

from tau_coding.commands import create_default_command_registry
from tau_coding.skills import Skill
from tau_coding.tui.autocomplete import build_completion_state


def test_command_completion_suggests_registered_commands() -> None:
    state = build_completion_state(
        "/st",
        command_registry=create_default_command_registry(),
        skills=(),
        prompt_templates=(),
    )

    assert [item.display for item in state.items] == ["/status"]
    assert state.selected is not None
    assert state.selected.apply("/st") == "/status"


def test_skill_command_completion_prefers_colon_form() -> None:
    state = build_completion_state(
        "/ski",
        command_registry=create_default_command_registry(),
        skills=(),
        prompt_templates=(),
    )

    assert "/skill:" in [item.display for item in state.items]


def test_skill_name_completion_preserves_request_text() -> None:
    state = build_completion_state(
        "/skill:r fix tests",
        command_registry=create_default_command_registry(),
        skills=(
            Skill(
                name="review",
                path=Path("review.md"),
                content="Review code",
                description="Review code",
            ),
        ),
        prompt_templates=(),
    )

    assert [item.display for item in state.items] == ["/skill:review"]
    assert state.selected is not None
    assert state.selected.apply("/skill:r fix tests") == "/skill:review fix tests"


def test_completion_selection_wraps() -> None:
    state = build_completion_state(
        "/s",
        command_registry=create_default_command_registry(),
        skills=(),
        prompt_templates=(),
    )

    assert len(state.items) > 1
    assert state.select_previous().selected_index == len(state.items) - 1
    assert state.select_next().selected_index == 1
