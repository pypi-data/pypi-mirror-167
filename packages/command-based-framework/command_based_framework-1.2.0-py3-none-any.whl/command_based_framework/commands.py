import itertools
import sys
import time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Event
from types import TracebackType
from typing import Iterator, Optional, Set, Tuple, Type, Union

if sys.version_info >= (3, 10):
    # WPS433: Found nested import
    # WPS440: Found block variables overlap
    from typing import TypeAlias  # noqa: WPS433, WPS440; pragma: no cover
else:
    # WPS433: Found nested import
    # WPS440: Found block variables overlap
    from typing_extensions import TypeAlias  # noqa: WPS433, WPS440; pragma: no cover

from command_based_framework._common import ContextManagerMixin
from command_based_framework.scheduler import Scheduler
from command_based_framework.subsystems import Subsystem

CommandType: TypeAlias = Union["Command", "CommandGroup"]


class Command(ABC, ContextManagerMixin):  # noqa: WPS214
    """Executes a process when activated by an :py:class:`~command_based_framework.actions.Action`.

    Commands dictate what subsystems do at what time. They are scheduled
    when a :py:meth:`~command_based_framework.actions.Action.poll`
    bound condition is met. Commands are also synchronous, meaning they
    are always blocking the scheduler's event loop and should complete
    quickly.

    Commands have the following life cycle in the scheduler:

    **1.** New commands have their :py:meth:`~command_based_framework.commands.Command.initialize`
    method called.

    **2.** Actions bound to this command have their :py:meth:`~command_based_framework.actions.Action.poll`
    method called. Depending on how a command is bound to an action, the
    scheduler may skip directly to step 4 for a command.

    **3.** The scheduler now periodically executes these new commands by
    calling their :py:meth:`~command_based_framework.commands.Command.is_finished`
    and :py:meth:`~command_based_framework.commands.Command.execute`
    methods, in that order.

    **4.** Whether through an action or :py:meth:`~command_based_framework.commands.Command.is_finished`,
    commands have their :py:meth:`~command_based_framework.commands.Command.end`
    methods called and are removed from the stack.

    Commands also maintain their state after being unscheduled as long
    as a reference is maintained. The scheduler maintains a reference as
    long as the command is scheduled, but releases it immediately after.
    """  # noqa: E501

    # The name of the command
    _name: str

    # Requirements are the subsystems required for this command to run.
    # The scheduler uses this to ensure only one command is using a
    # subsystem at any time
    _requirements: Set[Subsystem]

    # Indicates whether or not the command needs to be interrupted after
    # encountering an error
    _needs_interrupt: bool

    def __init__(self, name: Optional[str] = None, *subsystems: Subsystem) -> None:
        """Creates a new `Command` instance.

        :param name: The name of the command. If not provided, the class
            name is used instead.
        :type name: str, optional
        :param subsystems: Variable length of subsystems to
            automatically require.
        :type subsystems: tuple
        """
        super().__init__()
        self._name = name or self.__class__.__name__
        self._requirements = set()
        self._needs_interrupt = False

        # Register each subsystem as a requirements
        self.add_requirements(*subsystems)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> bool:
        """Called when the command exits a context manager."""
        # Ignore non-errors
        if not exc_type or not exc or not traceback:
            return True

        handled = self.handle_exception(exc_type, exc, traceback)
        self.needs_interrupt = not handled or not isinstance(handled, bool)
        return True

    def __repr__(self) -> str:
        """Unicode representation of the class."""
        return self.__str__()

    def __str__(self) -> str:
        """Unicode representation of the class."""
        return "<{name}>".format(name=self.name)

    @property
    def name(self) -> str:
        """The name of the command.

        This is a read-only property.

        If one was not provided at the creation of the command, the
        class name is used instead.
        """
        return self._name

    @property
    def needs_interrupt(self) -> bool:
        """Indicates if the command needs to be interrupted.

        This property should not be set directly as it is managed by the
        scheduler.

        Every read of this property resets its state.
        """
        ret = self._needs_interrupt
        self.needs_interrupt = False
        return ret

    @needs_interrupt.setter
    def needs_interrupt(self, state: bool) -> None:
        self._needs_interrupt = state

    @property
    def requirements(self) -> Set[Subsystem]:
        """The subsystems this command requires to run.

        This is a read-only property.
        """
        return self._requirements

    def add_requirements(self, *subsystems: Subsystem) -> None:
        """Register any number of subsystems as a command requirement.

        Only one command can be running with any given requirement. If
        two commands share any requirement and are scheduled to run,
        which command runs may be undefined. If one command is already
        scheduled then it will be interrupted by the newly scheduled
        command.
        """
        self._requirements.update(set(subsystems))

    def handle_exception(
        self,
        exc_type: Type[BaseException],
        exc: BaseException,
        traceback: TracebackType,
    ) -> bool:
        """Called when :py:meth:`~command_based_framework.commands.Command.execute` raises an error.

        The scheduler uses the output of this method to determine
        whether the command should be immediately interrupted.

        :param exc_type: The type of exception raised.
        :type exc_type: :py:class:`Type`
        :param exc: The exception raised.
        :type exc: :py:class:`Exception`
        :param traceback: The frame traceback of the error.
        :type traceback: :py:class:`Traceback`

        :return: `True` to indicate the error is handled. All other
            returns to the scheduler will be interpreted as the command
            needing to be immediately interrupted.
        :rtype: bool
        """  # noqa: DAR202

    def initialize(self) -> None:
        """Called each time the command in scheduled.

        Any initialization or pre-execution code should go here.
        """

    @abstractmethod
    def execute(self) -> None:
        """Periodically called while the command is scheduled.

        All execution code should go here.
        """

    def end(self, interrupted: bool) -> None:
        """Called once the command has been unscheduled.

        Any clean up or post-execution code should go here.

        :param interrupted: the command was interrupted, not ended.
        :type interrupted: bool
        """

    @abstractmethod
    def is_finished(self) -> bool:
        """Periodically called before :py:meth:`~command_based_framework.commands.Command.execute` while the command is scheduled.

        :return: `True` if the command should end, otherwise `False`.
        :rtype: bool
        """  # noqa: E501


