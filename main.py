import math
from dataclasses import dataclass
from enum import Enum


class Gas(Enum):
    C2H2 = "C2H2"
    H2 = "H2"
    C2H6 = "C2H6"
    CH4 = "CH4"
    C2H24 = "C2H24"


class PentagonLines(Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"
    P6 = "P6"
    P7 = "P7"
    P8 = "P8"
    P9 = "P9"
    P10 = "P10"
    P11 = "P11"
    P12 = "P12"
    P13 = "P13"
    P14 = "P14"
    P15 = "P15"

class PentagonRegions(Enum):
    S = "S"
    PD = "PD"
    D1 = "D1"
    D2 = "D2"
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"

ANGLES_PER_GAS = {Gas.C2H2: 18, Gas.H2: 90, Gas.C2H6: 162, Gas.CH4: 234, Gas.C2H24: 306}


@dataclass
class Coordinates:
    x: float
    y: float


def calculate_line_angular_coeficient(a: Coordinates, b: Coordinates) -> float:
    return (b.y - a.y) / (b.x - a.x)


COORDS_PER_LINES = {
    PentagonLines.P1: {
        "A": Coordinates(-38, 12.4),
        "B": Coordinates(0, 40),
    },
    PentagonLines.P2: {
        "A": Coordinates(-35, 3.1),
        "B": Coordinates(-38, 12.4),
    },
    PentagonLines.P3: {
        "A": Coordinates(0, 1.5),
        "B": Coordinates(-35, 3.1),
    },
    PentagonLines.P4: {
        "A": Coordinates(-35, 3.1),
        "B": Coordinates(-23.5, 32.4),
    },
    PentagonLines.P5: {
        "A": Coordinates(-23.5, 32.4),
        "B": Coordinates(23.5, -32.4),
    },
    PentagonLines.P6: {
        "A": Coordinates(-6, -4),
        "B": Coordinates(-22.5, -32.4),
    },
    PentagonLines.P7: {
        "A": Coordinates(0, -3),
        "B": Coordinates(-6, -4),
    },
    PentagonLines.P8: {
        "A": Coordinates(-6, -4),
        "B": Coordinates(1, -32.4),
    },
    PentagonLines.P9: {
        "A": Coordinates(24.3, -30),
        "B": Coordinates(23.5, -32.4),
    },
    PentagonLines.P10: {
        "A": Coordinates(0, -3),
        "B": Coordinates(24.3, -30),
    },
    PentagonLines.P11: {
        "A": Coordinates(32, -6.1),
        "B": Coordinates(24.3, -30),
    },
    PentagonLines.P12: {
        "A": Coordinates(0, 1.5),
        "B": Coordinates(4, 16),
    },
    PentagonLines.P13: {
        "A": Coordinates(4, 16),
        "B": Coordinates(32, -6.1),
    },
    PentagonLines.P14: {
        "A": Coordinates(32, -6.1),
        "B": Coordinates(38, 12.4),
    },
    PentagonLines.P15: {
        "A": Coordinates(0, 40),
        "B": Coordinates(38, 12.4),
    },
}

ANGULAR_COEFICIENT_PER_LINE = {
    PentagonLines.P1: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P1]["A"], COORDS_PER_LINES[PentagonLines.P1]["B"]
    ),
    PentagonLines.P2: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P2]["A"], COORDS_PER_LINES[PentagonLines.P2]["B"]
    ),
    PentagonLines.P3: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P3]["A"], COORDS_PER_LINES[PentagonLines.P3]["B"]
    ),
    PentagonLines.P4: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P4]["A"], COORDS_PER_LINES[PentagonLines.P4]["B"]
    ),
    PentagonLines.P5: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P5]["A"], COORDS_PER_LINES[PentagonLines.P5]["B"]
    ),
    PentagonLines.P6: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P6]["A"], COORDS_PER_LINES[PentagonLines.P6]["B"]
    ),
    PentagonLines.P7: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P7]["A"], COORDS_PER_LINES[PentagonLines.P7]["B"]
    ),
    PentagonLines.P8: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P8]["A"], COORDS_PER_LINES[PentagonLines.P8]["B"]
    ),
    PentagonLines.P9: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P9]["A"], COORDS_PER_LINES[PentagonLines.P9]["B"]
    ),
    PentagonLines.P10: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P10]["A"],
        COORDS_PER_LINES[PentagonLines.P10]["B"],
    ),
    PentagonLines.P11: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P11]["A"],
        COORDS_PER_LINES[PentagonLines.P11]["B"],
    ),
    PentagonLines.P12: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P12]["A"],
        COORDS_PER_LINES[PentagonLines.P12]["B"],
    ),
    PentagonLines.P13: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P13]["A"],
        COORDS_PER_LINES[PentagonLines.P13]["B"],
    ),
    PentagonLines.P14: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P14]["A"],
        COORDS_PER_LINES[PentagonLines.P14]["B"],
    ),
    PentagonLines.P15: calculate_line_angular_coeficient(
        COORDS_PER_LINES[PentagonLines.P15]["A"],
        COORDS_PER_LINES[PentagonLines.P15]["B"],
    ),
}


@dataclass
class GasPercentage:
    gas: Gas
    percentage: float


def calculate_polygon_vertices_coords(gas: Gas, percentage: float) -> Coordinates:
    cos = math.cos(math.radians(ANGLES_PER_GAS[gas]))
    sen = math.sin(math.radians(ANGLES_PER_GAS[gas]))

    x = percentage * cos
    y = percentage * sen

    return Coordinates(x, y)


