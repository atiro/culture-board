import csv
import os

from django.core.management.base import BaseCommand, CommandError

from visitors.models import Annual, Monthly
from common.models import Organisation

month_map = {
	'January': 0,
	'February': 1,
	'March': 2,
	'April': 3,
	'May': 4,
	'June': 5,
	'July': 6,
	'August': 7,
	'September': 8,
	'October': 9,
	'November': 10,
	'December': 11
}


# parse csv

class Command(BaseCommand):
	help = "Import monthly stats"

	def add_arguments(self, parser):
		parser.add_argument('--stats_dir', nargs=1, required=True)

	def handle(self, *args, **options):

		if len(options['stats_dir']) > 0:
			# Recurse through directory looking for CSV files

		  for root, dirs, files in os.walk(options['stats_dir'][0]):
		     for csvfile in files:
		       if csvfile.endswith(".csv"):
			 with open(root + '/' + csvfile, 'rb') as csvfile:
			   statsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
			   headers = statsreader.next()
			   organisation = headers.pop(0)
			   org, status = Organisation.objects.get_or_create(name=organisation)
			   for year in headers:
				real_year = year.split('/')[0]
		
			   for statsline in statsreader:
				month_string = statsline.pop(0)
				month = month_map[month_string]
				for stats in statsline:
				  print "Saving " + stats + " for month: " + str(month)
				  monthly = Monthly(year = real_year, month = month, visitors=stats.replace(',', ''), organisation=org)
				  monthly.save()
				  print "Created monthly object"
			

			# Sum up annual

		for org in Monthly.objects.group_by_org
		  for month in org.group_by_year
			sum  += month.visitors

			annual, status =Annual.objects.get_or_create(organisation=org, year= year, visitors=sum)

			annual.save()
			
# sum monthly for annual

	

