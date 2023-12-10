from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.master.models import Journal, Reviewer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Create your views here.
def reviewer_list(request):  
    reviewers = Reviewer.objects.order_by("name").all()
    page = Paginator(reviewers, 24)
    page_number = request.GET.get("page")
    page_obj = page.get_page(page_number)
    return render(request,"reviewer/reviewer_list.html",{'page_obj':page_obj})

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
    if request.method == "POST":
        title_input = request.POST.get("title")
        abstract_input = request.POST.get("abstract")
        combined_input = "{}. {}".format(title_input, abstract_input)

        # Preprocessing data input
        lowercase = combined_input.lower()
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words("english"))
        split_sentences = lowercase.split()
        input_stopwords = " ".join(
            [word for word in split_sentences if word.lower() not in stop_words]
        )
        input_tokenized = word_tokenize(input_stopwords)
        lemmatized_input = [lemmatizer.lemmatize(word) for word in input_tokenized]
        input_prepprocessed = " ".join(lemmatized_input)

        result = []
        all_journal = Journal.objects.all()
        for journal in all_journal:
            title_journal_db = journal.title
            abstract_journal_db = journal.abstrack
            author_journal_db = journal.reviewer.all().values()
            combined_journal_db = "{}. {}".format(title_journal_db, abstract_journal_db)

            # Preprocessing data db
            lowercase_journal_db = combined_journal_db.lower()
            lemmatizer = WordNetLemmatizer()
            split_sentences_journal_db = lowercase_journal_db.split()

            data_journal_db_stopwords = " ".join(
                [
                    word
                    for word in split_sentences_journal_db
                    if word.lower() not in stop_words
                ]
            )
            data_journal_db_tokenized = word_tokenize(data_journal_db_stopwords)
            lemmatized_data_journal_db = [
                lemmatizer.lemmatize(word) for word in data_journal_db_tokenized
            ]
            data_journal_db_preprocessed = " ".join(lemmatized_data_journal_db)

            # TF-IDF
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(
                [input_prepprocessed, data_journal_db_preprocessed]
            )

            # Count similarity
            similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            similarity = (similarity_matrix[0][1]) * 100
            int_similarity = int(similarity)
            round_similarity = round(similarity, 2)

            result.append(
                {
                    "title_db": title_journal_db,
                    "abstract_db": abstract_journal_db,
                    "author_db": author_journal_db[0],
                    "similarity_mentah": similarity,
                    "similarity_bulat": int_similarity,
                    "similarity_koma": round_similarity,
                }
            )
        sorted_result = sorted(
            result, key=lambda x: x["similarity_mentah"], reverse=True
        )

        top_ten_result = sorted_result[:10]
        grouped_author = {}

        for journal in top_ten_result:
            author = journal["author_db"]
            author_name = author["name"]
            if author_name not in grouped_author:
                grouped_author[author_name] = [journal]
            else:
                grouped_author[author_name].append(journal)
        # breakpoint()
        return render(
            request,
            "reviewer/recommended_reviewers.html",
            {
                "title_input": title_input,
                "abstract_input": abstract_input,
                "result": grouped_author,
            },
        )
    return render(request, "reviewer/journal-submission.html")


def upload(request):
    return render(request, "reviewer/file_uploader.html")

def recommend(request):
    return render(request, "reviewer/recommended_reviewers.html")
