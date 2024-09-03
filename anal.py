import csv

from generate_results import MAP_PENTAGON_REGIONS



if __name__ == "__main__":

    r_regions = {
        "PentagonRegions.PD": {
            "right": 0,
            "wrong": 0
        },
        "PentagonRegions.T1":{            "right": 0,
            "wrong": 0},
        "PentagonRegions.T2": {            "right": 0,
            "wrong": 0},
        "PentagonRegions.T3": {            "right": 0,
            "wrong": 0},
        "PentagonRegions.D1": {            "right": 0,
            "wrong": 0},
        "PentagonRegions.D2": {            "right": 0,
            "wrong": 0},

        "PentagonRegions.S": {
            "right": 0,
            "wrong": 0
        }
    }

    for i in range(17, 18):

        # with open(f"./results/dataset_{i}/right.csv", "r") as file:
        #     csv_reader = csv.reader(file)

        #     next(csv_reader)


        #     for row in csv_reader:
        #         region = row[12]

        #         r_regions[region]["right"] += 1

        
        with open(f"./results/dataset_{i}/wrong_match.csv", "r") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)


            for row in csv_reader:
                region = row[12]

                r_regions[region]["wrong"] += 1


    print(r_regions)



