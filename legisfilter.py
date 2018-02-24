#Generate two csv files from a list of Illinois legislators, one containing legislators under 45 and the other containing legislators with both a Twitter and YouTube account on file.

import csv
from datetime import date, datetime

#define starting data set
legislator_data = "legislators.csv"

#define files to write filtered data to
filtered_age = "legislators_under_45.csv"
filtered_SM = "legislators_on_social_media.csv"

#define age threshold and cutoff
age_threshold = 45
age_cutoff = date.today()


def calculate_age(birthdate, cutoff):
	try:
		#parse ISO 8601 time to datetime format
		b = datetime.strptime(birthdate, "%Y-%m-%d")
		#compare years directly and subtract one if birthday hasn't happened yet this year
		return cutoff.year - b.year - ((cutoff.month, cutoff.day) < (b.month, b.day))
	except ValueError:
		print("Was not able to calculate an age for the birthdate input " + birthdate + ". This may be an incorrectly formatted date.")


with open(legislator_data, "rb") as fin, open(filtered_age, "wb") as fout1, open(filtered_SM, "wb") as fout2:

	#read source file and instantiate two csv files to write to
	reader = csv.DictReader(fin)
	writer_age = csv.DictWriter(fout1, reader.fieldnames)
	writer_SM = csv.DictWriter(fout2, reader.fieldnames)

	#write headers into both new files
	writer_age.writeheader()
	writer_SM.writeheader()

	for row in reader:

		#filter for age threshold
		if ((calculate_age(row["birthdate"], age_cutoff) < age_threshold)):
			writer_age.writerow(row)

		#filter for social media presence
		if (row['twitter_id'] and row["youtube_url"]):
			writer_SM.writerow(row)

print("Filtering complete!")