class CommandGroup(Command):
    """Group commands into a single manageable interface.

    Only provides a modified command `__init__` method which accepts
    commands instead of subsystems. Also requires all subsystems by any
    passed commands which may share requirements. Note this behavior may
    change on child classes of this abstract.

    Any command or group can be provided to this abstract.
    """

    _commands: Tuple[CommandType, ...]

    def __init__(self, name: Optional[str] = None, *commands: CommandType) -> None:
        """Creates a new :class:`~CommandGroup` instance.

        Args:
            name: The name of the command group. If not provided, the
                class name is used instead.
            commands: Variable length of commands to group.
        """  # noqa: RST203
        super().__init__(name)

        # Require all subsystems
        for command in commands:
            self.add_requirements(*command.requirements)

        self._commands = commands


class SequentialCommandGroup(CommandGroup):
    """Sequentially executes commands.

    The order which commands are provided to the constructor determines
    the order the commands are executed. If any commands error or are
    interrupted, no further commands will be executed.

    Any command or group can be provided to the constructor.
    """

    _sequence: Iterator[CommandType]
    _current_command: Optional[CommandType]
    _end_of_sequence: bool

    def __init__(self, name: Optional[str] = None, *commands: CommandType) -> None:
        """Creates a new :class:`~SequentialCommandGroup` instance.

        Args:
            name: The name of the command group. If not provided, the
                class name is used instead.
            commands: Variable length of commands to group.
        """  # noqa: RST203
        super().__init__(name, *commands)
        self._end_of_sequence = False

    def initialize(self) -> None:
        """Select the first command in the chain to run."""
        self._end_of_sequence = False
        self._sequence = iter(self._commands)
        self._prepare_next_command()

    def execute(self) -> None:
        """Execute the currently sequenced command."""
        # mypy fix, check if self._current_command is set
        if not self._current_command:  # pragma: no cover
            self._end_of_sequence = True  # pragma: no cover
            return  # pragma: no cover

        # Check if the current command has finished
        # If so, end it and prepare the next one
        if self._current_command.is_finished():
            self._current_command.end(interrupted=False)
            self._prepare_next_command()
            return

        # Execute the current command
        self._current_command.execute()

    def is_finished(self) -> bool:
        """Check if the end of the chain has been reached."""
        return self._end_of_sequence or not self._current_command

    def end(self, interrupted: bool) -> None:
        """End the current command."""
        if self._current_command:
            self._current_command.end(interrupted=interrupted)

    def _prepare_next_command(self) -> None:
        try:
            self._current_command = next(self._sequence)
        except StopIteration:
            self._current_command = None
            self._end_of_sequence = True
            return

        # Initialize the command
        self._current_command.initialize()


