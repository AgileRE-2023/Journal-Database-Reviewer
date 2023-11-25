from django.shortcuts import render, redirect
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from django.contrib import messages
from ..master.models import Upload_Data, Editor, Reviewer, Journal, Scraping, detail_journal
import pandas as pd
from django.utils import timezone


# Create your views here.
def scraping_jurnal(request):
    if request.method == 'POST':
        reviewers = Reviewer.objects.all()
        editor = Editor.objects.get(pk=request.user.editor_id)

        # API Key
        client = ElsClient('6aed794eb40c72d178d4e29b1e64ae51')
        
        # read Jurnal data
        for reviewer in reviewers:
            author_scopus_id = reviewer.scopus_id
            journal_results = []
            
            if author_scopus_id:
                    # send request menggunakan scopus_id untuk melakukan scraping jurnal
                    journal_search_query = "AU-ID({})".format(author_scopus_id)
                    journal_search = ElsSearch(journal_search_query, 'scopus')
                    journal_search.execute(client)
                    journal_results = journal_search.results


                    # add Jurnal Data ke dalam model Journal
                    for result in journal_results:
                        journal = Journal(
                            title=result.get('dc:title'),
                            abstrack=result.get("dc:description"),
                            other=result.get('prism:doi', ''),
                        )
                        journal.save()


                    # Simpan journal_id dan reviewer_id pada detail_journal
                    detail_entry = detail_journal.objects.create(
                        journal_id=journal, 
                        reviewer_id=reviewer  
                    )
                    detail_entry.save()

            
        # Simpan log data scraping
        scraping_data = Scraping(editor_id=editor, scraping_date=timezone.now())
        scraping_data.save()

        # notifyUser
        messages.success(request, "Scraping Success")
        return redirect("dashboard")

    return render(request, "dashboard.html")