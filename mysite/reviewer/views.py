from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def submission(request):
    return render(request, "reviewer/index.html")

def upload(request):
    return render(request, 'reviewer/file_uploader.html')

def recommend(request):
    return render(request, 'reviewer/recommended_reviewers.html')