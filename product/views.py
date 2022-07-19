from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import Vegetables, Category


class AboutView(TemplateView):
    template_name = "about.html"


def about(request):
    return render(request, 'about.html')


# Create your views here.
def homepage(request):
    # SELECT * FROM Vegetables
    products = Vegetables.objects.all()  # list
    context = {"all_vegetables": products}
    return render(request, "product/list.html", context)


def pomidor(request):
    # SELECT * FROM Vegetables WHERE id = 1;
    pomidor_object = Vegetables.objects.get(id=1)
    description = pomidor_object.description
    return HttpResponse(description)


def categories_view(request):
    categories = Category.objects.all()
    c = {"categories": categories}
    return render(request, "product/categories.html", c)



