import csv

from main import GasPercentage, Gas, calcuate_polygon_area, calculate_all_centroid_positions_per_line, calculate_pentagon_region, calculate_polygon_centroid_coords, calculate_polygon_vertices_coords, PentagonRegions


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

    wrong_results = [header]

    right_results = [header]

    for i in range(1, 13):
        file_path = f"./data/dataset_{i}.csv"

        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            for row in csv_reader:
                h2_percentage = float(row[0])
                ch4_percentage = float(row[1])
                c2h6_percentage = float(row[2])
                c2h4_percentage = float(row[3])
                c2h2_percentage = float(row[4])

                right_pentagon_region = MAP_PENTAGON_REGIONS[int(row[5])]

                gases_percentages = [
                    GasPercentage(Gas.C2H2, c2h2_percentage),
                    GasPercentage(Gas.H2, h2_percentage),
                    GasPercentage(Gas.C2H6, c2h6_percentage),
                    GasPercentage(Gas.CH4, ch4_percentage),
                    GasPercentage(Gas.C2H4, c2h4_percentage),
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

                if pentagon_region != right_pentagon_region:
                    wrong_results.append(
                        [h2_percentage, ch4_percentage, c2h6_percentage, c2h4_percentage, c2h2_percentage, centroid_coords.x, centroid_coords.y, right_pentagon_region, pentagon_region]
                    )
                else:
                    right_results.append(
                        [h2_percentage, ch4_percentage, c2h6_percentage, c2h4_percentage, c2h2_percentage, centroid_coords.x, centroid_coords.y, right_pentagon_region, pentagon_region]
                    )




        with open("./results/wrong_results.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(wrong_results)

        with open("./results/right_results.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(right_results)
