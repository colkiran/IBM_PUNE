import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    # colhead = next(emp_details)
    # print(*colhead)
    prtyTbl = PrettyTable(next(emp_details))

    for row in emp_details:
        # print(*row)
        prtyTbl.add_row(row)


print(prtyTbl)
