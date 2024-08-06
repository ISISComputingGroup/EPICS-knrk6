from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedKnrk6(StateMachineDevice):
    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self.connected = True
        self.input_correct = True

        self.position = 1  # Home position
        self.valve_type = "VALVE 6"

    def _get_state_handlers(self):
        return {
            "default": DefaultState(),
        }

    def _get_initial_state(self):
        return "default"

    def _get_transition_handlers(self):
        return OrderedDict([])

    def reset(self):
        self._initialize_data()
