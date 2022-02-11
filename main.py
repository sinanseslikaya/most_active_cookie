import sys
import csv
import datetime


def dateCheck():
    year = int(sys.argv[3][0:4])
    month = int(sys.argv[3][5:7])
    day = int(sys.argv[3][8:10])

    correctDate = None
    try:
        newDate = datetime.datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
        print("Invalid date")
        exit(1)
    return correctDate


def run():

    if len(sys.argv[1]) > 1 and dateCheck() == True:
        # filepath = sys.argv[1]
        try:
            with open(sys.argv[1]) as file:
                csvFile = csv.reader(file)
                cookies = {}

                for lines in csvFile:
                    if lines[1][0:10] == sys.argv[3]:  # checks if correct date
                        if str(lines[0]) not in cookies:
                            cookies[str(lines[0])] = 1
                        else:
                            cookies[str(lines[0])] += 1

                max_keys = [key for key, value in cookies.items() if value == max(cookies.values())]

                for key in max_keys:
                    print(key)

        except FileNotFoundError:
            print("File not found")
            exit(1)
    else:
        print('You need file path')
        exit(1)

#TODO CHECK runtime conditinos
run()
