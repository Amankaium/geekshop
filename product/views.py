from django.shortcuts import render, HttpResponse
from .models import Vegetables

# Create your views here.
def homepage(request):
    # SELECT * FROM Vegetables
    products = Vegetables.objects.all()  # list
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context)


def pomidor(request):
    pomidor_object = Vegetables.objects.get(id=1)
    description = pomidor_object.description
    return HttpResponse(description)
