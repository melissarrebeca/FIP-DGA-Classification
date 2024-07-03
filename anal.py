import csv

from main import PentagonRegions


if __name__ == "__main__":

    right_under_40 = 0
    right_above_40 = 0

    wrongs_under_40 = 0
    wrongs_above_40 = 0

    for i in range(1, 15):
        file_path = f"./results/dataset_{i}/right.csv"
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            for row in csv_reader:

                h2_percentage = float(row[5])
                ch4_percentage = float(row[6])
                c2h6_percentage = float(row[7])
                c2h4_percentage = float(row[8])
                c2h2_percentage = float(row[9])

                if h2_percentage > 40 or ch4_percentage > 40 or c2h6_percentage > 40 or c2h4_percentage > 40 or c2h2_percentage > 40:
                    right_above_40 += 1
                else:
                    right_under_40 += 1

        file_path = f"./results/dataset_{i}/wrong_match.csv"
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            for row in csv_reader:

                h2_percentage = float(row[5])
                ch4_percentage = float(row[6])
                c2h6_percentage = float(row[7])
                c2h4_percentage = float(row[8])
                c2h2_percentage = float(row[9])

                if h2_percentage > 40 or ch4_percentage > 40 or c2h6_percentage > 40 or c2h4_percentage > 40 or c2h2_percentage > 40:
                    wrongs_above_40 += 1
                else:
                    wrongs_under_40 += 1



    print(f"Rights above 40: {right_above_40}")
    print(f"Rights under 40: {right_under_40}")
    print(f"Wrongs above 40: {wrongs_above_40}")
    print(f"Wrongs under 40: {wrongs_under_40}")
