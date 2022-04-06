"""
# Cheap dimmer switch

A dimmer switch controls the brightness of one or more bulbs.
You have a cheap dimmer switch, that its level goes from 5 to 15.

A bulb has a dynamic wattage. Its brightness is based on the wattage
and the level of the switch.

## Example

| Dimmer switch level | Bulb with 30 wattage | Bulb with 50 wattage | Bulb with 70 wattage |
| ------------------- | -------------------- | -------------------- | -------------------- |
| 5                   | 0 brightness         | 0 brightness         | 0 brightness         |
| 10                  | 15 brightness        | 25 brightness        | 35 brightness        |
| 12                  | ?  brightness        | ? brightness         | ? brightness         |
| 15                  | 30 brightness        | 50 brightness        | 70 brightness        |

## Outcome

Implement these entities so the test cases below pass.
"""

from typing import List


class Bulb:

    def __init__(self, wattage: int) -> None:
        self.wattage = wattage
        self.brightness = 0

    def set_brightness(self, level: float) -> None:
        self.brightness = level * self.wattage


class Dimmer:

    def __init__(self, *args) -> None:
        self.bulbs: List[Bulb] = list(args)
        self.min_level = 5
        self.max_level = 15
        self.level = self.min_level

    def set_level(self, level: int) -> None:
        if self.min_level <= level <= self.max_level:
            for bulb in self.bulbs:
                level_pct = (level - self.min_level) / (self.max_level - self.min_level)
                bulb.set_brightness(level_pct)
        else:
            raise ValueError(f"Level {level} is not valid.")


def test_bulbs_switch_off():
    bulb_30 = Bulb(wattage=30)
    bulb_50 = Bulb(wattage=50)
    bulb_70 = Bulb(wattage=70)
    dimmer = Dimmer(bulb_30, bulb_50, bulb_70)
    dimmer.set_level(5)
    assert bulb_30.brightness == 0
    assert bulb_50.brightness == 0
    assert bulb_70.brightness == 0


def test_bulbs_switch_half():
    bulb_30 = Bulb(wattage=30)
    bulb_50 = Bulb(wattage=50)
    bulb_70 = Bulb(wattage=70)
    dimmer = Dimmer(bulb_30, bulb_50, bulb_70)
    dimmer.set_level(10)
    assert bulb_30.brightness == 15
    assert bulb_50.brightness == 25
    assert bulb_70.brightness == 35


def test_bulbs_switch_almost_full():
    bulb_30 = Bulb(wattage=30)
    bulb_50 = Bulb(wattage=50)
    bulb_70 = Bulb(wattage=70)
    dimmer = Dimmer(bulb_30, bulb_50, bulb_70)
    dimmer.set_level(13)
    assert bulb_30.brightness == 24
    assert bulb_50.brightness == 40
    assert bulb_70.brightness == 56


def test_bulbs_switch_full():
    bulb_30 = Bulb(wattage=30)
    bulb_50 = Bulb(wattage=50)
    bulb_70 = Bulb(wattage=70)
    dimmer = Dimmer(bulb_30, bulb_50, bulb_70)
    dimmer.set_level(15)
    assert bulb_30.brightness == 30
    assert bulb_50.brightness == 50
    assert bulb_70.brightness == 70


test_bulbs_switch_off()
test_bulbs_switch_half()
test_bulbs_switch_almost_full()
test_bulbs_switch_full()

