from abc import ABC, abstractmethod
from enum import Enum, auto

from command_based_framework._common import ContextManagerMixin
from command_based_framework.commands import Command
from command_based_framework.scheduler import Scheduler


class Condition(Enum):
    """Enums representing different action conditions."""

    cancel_when_activated = auto()
    toggle_when_activated = auto()
    when_activated = auto()
    when_deactivated = auto()
    when_held = auto()


class Action(ABC, ContextManagerMixin):  # noqa: WPS214
    """Schedules :py:class:`~command_based_framework.commands.Command` based on a condition being met.

    Actions determine when commands are scheduled/executed. To do this,
    the scheduler periodically runs the :py:meth:`~command_based_framework.actions.Action.poll`
    method. Any arbitrary condition, or multiple conditions, can be
    implemented in :py:meth:`~command_based_framework.actions.Action.poll`.

    To setup when commands are scheduled, bind them using any of the
    `when` methods. Attempts to bind a command multiple times in the
    same action will result in the previous binding being replaced by
    the new one.

    A command can be bound to a single or multiple actions.
    """  # noqa: E501

    # Flag to indicate the state of the action the last time it was
    # checked
    _last_state: bool

    def __init__(self) -> None:
        """Creates a new `Action` instance."""
        super().__init__()
        self._last_state = False

    @property
    def last_state(self) -> bool:
        """The state of the action the last time it was checked."""
        return self._last_state

    @last_state.setter
    def last_state(self, state: bool) -> None:
        self._last_state = state

    @abstractmethod
    def poll(self) -> bool:
        """Check if the condition to activate commands are met.

        Only return `True` when all conditions are met for this action
        to activate and schedule bound commands.
        """
        return False  # pragma: no cover

    def cancel_when_activated(self, command: Command) -> None:
        """Cancel `command` when this action is activated."""
        Scheduler.instance.bind_command(  # type: ignore
            self,
            command,
            Condition.cancel_when_activated,
        )

    def toggle_when_activated(self, command: Command) -> None:
        """Toggle scheduling `command` when this action is activated.

        For example, a button is pressed for the first time and a
        command runs. The same button is pressed again, but the command
        exits. The cycle repeats when the button is pressed for a third
        time.
        """
        Scheduler.instance.bind_command(  # type: ignore
            self,
            command,
            Condition.toggle_when_activated,
        )

    def when_activated(self, command: Command) -> None:
        """Schedule `command` when this action is activated."""
        Scheduler.instance.bind_command(  # type: ignore
            self,
            command,
            Condition.when_activated,
        )

    def when_deactivated(self, command: Command) -> None:
        """Schedule `command` when this action is deactivated."""
        Scheduler.instance.bind_command(  # type: ignore
            self,
            command,
            Condition.when_deactivated,
        )

    def when_held(self, command: Command) -> None:
        """Schedule `command` when this action is perpetually activated."""
        Scheduler.instance.bind_command(  # type: ignore
            self,
            command,
            Condition.when_held,
        )
