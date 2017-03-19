
import csv
import testerWithoutHeadaches
from testerWithoutHeadaches import totRes
with open('scores.csv', 'w') as csvfile:
    fieldnames = ['scores', "total"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({totRes})
    writer.writerow({'scores'' total'})
    writer.writerow({'scores': 'total'})
