import sys
import csv
import datetime


def get_date():
    """
    This function ensures the date command line argument provided is valid
    :return: the date
    """
    try:
        cookie_date = datetime.datetime(int(sys.argv[3][0:4]), int(sys.argv[3][5:7]), int(sys.argv[3][8:10]))
        cookie_date = cookie_date.strftime('%Y-%m-%d')  # formats into desired string form
    except ValueError:
        print("Error: invalid date argument")
        exit(1)
    return cookie_date


def args_provided():
    """
    ensures both filename and date args are provided in command line
    """
    try:
        x = len(sys.argv[1]) > 1
        y = len(sys.argv[3]) > 1
    except IndexError:
        print("Error: insufficient arguments")
        exit(1)


def main():
    args_provided()
    date = get_date()
    try:
        with open(sys.argv[1]) as file:
            csv_file = csv.reader(file)
            cookies = {}
            for lines in csv_file:
                if lines[1][0:10] == date:  # checks if correct date
                    if str(lines[0]) not in cookies:
                        cookies[str(lines[0])] = 1
                    else:
                        cookies[str(lines[0])] += 1
            max_occurrences = max(cookies.values())

            for key in cookies.items():
                if key[1] == max_occurrences:
                    print(key[0])

    except ValueError:
        # error arises from max() having an empty arg -> no cookies on the provided date
        print("Error: no cookies timestamped for given date")
        exit(1)
    except FileNotFoundError:
        print("Error: file not found")
        exit(1)

main()
