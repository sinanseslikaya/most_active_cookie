import sys
import csv
import datetime


def main():
    try:
        if sys.argv[2] == "-d":
            run_with_date()
        else:
            # could be changed in the future to accept different arguments
            print("Error: parameter", sys.argv[2], "not defined")
            exit(1)
    except IndexError:
        run()


def get_date():
    """
    This function ensures the date command line argument provided is valid
    :return: the date
    """
    try:
        cookie_date = datetime.datetime(int(sys.argv[3][0:4]), int(sys.argv[3][5:7]), int(sys.argv[3][8:10]))
        # create datetime object to ensure the validity of the date argument i.e. not a valid date -> ValueError
        cookie_date = cookie_date.strftime('%Y-%m-%d')  # formats into desired string form
    except ValueError:
        print("Error: invalid date argument")
        exit(1)
    return cookie_date


def args_provided(with_dates):
    """
    ensures all arguments provided in command line
    :param with_dates: bool param to decide if func should check for data param or not
    """
    if with_dates:
        try:
            x = len(sys.argv[1]) > 1
            y = len(sys.argv[3]) > 1
        except IndexError:
            print("Error: insufficient arguments")
            exit(1)
    else:
        try:
            x = len(sys.argv[1]) > 1
        except IndexError:
            print("Error: insufficient arguments")
            exit(1)


def run():
    """
    finds most active cookie in entire csv
    """
    args_provided(False)
    try:
        with open(sys.argv[1]) as file:
            csv_file = csv.reader(file)
            cookies = {}
            for lines in csv_file:
                if str(lines[0]) not in cookies:
                    cookies[str(lines[0])] = 1
                else:
                    cookies[str(lines[0])] += 1
            max_occurrences = max(cookies.values())

        for key in cookies.items():
            if key[1] == max_occurrences:
                print(key[0])
    except ValueError:
        # error arises from max() having an empty arg -> no cookies
        print("Error: no cookies")
        exit(1)
    except FileNotFoundError:
        print("Error: file not found")
        exit(1)


def run_with_date():
    """
    finds most active cookie on provided date
    """
    args_provided(True)
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