def calcuate_polygon_area(gases_coords: list[Coordinates]) -> float:
    sum = 0

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        sum += current_coords.x * next_coords.y - next_coords.x * current_coords.y

    return sum / 2


def calculate_polygon_centroid_coords(
    gases_coords: list[Coordinates], area: float
) -> Coordinates:
    x_sum = 0
    y_sum = 0

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        x_sum += (current_coords.x + next_coords.x) * (
            current_coords.x * next_coords.y - next_coords.x * current_coords.y
        )
        y_sum += (current_coords.y + next_coords.y) * (
            current_coords.x * next_coords.y - next_coords.x * current_coords.y
        )

    x = x_sum / (6 * area)
    y = y_sum / (6 * area)

    return Coordinates(x, y)


def calculate_centroid_position_based_on_line(
    angular_coeficient: float, centroid_coords: Coordinates, line_coords: Coordinates
):
    return (angular_coeficient * (centroid_coords.x - line_coords.x)) - (
        centroid_coords.y - line_coords.y
    )


def calculate_all_centroid_positions_per_line(centroid_coords: Coordinates):
    centroids_position_per_line = {}

    for pentagon_lines in PentagonLines:
        angular_coeficient = ANGULAR_COEFICIENT_PER_LINE[
            PentagonLines[pentagon_lines.name]
        ]
        position = calculate_centroid_position_based_on_line(
            angular_coeficient,
            centroid_coords,
            COORDS_PER_LINES[PentagonLines[pentagon_lines.name]]["A"],
        )

        centroids_position_per_line[PentagonLines[pentagon_lines.name]] = position

    return centroids_position_per_line


def calculate_pentagon_region(centroid_coords: Coordinates, position_per_line: dict[PentagonLines, float]):

    if (centroid_coords.x >= -1 and centroid_coords.x <= 0) and (
        centroid_coords.y >= 24.5 and centroid_coords.y <= 33
    ):
        return PentagonRegions.PD

    elif (centroid_coords.x == 0 and centroid_coords.y == 1.5) or (
        centroid_coords.x == 0 and centroid_coords.y == -3
    ):
        return PentagonRegions.D2

    elif (centroid_coords.y > 1.5 and centroid_coords.x < 0) and (
        position_per_line[PentagonLines.P1] >= 0
        and position_per_line[PentagonLines.P2] <= 0
        and position_per_line[PentagonLines.P3] < 0
    ):
        return PentagonRegions.S

    elif (centroid_coords.x <= 0 and centroid_coords.y <= 3.1) and (
        position_per_line[PentagonLines.P3] >= 0
        and position_per_line[PentagonLines.P4] <= 0
        and position_per_line[PentagonLines.P5] <= 0
        and position_per_line[PentagonLines.P6] > 0
        and position_per_line[PentagonLines.P7] < 0
    ):
        return PentagonRegions.T1

    elif (centroid_coords.x <= 0 and centroid_coords.y <= 3.1) and (
        position_per_line[PentagonLines.P3] > 0
        and position_per_line[PentagonLines.P4] < 0
        and position_per_line[PentagonLines.P5] < 0
        and position_per_line[PentagonLines.P6] < 0
    ):
        return PentagonRegions.T1

    elif (centroid_coords.x < 1) and (
        position_per_line[PentagonLines.P5] <= 0
        and position_per_line[PentagonLines.P6] >= 0
        and position_per_line[PentagonLines.P8] > 0
    ):
        return PentagonRegions.T2

    elif (centroid_coords.x >= -6) and (
        position_per_line[PentagonLines.P5] <= 0
        and position_per_line[PentagonLines.P7] >= 0
        and position_per_line[PentagonLines.P8] <= 0
        and position_per_line[PentagonLines.P9] <= 0
        and position_per_line[PentagonLines.P10] > 0
    ):
        return PentagonRegions.T3

    elif (centroid_coords.x > 0) and (
        position_per_line[PentagonLines.P10] <= 0
        and position_per_line[PentagonLines.P11] <= 0
        and position_per_line[PentagonLines.P12] >= 0
        and position_per_line[PentagonLines.P13] >= 0
    ):
        return PentagonRegions.D2

    elif (centroid_coords.x > 0) and (
        position_per_line[PentagonLines.P12] < 0
        and position_per_line[PentagonLines.P15] >= 0
    ):
        return PentagonRegions.D1

    elif (centroid_coords.x > 0) and (
        position_per_line[PentagonLines.P12] >= 0
        and position_per_line[PentagonLines.P13] < 0
        and position_per_line[PentagonLines.P14] <= 0
        and position_per_line[PentagonLines.P15] >= 0
    ):
        return PentagonRegions.D1

    return None

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
        coords = calculate_polygon_vertices_coords(gas_percentage.gas, gas_percentage.percentage)
        gases_coords.append(coords)

    area = calcuate_polygon_area(gases_coords)
    centroid_coords = calculate_polygon_centroid_coords(gases_coords, area)

    centroid_positions_per_line = calculate_all_centroid_positions_per_line(
        centroid_coords
    )

    pentagon_region = calculate_pentagon_region(centroid_coords, centroid_positions_per_line)

    print(centroid_coords)
    print(centroid_positions_per_line)

    print(f"Pentagon region: {pentagon_region}")

# Não está calculando corretamento, o que acredito que pode ser:
    # 1 - A notação da somatória na hora de calculcar a area do poligno e as coordenadas da centroide ta um pouco confusa
    # 2 - A ordem da delimitação dos pontos por linha do poligono
