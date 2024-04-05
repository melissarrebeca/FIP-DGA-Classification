import math
from dataclasses import dataclass
from enum import Enum


class Gas(Enum):
    C2H2 = "C2H2"
    H2 = "H2"
    C2H6 = "C2H6"
    CH4 = "CH4"
    C2H24 = "C2H24"


ANGLES_PER_GAS = {Gas.C2H2: 18, Gas.H2: 90, Gas.C2H6: 162, Gas.CH4: 234, Gas.C2H24: 306}


@dataclass
class Coordinates:
    x: float
    y: float

@dataclass
class GasPercentage:
    gas: Gas
    percentage: float

def calculate_x_and_y_coords(gas: Gas, percentage: float) -> tuple[float, float]:
    cos = math.cos(math.radians(ANGLES_PER_GAS[gas]))
    sen = math.sin(math.radians(ANGLES_PER_GAS[gas]))

    x = percentage * cos
    y = percentage * sen

    return x, y


def calcuate_polygon_area(gases_coords: list[Coordinates]) -> float:
    sum = 0

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        sum += current_coords.x * next_coords.y - next_coords.x * current_coords.y

    return sum / 2


def calculate_polygon_centroid_coords(gases_coords: list[Coordinates], area: float) -> tuple[float, float]:
    x_sum = 0
    y_sum = 0

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        x_sum += (current_coords.x + next_coords.x) * (current_coords.x * next_coords.y - next_coords.x * current_coords.y)
        y_sum += (current_coords.y + next_coords.y) * (current_coords.x * next_coords.y - next_coords.x * current_coords.y)

    x = x_sum / (6 * area)
    y = y_sum / (6 * area)

    return x, y




if __name__ == "__main__":
    gases_percentages = [
        GasPercentage(Gas.C2H2, 10),
        GasPercentage(Gas.H2, 20),
        GasPercentage(Gas.C2H6, 30),
        GasPercentage(Gas.CH4, 40),
        GasPercentage(Gas.C2H24, 50),
    ]

    gases_coords = []

    for gas_percentage in gases_percentages:
        x, y = calculate_x_and_y_coords(gas_percentage.gas, gas_percentage.percentage)
        gases_coords.append(Coordinates(x, y))

    area = calcuate_polygon_area(gases_coords)
    x, y = calculate_polygon_centroid_coords(gases_coords, area)

    print(f"Centroid coords: ({x}, {y})")
