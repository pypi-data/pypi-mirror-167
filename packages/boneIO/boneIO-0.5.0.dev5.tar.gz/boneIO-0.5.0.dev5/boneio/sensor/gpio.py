"""GPIOInputButton to receive signals."""
import logging
from functools import partial

from boneio.const import BOTH, PRESSED, RELEASED
from boneio.helper import GpioBaseClass, edge_detect

_LOGGER = logging.getLogger(__name__)


class GpioInputSensor(GpioBaseClass):
    """Represent Gpio sensor on input boards."""

    def __init__(self, **kwargs) -> None:
        """Setup GPIO Input Button"""
        super().__init__(**kwargs)
        edge_detect(
            self._pin,
            callback=self._handle_press,
            bounce=self._bounce_time.total_milliseconds,
            edge=BOTH,
        )
        _LOGGER.debug("Configured sensor pin %s", self._pin)

    def _handle_press(self, pin: str) -> None:
        """Handle the button press callback"""
        # Ignore if we are in a long press
        if self.is_pressed:
            _LOGGER.debug("Pressed event on pin %s", self._pin)
            self._loop.call_soon_threadsafe(
                partial(self._press_callback, PRESSED, self._pin)
            )
        else:
            _LOGGER.debug("Released event on pin %s", self._pin)
            self._loop.call_soon_threadsafe(
                partial(self._press_callback, RELEASED, self._pin)
            )
