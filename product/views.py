from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView
from .models import Vegetables, Category
from .forms import VegetableCreateForm
from core.decorators import should_be_staff


class AboutView(TemplateView):
    template_name = "about.html"


def about(request):
    return render(request, 'about.html')


# Create your views here.
# model, template
# def homepage(request):
#     # SELECT * FROM Vegetables
#     products = Vegetables.objects.all()  # list
#     context = {"all_vegetables": products}
#     return render(request, "product/list.html", context)


class VegetablesListView(ListView):
    model = Vegetables
    template_name = "product/list.html"
    # queryset = Vegetables.objects.filter(is_avialable=True)

    def get_queryset(self):
        return Vegetables.objects.filter(is_avialable=True)

# def categories_view(request):
#     categories = Category.objects.all()
#     c = {"categories": categories}
#     return render(request, "product/categories.html", c)


class CategoryListView(ListView):
    model = Category
    template_name = "product/categories.html"


# def vegetable_detail(request, id):
#     try:
#         vegetable = Vegetables.objects.get(id=id)
#         context = {"vegetable": vegetable}
#         return render(request, "product/vegetable_info.html", context)
#     except Vegetables.DoesNotExist:
#         return HttpResponse("Такой страницы не существует", status=404)


class VegetableDetailView(DetailView):
    model = Vegetables
    template_name = "product/vegetable_info.html"


# def category_detail(request, id):
#     # SELECT * FROM Vegetables WHERE category = (SELECT id FROM Category WHERE id = id)
#     category_object = Category.objects.get(id=id)
#     vegetables_list = Vegetables.objects.filter(category=category_object)
#     context = {"all_vegetables": vegetables_list}
#     return render(request, "product/list.html", context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "product/list.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse("hello")

    def get_object(self):
        return Category.objects.get(id=self.kwargs["id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Vegetables.objects.filter(category=self.object)
        return context


@login_required(login_url='http://localhost:8000/signin/')
# @permission_required("product.add_vegetable")
@should_be_staff
def vegetable_add(request):
    # if not request.user.is_staff:
    #     return HttpResponse("У вас нет доступа!", status=403)

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