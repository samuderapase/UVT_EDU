from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from models import *


def index(request):
	return render_to_response ('index.html')