class ParallelCommandGroup(CommandGroup):
    """Run multiple commands in parallel.

    Each command will execute in its own dedicated thread. Unlike most
    other command groups, commands submitted here cannot share
    requirements.
    """

    _pool: ThreadPoolExecutor
    _finished: Barrier
    _sentinel: Event

    def __init__(  # noqa: WPS231
        self,
        name: Optional[str] = None,
        *commands: CommandType,
    ) -> None:
        """Creates a new :py:class:`~ParallelCommandGroup` instance.

        Args:
            name: The name of the command group. If not provided, the
                class name is used instead.
            commands: Variable length of commands to group.
        """  # noqa: RST203
        # Don't pass the commands to the parent class, we have to
        # implement custom checking of them here
        super().__init__(name)

        # Check for shared requirements
        for command in commands:
            for cmd in commands:
                if cmd == command:
                    continue
                if cmd.requirements.intersection(command.requirements):
                    raise ValueError(
                        "{cmd1} has shared requirements with {cmd2}".format(
                            cmd1=command,
                            cmd2=cmd,
                        ),
                    )
            self.add_requirements(*command.requirements)

        self._commands = commands
        self._sentinel = Event()

    def initialize(self) -> None:
        """Submit all commands to the thread pool."""
        self._sentinel.clear()
        self._pool = ThreadPoolExecutor(len(self._commands) + 1)
        self._finished = Barrier(len(self._commands) + 1)
        self._pool.map(
            self._execute,
            self._commands,
            itertools.repeat(self._finished),
            itertools.repeat(self._sentinel),
        )

    def execute(self) -> None:
        """Not implemented."""

    def is_finished(self) -> bool:
        """Check if all commands have finished."""
        # Do not catch BrokenPipeErrors
        # We want to ensure commands are interrupted in the event
        # something unexpected occurs
        return self._finished.n_waiting == len(self._commands)

    def end(self, interrupted: bool) -> None:
        """Wait for all commands to finish executing."""
        self._sentinel.set()
        self._finished.wait()
        self._pool.shutdown(wait=True)

    def _execute(
        self,
        command: CommandType,
        finished: Barrier,
        sentinel: Event,
    ) -> None:
        try:  # noqa: WPS229
            # Initialize the command
            command.initialize()

            # Run an event loop
            while True:
                # Check if the current command has finished
                if command.is_finished():
                    command.end(interrupted=False)
                    return

                # Check if the thread pool is shutting down
                if sentinel.is_set():
                    command.end(interrupted=True)
                    return

                # Execute the current command
                command.execute()

                time.sleep(Scheduler.instance.clock_speed)  # type: ignore
        except Exception:
            # Handle errors
            command.handle_exception(*sys.exc_info())
            command.end(interrupted=True)

            # Stop execution
            sentinel.set()
        finally:
            finished.wait()
