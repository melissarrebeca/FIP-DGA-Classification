import math
from dataclasses import dataclass
from enum import Enum


class Gas(Enum):
    C2H2 = "C2H2"
    H2 = "H2"
    C2H6 = "C2H6"
    CH4 = "CH4"
    C2H4 = "C2H4"



ANGLE_PER_GASES = {Gas.C2H2: 18, Gas.H2: 90, Gas.C2H6: 162, Gas.CH4: 234, Gas.C2H4: 306}


@dataclass
class Coordinates:
    x: float
    y: float


@dataclass
class GasPercentage:
    gas: Gas
    percentage: float


def calculate_polygon_vertices_coords(gas: Gas, percentage: float) -> Coordinates:
    cos = math.cos(math.radians(ANGLE_PER_GASES[gas]))
    sen = math.sin(math.radians(ANGLE_PER_GASES[gas]))

    x = percentage * cos
    y = percentage * sen

    return Coordinates(x, y)


if __name__ == "__main__":
    gases_percentages = [
        GasPercentage(Gas.C2H2, 10),
        GasPercentage(Gas.H2, 20),
        GasPercentage(Gas.C2H6, 30),
        GasPercentage(Gas.CH4, 40),
        GasPercentage(Gas.C2H4, 50),
    ]

    vertices_coods = {}

    for gas_percentage in gases_percentages:
        vertices_coods[gas_percentage.gas] = calculate_polygon_vertices_coords(gas_percentage.gas, gas_percentage.percentage)
