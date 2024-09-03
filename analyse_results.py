import csv

from main import PentagonRegions

NEAR_REGIONS = {
    PentagonRegions.D1: [PentagonRegions.PD, PentagonRegions.D2, PentagonRegions.S, PentagonRegions.T1],
    PentagonRegions.D2: [PentagonRegions.D1, PentagonRegions.T1, PentagonRegions.T3],
    PentagonRegions.T2: [PentagonRegions.T3, PentagonRegions.T1],
    PentagonRegions.T3: [PentagonRegions.T2, PentagonRegions.D2, PentagonRegions.T1],
    PentagonRegions.T1: [PentagonRegions.T2, PentagonRegions.S],
    PentagonRegions.PD: [PentagonRegions.D1, PentagonRegions.S],
}

if __name__ == "__main__":

    rows_count = 0
    near_regions_count = 0

    near_regions_dict = {}
    not_near_regions_dict = {}


    for i in range(17, 18):
        file_path = f"./results/dataset_{i}/wrong_match.csv"
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            for row in csv_reader:

                expected = PentagonRegions[row[12].split(".")[1]]
                matched = PentagonRegions[row[13].split(".")[1]]

                h2_percentage = float(row[5])
                ch4_percentage = float(row[6])
                c2h6_percentage = float(row[7])
                c2h4_percentage = float(row[8])
                c2h2_percentage = float(row[9])

                key = f"{expected.value}->{matched.value}"


                if matched in NEAR_REGIONS[expected]:
                    if key not in near_regions_dict:
                        near_regions_dict[key] = 1
                    else:
                        near_regions_dict[key] += 1
                else:
                    if key not in not_near_regions_dict:
                        not_near_regions_dict[key] = 1
                    else:
                        not_near_regions_dict[key] += 1

    print("Near regiosn", near_regions_dict)
    print("Not near regions", not_near_regions_dict)
