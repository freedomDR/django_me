from django.shortcuts import render
from django.http import HttpResponse
from .models import MatchInformation

# Create your views here.


def freedom(request):
    match_list = MatchInformation.objects.order_by('match_start_date')
    match_numbers = MatchInformation.objects.count()
    match_data = []
    for t in range(match_numbers):
        tmp = match_list[t].match_website.split('.')[1]
        match_data.append({'item':match_list[t], 'sort_id':t+1, 'website':tmp})
    context = {'test':'test', 'match_list': match_data, 'match_numbers': match_numbers}
    return render(request, 'info/index.html', context)

