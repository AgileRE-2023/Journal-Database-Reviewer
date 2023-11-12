from django.http import HttpResponse
from django.shortcuts import render

def reviewer_list(request):
    return render(request, "reviewer/reviewer_list.html")

def submission(request):
    return render(request, "reviewer/index.html")

def upload(request):
    return render(request, 'reviewer/file_uploader.html')

def recommend(request):
    return render(request, 'reviewer/recommended_reviewers.html')