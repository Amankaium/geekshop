from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .models import Vegetables, Category
from .forms import VegetableCreateForm


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
    try:
        vegetable = Vegetables.objects.get(id=id)
        context = {"vegetable": vegetable}
        return render(request, "product/vegetable_info.html", context)
    except Vegetables.DoesNotExist:
        return HttpResponse("Такой страницы не существует", status=404)


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



def vegetable_add(request):
    context = {}

    if request.method == "GET":
        vegetable_form = VegetableCreateForm()
        context["vegetable_form"] = vegetable_form
        return render(request, 'product/vegetable_form.html', context)

    elif request.method == "POST":
        vegetable_form = VegetableCreateForm(request.POST)
        if vegetable_form.is_valid():
            new_vegetable = vegetable_form.save()
            return redirect(vegetable_detail, id=new_vegetable.id)
        else:
            return HttpResponse("Форма не валидна", status=400)


def vegetable_update(request, id):
    context = {}
    vegetable_object = Vegetables.objects.get(id=id)

    if request.method == "POST":
        vegetable_form = VegetableCreateForm(request.POST, instance=vegetable_object)
        if vegetable_form.is_valid():
            vegetable_object = vegetable_form.save()
            return HttpResponse("Данные сохранены")

    vegetable_form = VegetableCreateForm(instance=vegetable_object)
    context["vegetable_form"] = vegetable_form
    return render(request, 'product/vegetable_form.html', context)


def vegetable_delete(request, id):
    if request.method == "POST":
        vegetable_object = Vegetables.objects.get(id=id)
        vegetable_object.delete()
        return HttpResponse("Информация успешно удалена!")