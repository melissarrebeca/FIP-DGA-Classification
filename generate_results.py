import csv
import os
import shutil
from main import (
    GasPercentage,
    Gas,
    calcuate_polygon_area,
    calculate_all_centroid_positions_per_line,
    calculate_pentagon_region,
    calculate_polygon_centroid_coords,
    calculate_polygon_vertices_coords,
    PentagonRegions,
    calculate_relative_gas_percentage,
)


MAP_PENTAGON_REGIONS = {
    1: PentagonRegions.PD,
    2: PentagonRegions.D1,
    3: PentagonRegions.D2,
    4: PentagonRegions.T1,
    5: PentagonRegions.T2,
    6: PentagonRegions.T3,
}


if __name__ == "__main__":

    header = [
        "H2 ppm",
        "CH4 ppm",
        "C2H6 ppm",
        "C2H4 ppm",
        "C2H2 ppm",
        "H2 percentage",
        "CH4 percentage",
        "C2H6 percentage",
        "C2H4 percentage",
        "C2H2 percentage",
        "Centroid X",
        "Centroid Y",
        "Expected Region",
        "Matched Region",
    ]

    for i in range(16, 18):

        wrong_match_results = [header]

        not_discovered_results = [header]

        right_results = [header]

        file_path = f"./data/dataset_{i}.csv"

        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            count = 0

            for row in csv_reader:
                h2_value = float(row[0])
                ch4_value = float(row[1])
                c2h6_value = float(row[2])
                c2h4_value = float(row[3])
                c2h2_value = float(row[4])

                sum = h2_value + ch4_value + c2h6_value + c2h4_value + c2h2_value

                h2_percentage = calculate_relative_gas_percentage(h2_value, sum)
                ch4_percentage = calculate_relative_gas_percentage(ch4_value, sum)
                c2h6_percentage = calculate_relative_gas_percentage(c2h6_value, sum)
                c2h4_percentage = calculate_relative_gas_percentage(c2h4_value, sum)
                c2h2_percentage = calculate_relative_gas_percentage(c2h2_value, sum)

                right_pentagon_region = MAP_PENTAGON_REGIONS[int(float(row[5]))]

                gases_percentages = [
                    GasPercentage(Gas.C2H2, c2h2_percentage),
                    GasPercentage(Gas.H2, h2_percentage),
                    GasPercentage(Gas.C2H6, c2h6_percentage),
                    GasPercentage(Gas.CH4, ch4_percentage),
                    GasPercentage(Gas.C2H4, c2h4_percentage),
                ]

                gases_coords = []

                for gas_percentage in gases_percentages:
                    coords = calculate_polygon_vertices_coords(
                        gas_percentage.gas, gas_percentage.percentage
                    )
                    gases_coords.append(coords)

                area = calcuate_polygon_area(gases_coords)

                centroid_coords = calculate_polygon_centroid_coords(gases_coords, area)

                centroid_positions_per_line = calculate_all_centroid_positions_per_line(
                    centroid_coords
                )

                pentagon_region = calculate_pentagon_region(
                    centroid_coords, centroid_positions_per_line
                )

                if pentagon_region == None:
                    not_discovered_results.append(
                        [
                            h2_value,
                            ch4_value,
                            c2h6_value,
                            c2h4_value,
                            c2h2_value,
                            h2_percentage,
                            ch4_percentage,
                            c2h6_percentage,
                            c2h4_percentage,
                            c2h2_percentage,
                            centroid_coords.x,
                            centroid_coords.y,
                            right_pentagon_region,
                            "Not Discovered",
                        ]
                    )

                elif pentagon_region != right_pentagon_region:
                    wrong_match_results.append(
                        [
                            h2_value,
                            ch4_value,
                            c2h6_value,
                            c2h4_value,
                            c2h2_value,
                            h2_percentage,
                            ch4_percentage,
                            c2h6_percentage,
                            c2h4_percentage,
                            c2h2_percentage,
                            centroid_coords.x,
                            centroid_coords.y,
                            right_pentagon_region,
                            pentagon_region,
                        ]
                    )
                else:
                    right_results.append(
                        [
                            h2_value,
                            ch4_value,
                            c2h6_value,
                            c2h4_value,
                            c2h2_value,
                            h2_percentage,
                            ch4_percentage,
                            c2h6_percentage,
                            c2h4_percentage,
                            c2h2_percentage,
                            centroid_coords.x,
                            centroid_coords.y,
                            right_pentagon_region,
                            pentagon_region,
                        ]
                    )

            dir_path = f"./results/dataset_{i}"


            shutil.rmtree(dir_path)
            os.mkdir(dir_path)

            with open(f"{dir_path}/not_discovered.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(not_discovered_results)

            with open(f"{dir_path}/right.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(right_results)

            with open(f"{dir_path}/wrong_match.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(wrong_match_results)