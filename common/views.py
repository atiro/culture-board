# Create your views here.

from django.shortcuts import render_to_response

from common.models import Organisation

def organisations(request):
	orgs = Organisation.objects.all()
	return render_to_response('common/organisations.html', {'orgs': orgs })

