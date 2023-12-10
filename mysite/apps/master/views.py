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

        selected_columns = [
            "givenname.Element:Text",
            "familyname.Element:Text",
            "email",
            "review_interests",
        ]

        if not set(selected_columns).issubset(df.columns):
            messages.info(request, "Kolom pada file excel tidak sesuai")
            return redirect("upload data OJS")
        
        df["name"] = df["givenname.Element:Text"] + " " + df["familyname.Element:Text"]
        df["other"] = df["review_interests"]
        df = df[selected_columns]

        success_count = 0

        for index, row in df.iterrows():
            data_dict = row.to_dict()

            data_dict[
                "name"
            ] = f"{data_dict.get('givenname.Element:Text', '')} {data_dict.get('familyname.Element:Text', '')}"
            data_dict["other"] = f"{data_dict.get('review_interests', '')}"

            data_dict.pop("givenname.Element:Text", None)
            data_dict.pop("familyname.Element:Text", None)
            data_dict.pop("review_interests", None)

            # Cek data dengan database
            duplicate_check = Reviewer.objects.filter(**data_dict).first()

            # Menghitung jumlah data yang masuk
            if not duplicate_check:
                reviewer = Reviewer(**data_dict)
                reviewer.save()
                success_count += 1

        total_entries = len(df)

        # Simpan log uploads
        upload_data = Upload_Data(editor_id=editor, upload_date=timezone.now())
        upload_data.save()

        messages.success(
            request,
            f"File Excel berhasil diunggah dan data disimpan. Data yang berhasil dimasukkan: {success_count} dari {total_entries} total entri.",
        )
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


def csrf_failure(request, reason=""):
    if request.method == "POST":
        form = EditorForm(data=request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
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


def dashboard(request):
    return render(request, "master/dashboard.html")


def signout(request):
    logout(request)
