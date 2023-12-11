from django.shortcuts import render, redirect
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from django.contrib import messages
from ..master.models import Editor, Reviewer, Journal, Scrapping
from django.utils import timezone
import requests

from apps.master.models import Reviewer

import json
import time
import asyncio
from asgiref.sync import sync_to_async
from apps.master.models import Reviewer

# Create your views here.
file = open("config.json")

config = json.load(file)

client = ElsClient(api_key=config["apikey"])


async def reviewerScrapping(request):
    reviewers = Reviewer.objects.filter(scopus_id__isnull=True)[:10]

    start = time.perf_counter()
    # response = await searchAuthorData(reviewers)
    reviewer_batches = await getReviewerBatches(reviewers, 5)

    tasks = []

    # Create and append tasks to the list
    for batches in reviewer_batches:
        task = asyncio.ensure_future(searchAuthorData(batches))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    end = time.perf_counter()

    if all(task.done() for task in tasks):
        return {"responses": sum(responses), "start": start, "end": end}
    else:
        return "loading"

    # messages.success(request, f"Updated {sum(responses)} Reviewer Scopus ID, takes {end - start:0.1f} seconds")

    # return redirect('dashboard')


def create_scrapping(request):
    scrapping = Scrapping(editor_id=request.user.editor_id)
    scrapping.save()
    return redirect('dashboard')


async def index(request):
    result = await reviewerScrapping(request)
    messages.success(
        request,
        f"Updated {result['responses']} Reviewer Scopus ID, takes {result['end'] - result['start']:0.1f} seconds",
    )
    return redirect("create scrapping")


async def searchAuthorData(reviewers: list[Reviewer]):
    success = 0
    for reviewer in reviewers:
        full_name = reviewer.name.split()
        first_name = full_name[0]
        last_name = " ".join(full_name[1 : len(full_name)])
        doc_srch = ElsSearch(
            f"authfirst({first_name}) and authlast({last_name})", "author"
        )
        doc_srch.execute(client, get_all=False)
        if doc_srch.results and doc_srch.results[0].get("error") is not None:
            scopus_id = None
        else:
            identifier = doc_srch.results[0]["dc:identifier"]
            scopus_id = identifier.split(":")[1]
            success += 1

        reviewer.scopus_id = scopus_id
        await reviewer.asave()

    return success


@sync_to_async
def getReviewerBatches(reviewers, offset):
    reviewer_batches = []
    batch_size = int(len(reviewers) / offset)
    for i in range(offset):
        batches = reviewers[i * batch_size : (i + 1) * batch_size - 1]
        reviewer_batches.append(batches)

    return reviewer_batches


def scraping_jurnal(request):
    reviewers = Reviewer.objects.all()
    editor = Editor.objects.get(editor_id=request.user.editor_id)
    client = ElsClient("6aed794eb40c72d178d4e29b1e64ae51")
    api_endpoint = "https://api.elsevier.com/content/abstract/scopus_id/"
    headers = {
        "X-ELS-APIKey": "6aed794eb40c72d178d4e29b1e64ae51",
        "Accept": "application/json",
    }

    counter = []
    for reviewer in reviewers[0:3]:
        author_author_id = reviewer.scopus_id
        # find scopus_id berdasarkan author_id
        if author_author_id:
            journal_search_query = "AU-ID({})".format(author_author_id)
            journal_search = ElsSearch(journal_search_query, "scopus")
            journal_search.execute(client)
            journal_results = journal_search.results
            # send request menggunakan scopus_id untuk melakukan scraping jurnal
            for result in journal_results:
                scopus_id = result.get("dc:identifier", "").split(":")[-1]
                if scopus_id:
                    response = requests.get(
                        f"{api_endpoint}{scopus_id}", headers=headers
                    )
                    if response.status_code == 200:
                        data = response.json()
                        abstract = (
                            data.get("abstracts-retrieval-response", {})
                            .get("coredata", {})
                            .get("dc:description")
                        )
                        title = (
                            data.get("abstracts-retrieval-response", {})
                            .get("coredata", {})
                            .get("dc:title")
                        )
                        doi = (
                            data.get("abstracts-retrieval-response", {})
                            .get("coredata", {})
                            .get("prism:doi")
                        )
                        # add Jurnal Data ke dalam model Journal
                        journal, created = Journal.objects.update_or_create(
                            title=title,
                            abstrack=abstract,
                            other=doi,
                        )

                        journal.reviewer.add(reviewer)
                        # Simpan journal_id dan reviewer_id pada detail_journal
                        # detail_entry = detail_journal.objects.create(
                        #     journal_id=journal,
                        #     reviewer_id=reviewer
                        # )
                        counter.append(1)
                        # detail_entry.save()
                    else:
                        print("")
    # Simpan log data scraping
    scraping_data = Scrapping(editor_id=editor.editor_id, isReviewerScrap = False)
    scraping_data.save()
    messages.success(request, f"Updated {len(counter)} Abstract")
    return redirect("dashboard")

    # return render(request, 'dashboard')
