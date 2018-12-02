import csv
from LinearRegression import run


filename = "abc.csv"
country = "countries.csv"

data = []
countries = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

with open(country, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for col in row:
            countries.append(col.strip())

X = [i for i in range(1, 59)]

model = []


def m():
    for i in range(1, len(data)):
        Y = []
        for p in data[i]:
            try:
                Y.append(int(p))
            except ValueError:
                Y.append(0)
        (b, m) = run(X, Y)
        model.append([b, m])
        i += 1
    return model


if __name__ == '__main__':
    m()
