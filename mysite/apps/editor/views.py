from django.shortcuts import render
from apps.master.models import Scrapping, Upload_Data
from apps.reviewer.views import upload

# Create your views here.
def dashboard(request):
  try:
    reviewer_scrap_date = Scrapping.objects.filter(isReviewerScrap = True).latest('scrapping_date')
    journal_scrap_date = Scrapping.objects.filter(isReviewerScrap = False).latest('scrapping_date')
    upload_data_date = Upload_Data.objects.latest("upload_date")
    context = {"reviewer" : reviewer_scrap_date, "journal" : journal_scrap_date, "upload" : upload_data_date}
  except:
    context = {"reviewer" : None, "journal" : None, "upload" : None}
    
  return render(request, 'editor/dashboard.html', context)