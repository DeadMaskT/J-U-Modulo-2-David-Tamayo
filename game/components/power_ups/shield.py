from game.components.power_ups.power_up import Power_Up
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield(Power_Up):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
