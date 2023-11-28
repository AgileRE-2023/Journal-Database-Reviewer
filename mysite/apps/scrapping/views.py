from django.shortcuts import render, redirect
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from django.contrib import messages
from ..master.models import Upload_Data, Editor, Reviewer, Journal, Scraping, detail_journal
import pandas as pd
from django.utils import timezone
import threading
import requests


# Create your views here.
def scraping_jurnal(request):
    if request.method == 'POST':
        reviewers = Reviewer.objects.all()
        editor = Editor.objects.get(editor_id=1)
        client = ElsClient('6aed794eb40c72d178d4e29b1e64ae51')

        api_endpoint = 'https://api.elsevier.com/content/abstract/scopus_id/'  

        headers = {
            'X-ELS-APIKey': '6aed794eb40c72d178d4e29b1e64ae51',
            'Accept': 'application/json'
        }

        for reviewer in reviewers:
            author_author_id = reviewer.scopus_id

            # find scopus_id berdasarkan author_id
            if author_author_id:
                journal_search_query = 'AU-ID({})'.format(author_author_id)
                journal_search = ElsSearch(journal_search_query, 'scopus')
                journal_search.execute(client)
                journal_results = journal_search.results

                # send request menggunakan scopus_id untuk melakukan scraping jurnal
                for result in journal_results:
                    scopus_id = result.get('dc:identifier', '').split(':')[-1] 
                    if scopus_id:
                       
                        response = requests.get(f"{api_endpoint}{scopus_id}", headers=headers)

                        if response.status_code == 200:
                            data = response.json()
                            abstract = data.get('abstracts-retrieval-response', {}).get('coredata', {}).get('dc:description')
                            title = data.get('abstracts-retrieval-response', {}).get('coredata', {}).get('dc:title')
                            doi = data.get('abstracts-retrieval-response', {}).get('coredata', {}).get('prism:doi')

                            # add Jurnal Data ke dalam model Journal
                            journal = Journal(
                                title=title,
                                abstrack=abstract,
                                other=doi,
                            )
                            journal.save()

                            # Simpan journal_id dan reviewer_id pada detail_journal
                            detail_entry = detail_journal.objects.create(
                                journal_id=journal, 
                                reviewer_id=reviewer  
                            )
                            detail_entry.save()
                        else:
                            print("")

        # Simpan log data scraping
        scraping_data = Scraping(editor_id=editor, scraping_date=timezone.now())
        scraping_data.save()

        messages.success(request, 'Scraping Success')
        return redirect('master/dashboard.html')

    return render(request, 'master/dashboard.html')