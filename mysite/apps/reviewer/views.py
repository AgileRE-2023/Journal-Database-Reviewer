from django.http import HttpResponse
from django.shortcuts import render
from apps.master.models import Journal
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def reviewer_list(request):
    return render(request, "reviewer/reviewer_list.html")


def submission(request):
    if request.method == "POST":
        title_input = request.POST.get("title")
        abstract_input = request.POST.get("abstract")
        combined_input = "{}. {}".format(title_input, abstract_input)

        # Preprocessing data input
        lowercase = combined_input.lower()
        stop_words = set(stopwords.words("english"))
        split_sentences = lowercase.split()
        input_prepprocessed = " ".join(
            [word for word in split_sentences if word.lower() not in stop_words]
        )

        result = []
        all_journal = Journal.objects.all()
        for journal in all_journal:
            title_journal_db = journal.title
            abstract_journal_db = journal.abstrack
            author_journal_db = journal.reviewer
            combined_journal_db = "{}. {}".format(title_journal_db, abstract_journal_db)

            # Preprocessing data db
            lowercase_journal_db = combined_journal_db.lower()
            split_sentences_journal_db = lowercase_journal_db.split()
            data_journal_db_preprocessed = " ".join(
                [
                    word
                    for word in split_sentences_journal_db
                    if word.lower() not in stop_words
                ]
            )

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
                    "author_db": author_journal_db,
                    "similarity_mentah": similarity,
                    "similarity_bulat": int_similarity,
                    "similarity_koma": round_similarity,
                }
            )

        return render(
            request,
            "reviewer/journal-submission.html",
            {
                "title_input": title_input,
                "abstract_input": abstract_input,
                "result": result,
            },
        )
    return render(request, "reviewer/journal-submission.html")


def upload(request):
    return render(request, "reviewer/file_uploader.html")


def recommend(request):
    return render(request, "reviewer/recommended_reviewers.html")
