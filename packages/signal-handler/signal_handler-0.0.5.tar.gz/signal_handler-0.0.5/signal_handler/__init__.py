import types
import signal
import traceback
from typing import Callable


class SignalHandler:
    def __init__(self, signals: tuple = (signal.SIGTERM, signal.SIGINT),
                 handler: Callable[[], None] = lambda: print('Received termination signal\n')):
        """
        Constructor
        :param signals: processed signals
        :type signals: tuple
        :param handler: signals handler
        :type handler: Callable[[], None]
        """
        self._terminated = False
        self._on_terminate = handler
        self._traceback = None
        self._message = None
        self._signal_name = None
        for sign in signals:
            signal.signal(sign, self._handler)

    def _handler(self, signum: int, frame: types.FrameType) -> None:
        """
        Processed signals handling
        :param signum: system signal
        :type signum: int
        :param frame: terminating frame
        :type frame: types.FrameType
        """
        try:
            self._signal_name = signal.Signals(signum).name
        except ValueError:
            self._signal_name = signum

        self._message = f"received signal {self._signal_name} ({signal.strsignal(signum)}), terminating"
        self._traceback = traceback.format_stack(frame)[0].replace('\n', ';')
        self._terminated = True
        if self._on_terminate:
            self._on_terminate()

    @property
    def terminated(self) -> bool:
        """
        Is application terminated

        :return: True if application terminated else False
        :rtype: bool
        """
        return self._terminated

    @property
    def on_terminate(self):
        """
        Returns method, called on application terminate

        :return: method, called on application terminate
        :rtype: Callable[[], None]
        """
        return self._on_terminate

    @on_terminate.setter
    def on_terminate(self, value):
        """
        Set on_terminate property

        :param value: method, called on application terminate
        :type value Callable[[], None]
        """
        self._on_terminate = value

    @property
    def message(self) -> str:
        """
        Termination message

        :return: True if application terminated else False
        :rtype: str
        """
        return self._message

    @property
    def traceback(self) -> str:
        """
        Termination traceback

        :return: traceback
        :rtype: str
        """
        return self._traceback

    @property
    def signal_name(self) -> str:
        """
        Signal name

        :return: signal name
        :rtype: str
        """
        return self._signal_name
