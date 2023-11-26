from django.contrib import messages
from django.shortcuts import redirect
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from apps.master.models import Reviewer

import json
import time
import asyncio
from asgiref.sync import sync_to_async
from apps.master.models import Reviewer

# Create your views here.
file = open('config.json')

config = json.load(file)

client = ElsClient(api_key=config['apikey'])

async def reviewerScrapping(request):
    reviewers = Reviewer.objects.filter(scopus_id__isnull=True)[:300]
    
    start = time.perf_counter()
    # response = await searchAuthorData(reviewers)
    reviewer_batches = await getReviewerBatches(reviewers, 6)
    responses = await asyncio.gather(
        # searchAuthorData(reviewers[0:50]),
        # searchAuthorData(reviewers[51:100]),
        # searchAuthorData(reviewers[101:149]),
        *[searchAuthorData(batches) for batches in reviewer_batches]
    )
    end = time.perf_counter()
    
    messages.success(request, f"Updated {sum(responses)} Reviewer Scopus ID, takes {end - start:0.1f} seconds")
    
    return redirect('dashboard') 

async def searchAuthorData(reviewers : list[Reviewer]):
    success = 0
    for reviewer in reviewers:
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

@sync_to_async
def getReviewerBatches(reviewers, offset):
    reviewer_batches = []
    batch_size = int(len(reviewers)/offset)
    for i in range(offset):
        batches = reviewers[i * batch_size : (i + 1) * batch_size - 1]
        reviewer_batches.append(batches)
    
    return reviewer_batches