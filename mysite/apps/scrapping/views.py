from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from apps.master.models import Reviewer

import json
from apps.master.models import Reviewer

# Create your views here.
file = open('config.json')

config = json.load(file)

client = ElsClient(api_key=config['apikey'])

async def reviewerScrapping(request):
    reviewers = Reviewer.objects.filter(scopus_id__isnull=True)[0:10]
    
    response = await searchAuthorData(reviewers)
    messages.success(request, f"Updated {response} Reviewer Scopus ID")
    
    return redirect('dashboard') 

async def searchAuthorData(reviewers : list[Reviewer]):
    success = 0
    async for reviewer in reviewers:
        full_name = reviewer.name.split()
        first_name = full_name[0]
        last_name = ' '.join(full_name[1: len(full_name)])
        doc_srch = ElsSearch(f"authfirst({first_name}) and authlast({last_name})", 'author')
        doc_srch.execute(client, get_all=False)
        if doc_srch.results and doc_srch.results[0].get('error') is not None:
            scopus_id = None 
        else:
            identifier = doc_srch.results[0]['dc:identifier']
            scopus_id = identifier.split(':')[1]
            success += 1
        
        reviewer.scopus_id = scopus_id
        await reviewer.asave()
    
    return success