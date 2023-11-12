from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Upload_Data, Editor, Reviewer
import pandas as pd
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import EditorForm


# Create your views here.
def index(request):
    return redirect("signin")


def inputDataOJSFile(request):
    if request.method == "POST" and request.FILES["excel_file"]:
        excel_file = request.FILES["excel_file"]

        # Cek file excel
        if not excel_file.name.endswith(".xlsx"):
            messages.error(request, "File harus berupa Excel (.xlsx)")
            return redirect("upload data OJS")

        editor = Editor.objects.get(pk=request.user.editor_id)

        # Baca file Excel dan ambil data yang dibutuhkan
        df = pd.read_excel(excel_file)
        selected_columns = ["name", "email", "scopus_id", "scholar_id", "other"]
        df = df[selected_columns]

        for index, row in df.iterrows():
            data_dict = row.to_dict()

            # Cek data dengan database
            duplicate_check = Reviewer.objects.filter(**data_dict).first()

            if not duplicate_check:
                reviewer = Reviewer(**data_dict)
                reviewer.save()

        # Simpan log uploads
        upload_data = Upload_Data(editor_id=editor, upload_date=timezone.now())
        upload_data.save()

        messages.success(request, "File Excel berhasil diunggah dan data disimpan.")
        return redirect("upload data OJS")

    return render(request, "reviewer/upload data OJS.html")


def signin(request):
    if request.method == "POST":
        form = EditorForm(data=request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # breakpoint()
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "master/signin.html",
                {"form": form, "error": "User not found"},
            )
    else:
        form = EditorForm()

    return render(request, "master/signin.html", {"form": EditorForm()})

def signout(request):
    logout(request)
