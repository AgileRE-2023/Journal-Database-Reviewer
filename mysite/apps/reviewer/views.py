from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.master.models import Reviewer  

# Create your views here.
def reviewer_list(request):  
    reviewers = Reviewer.objects.all()  
    return render(request,"reviewer/reviewer_list.html",{'reviewers':reviewers})

def add(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        # institution = request.POST.get('institution')
        scopus_id = request.POST.get('scopus_id')
        scholar_id = request.POST.get('scholar_id')

        reviewer = Reviewer(
            name=fullname,
            email=email,
            # institution=institution,
            scopus_id=scopus_id,
            scholar_id=scholar_id
        )

        reviewer.save()
        return redirect('reviewer:reviewer_list') 


def edit(request):
    if request.method == 'POST':
        reviewer_id = request.POST.get('reviewer_id')
        reviewer = Reviewer.objects.get(reviewer_id=reviewer_id)
        # breakpoint()
        reviewer.name = request.POST.get('name')
        reviewer.email = request.POST.get('email')
        # reviewer.institution = request.POST.get('institution')
        reviewer.scopus_id = request.POST.get('scopus_id')
        reviewer.scholar_id = request.POST.get('scholar_id')

        reviewer.save()

        return redirect('reviewer:reviewer_list')


def delete(request, id):
    employee = Reviewer.objects.get(id=id)  
    employee.delete()  
    return redirect("/") 

def submission(request):
    return render(request, "reviewer/index.html")

def upload(request):
    return render(request, 'reviewer/file_uploader.html')

def recommend(request):
    return render(request, 'reviewer/recommended_reviewers.html')

# def parseUUID(uuid):
#     original_string = uuid
#     modified_string = original_string.replace("-", "")
#     return modified_string
