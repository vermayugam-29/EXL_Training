import csv

def readAndwrite_csc():
    with open('data.csv', mode='r+' ,newline='') as file:
        writer = csv.writer(file)
        file.seek(0,2)
        writer.writerow(["Rakshit",22, "Male"])

        file.seek(0)
        reader = csv.reader(file)
        for row in reader:
            print(row)

        print("Data manipulated successfully")

readAndwrite_csc()