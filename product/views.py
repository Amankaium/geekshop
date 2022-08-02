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


def vegetable_detail(request, id):
    vegetable = Vegetables.objects.get(id=id)
    context = {"vegetable": vegetable}
    return render(request, "product/vegetable_info.html", context)


def pomidor(request):
    # SELECT * FROM Vegetables WHERE id = 1;
    pomidor_object = Vegetables.objects.get(id=1)
    description = pomidor_object.description
    return HttpResponse(description)


def categories_view(request):
    categories = Category.objects.all()
    c = {"categories": categories}
    return render(request, "product/categories.html", c)


def category_detail(request, id):
    # SELECT * FROM Vegetables WHERE category = (SELECT id FROM Category WHERE id = id)
    category_object = Category.objects.get(id=id)
    vegetables_list = Vegetables.objects.filter(category=category_object)
    context = {"all_vegetables": vegetables_list}
    return render(request, "product/list.html", context)



