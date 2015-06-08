# Create your views here.

from django.shortcuts import render_to_response

from common.models import Organisation
from visitors.models import Monthly

def monthly(request, organisation, year):
	org = Organisation.objects.get(id=organisation)

	visits = Monthly.objects.all().filter(organisation=org).filter(year=year).order_by('month')
	return render_to_response('visitors/monthly.html', { 'visits': visits })

	
