from django.shortcuts import render, HttpResponse
from .models import Feedback
from .forms import FeedbackCreateForm


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


def feedback_form_view(request):
    context = {}

    if request.method == "POST":
        feedback_create_form = FeedbackCreateForm(request.POST)
        feedback_create_form.save()
        return HttpResponse("Ваш отзыв принят! Спасибо!")

    feedback_create_form = FeedbackCreateForm()
    context["feedback_create_form"] = feedback_create_form
    return render(request, "core/feedback_form.html", context)

