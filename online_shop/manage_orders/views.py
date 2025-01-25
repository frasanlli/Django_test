from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from manage_orders.models import Items
from manage_orders.forms import Contact_form

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

def contact (request):

    recipient_list = [settings.NOTIFY_EMAIL]

    if request.method == "POST":

        my_form = Contact_form(request.POST)

        if my_form.is_valid():

            form_info = my_form.cleaned_data
            send_mail(
                subject = form_info['subject'],
                message = form_info['message'],
                from_email = form_info.get('email', ''),
                recipient_list = recipient_list)

            return render(request, "thanks.html")

    else:

        my_form = Contact_form()


    return render(request, "contact.html", {"form":my_form})