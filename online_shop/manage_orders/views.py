from django.shortcuts import render
from django.http import HttpResponse
from manage_orders.models import Items

# Create your views here.

def search_item(request):

    return render(request, "search_item.html")

def search(request):

    message: str = ""
    search_item: str = request.GET["itm"]

    if request.GET["itm"]:
        if len(request.GET["itm"]) <= 20:
            #This is a LIKE sql query
            message = f"Searched item: '{request.GET["itm"]}'"
            filter_item = Items.objects.filter(name__icontains=search_item)

            return render(request, "search_result.html", {"items": filter_item, "query": search_item})

        else:
            message = "The searched item is too long"

            return HttpResponse(message)
    else:
        message = "Empty search"

        return HttpResponse(message)
