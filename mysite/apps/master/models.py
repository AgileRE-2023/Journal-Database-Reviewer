from uuid import uuid4
from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import EditorManager


# Create your models here.
class Editor(AbstractBaseUser, PermissionsMixin):
    editor_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Editor"
        verbose_name_plural = "Editors"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Editor_detail", kwargs={"pk": self.pk})

    objects = EditorManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Upload_Data(models.Model):
    upload_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    editor_id = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Upload_Data"
        verbose_name_plural = "Upload_Datas"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Upload_Data_detail", kwargs={"pk": self.pk})


class Reviewer(models.Model):
    reviewer_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    scopus_id = models.CharField(max_length=255)
    scholar_id = models.CharField(max_length=255)
    other = models.JSONField()

    class Meta:
        verbose_name = "Reviewer"
        verbose_name_plural = "Reviewers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Reviewer_detail", kwargs={"pk": self.pk})
