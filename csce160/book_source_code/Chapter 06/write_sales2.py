# This program prompts the user for sales amounts
# and writes those amounts to the sales.txt file.
import sys


def get_number_of_days():
    num = 0
    while num <= 0:
        try:
            num = int(input('For how many days do you have sales? '))
        except ValueError:
            print("Enter a numeric value.")
    return num


def get_sales_file():
    sales_file = None
    while sales_file is None:
        sales_file_name = input("Enter the name of the sales file: ")
        try:
            sales_file = open(sales_file_name, 'w')
        except PermissionError:
            print(f"You don't have permission to overwrite this file: {sales_file_name}")
            print("Enter a different file name.")

    return sales_file


def get_sales_for_day(day_number):
    # Get the sales for a day.
    sales = float(input('Enter the sales for day #' + \
                        str(day_number) + ': '))
    return sales


def main():
    num_days = get_number_of_days()

    sales_file = get_sales_file()

    # Get the amount of sales for each day and write
    # it to the file.
    for day_num in range(1, num_days + 1):
        day_sales = get_sales_for_day(day_num)
        sales_file.write(str(day_sales) + '\n')

    # Close the file.
    sales_file.close()
    print(f'Data written to {sales_file.name}.')


if __name__ == '__main__':
    main()
