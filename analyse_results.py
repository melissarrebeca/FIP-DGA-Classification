import csv

if __name__ == "__main__":
    file_path = f"./results/wrong_match.csv"

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        rows_count = 0
        rows_above_100 = 0

        for row in csv_reader:

            rows_count += 1

            h2_percentage = float(row[0])
            ch4_percentage = float(row[1])
            c2h6_percentage = float(row[2])
            c2h4_percentage = float(row[3])
            c2h2_percentage = float(row[4])

            min_value = min(h2_percentage, ch4_percentage, c2h6_percentage, c2h4_percentage, c2h2_percentage)
            max_value = max(h2_percentage, ch4_percentage, c2h6_percentage, c2h4_percentage, c2h2_percentage)

            if max_value > 100:
                rows_above_100 += 1

        print(f"Rows count: {rows_above_100}")
