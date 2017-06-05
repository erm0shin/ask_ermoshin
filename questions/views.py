from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

user_loged_in = False
username = "Тестовый пользователь"
popular_tags = ["Популярный тэг %d" % i for i in range(5)]
best_users = ["Активный пользователь %d" % i for i in range(5)]
text = """Guys, i have trouble with a moon park. 
Can't find the black-jack..."""
tags = ["Тэг %d" % i for i in range(5)]

default_context = {"user_loged_in": user_loged_in,
                   "username": username,
                   "popular_tags": popular_tags,
                   "best_users": best_users,
                   "tags": tags,
                   "text": text}


def paginate(request, type):
    if type == 'question':
        questions_number = 9
        questions_titles = ["Вопрос № %d" % (i + 1) for i in range(questions_number)]

        paginator = Paginator(questions_titles, 3)
        page = request.GET.get("page")

        try:
            questions_titles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            questions_titles = paginator.page(1)
            page = "1"
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            questions_titles = paginator.page(paginator.num_pages)
            page = str(paginator.num_pages)

        context = {"question_titles": questions_titles,
                   "range": range(5),
                   "num_pages": range(paginator.num_pages),
                   "current_page": int(page)}

        context.update(default_context)
    elif type == 'answer':
        answers_number = 9
        answers_titles = ["Ответ № %d" % (i + 1) for i in range(answers_number)]

        paginator = Paginator(answers_titles, 3)
        page = request.GET.get("page")

        try:
            answers_titles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            answers_titles = paginator.page(1)
            page = "1"
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            answers_titles = paginator.page(paginator.num_pages)
            page = str(paginator.num_pages)

        context = {"answer_titles": answers_titles,
                   "range": range(5),
                   "num_pages": range(paginator.num_pages),
                   "current_page": int(page)}

        context.update(default_context)

    return context


def new_questions(request):
    context = paginate(request, 'question')
    context["header"] = "New Questions"
    context["id"] = 1
    context["this_url"] = "new_questions"
    return render(request, "../templates/questions/new_questions.html", context)


def hot_questions(request):
    context = paginate(request, 'question')
    context["header"] = "Hot Questions"
    context["id"] = 2
    context["this_url"] = "hot_questions"
    return render(request, "../templates/questions/new_questions.html", context)


def find_by_tag(request):
    context = paginate(request, 'question')
    context["header"] = "Tag: "
    context["tag"] = "bla bla"
    context["id"] = 3
    context["this_url"] = "find_by_tag"
    return render(request, "../templates/questions/new_questions.html", context)


def question(request):
    context = paginate(request, 'answer')
    context["id"] = 4
    context["this_url"] = "question"
    return render(request, "../templates/questions/question.html", context)


def login(request):
    return render(request, "../templates/questions/login.html", default_context)


def signup(request):
    return render(request, "../templates/questions/signup.html", default_context)


def ask(request):
    return render(request, "../templates/questions/ask.html", default_context)


def settings(request):
    return render(request, "../templates/questions/settings.html", default_context)
