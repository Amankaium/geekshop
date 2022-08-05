from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackCreateForm, SignInForm


# Create your views here.
def price_view(request):
    return render(request, "core/price.html")


def feedback_view(request):
    # ...
    if request.method == "POST":
        data = request.POST
        feedback = Feedback()
        feedback.first_name = data["first_name"]
        feedback.rating = int(data["rating"])
        feedback.text = data["text"]
        feedback.contact = data["contact"]
        feedback.save()
        return HttpResponse("Ваш отзыв принят! Спасибо!")


    return render(request, "core/feedback.html")


@login_required(login_url='http://localhost:8000/signin/')
def feedback_form_view(request):
    context = {}

    if request.method == "POST":
        feedback_create_form = FeedbackCreateForm(request.POST)
        feedback_create_form.save()
        return HttpResponse("Ваш отзыв принят! Спасибо!")

    feedback_create_form = FeedbackCreateForm()
    context["feedback_create_form"] = feedback_create_form
    return render(request, "core/feedback_form.html", context)


def sign_in(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user is not None:
            login(request, user)
            return redirect('homepage')
    context = {"auth_form": SignInForm()}
    return render(request, 'core/sign_in.html', context)


@login_required()
def logout_from_site(request):
    logout(request)
    return redirect('homepage')
