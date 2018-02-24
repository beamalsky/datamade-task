# DataMade Task

A mini coding task completed for DataMade.

##The prompt

**Spreadsheet manipulation**

Download the Sunlight Foundation’s list of [legislators](http://unitedstates.sunlightfoundation.com/legislators/legislators.csv) in the United States. Write a script
that reads the spreadsheet as input, filters the rows based on specific criteria, and writes
out two spreadsheets as output. The criteria for the two spreadsheets should be:

1. First spreadsheet: All Democrats who are younger than 45 years old
2. Second spreadsheet: All Republicans who have Twitter accounts and YouTube
channels

For each row in the output, make sure to keep all of the columns from the original data
source.

##Setup

1. Make sure you have [Python 2.7+ installed]((https://www.python.org/downloads/).
2. Clone this repo.
3. Navigate to the directory in Terminal and run:
`python legisfilter.py `

The script should create two new spreadsheets with filtered data: "legislators_under_45.csv" and "legislators_on_social_media.csv"

-switch to dict
-switch to snake case