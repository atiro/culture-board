import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum

from visitors.models import Annual, Monthly
from common.models import Organisation

month_map = {
	'January': 1,
	'February': 2,
	'March': 3,
	'April': 4,
	'May': 5,
	'June': 6,
	'July': 7,
	'August': 8,
	'September': 9,
	'October': 10,
	'November': 11,
	'December': 12
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
			   real_years = []

			   for year in headers:
				real_years.append(year.split('/')[0])
		
			   for statsline in statsreader:
				month_string = statsline.pop(0)
				month = month_map[month_string]
				for index, stats in enumerate(statsline):
				  print "Saving " + stats + " for month: " + str(month)
				  monthly = Monthly(year = real_years[index], month = month, visitors=stats.replace(',', ''), organisation=org)
				  monthly.save()
				  print "Created monthly object"
			

			# Sum up annual

		  for org in Organisation.objects.all():
		    annual_visits = Monthly.objects.filter(organisation=org).values('year').annotate(visitors=Sum('visitors'))
		    for annual in annual_visits:
			print "Saving annual visits for year " + str(annual['year'])
			year = Annual(organisation=org, year=annual['year'], visitors=annual['visitors'])
			year.save()

			# Sum up total for each org
			

