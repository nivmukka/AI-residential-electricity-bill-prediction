import csv

#columns = ['abc','def']

with open('output.csv','wb') as outcsv:
	writer = csv.DictWriter(outcsv, fieldnames=["DOEID","REGIONC","DIVISION"])
	writer.writeheader()

	with open('test.csv','r') as incsv:
		reader = csv.DictReader(incsv)
		for row in reader:
			#print (row)
			writer.writerow({'DOEID':row['DOEID'], 'REGIONC':row['REGIONC'], 'DIVISION':row['DIVISION']})
			#writer.writerow({columns[0] : row[columns[0]]})