from game.components.power_ups.power_up import Power_Up
from game.utils.constants import HEART, HEART_TYPE


class HeartPowerUp(Power_Up):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)
