import csv

num_records = 0
column_index = 0
comparison_string = "single malt scotch"
f = open("iowa-liquor-sample.csv", "r")
try:
	reader = csv.reader(f)
	headers = reader.next()
	for i, header in enumerate(headers):
		if header == "CATEGORY NAME":
			column_index = i
	for row in reader:
		if comparison_string in row[column_index].lower():
			num_records += 1
	print "Number of records = %d" % num_records
finally:
	f.close()
