from django.shortcuts import render
from django.shortcuts import redirect,HttpResponse
from .forms import AddItem
from .models import Item
import re


# Create your views here.
def delete_items(request):
    if request.method == "POST":
        ids = request.POST.get("the_post").split(",")
        for item_id in ids:
            Item.objects.filter(id=item_id).delete()
        return HttpResponse('psted')
    else:
        return HttpResponse("geted")


def main_page(request):
    if request.user.is_authenticated:
        errors = []
        form = AddItem(request.POST or None)
        if form.is_valid():
            new_item = Item(description=form.cleaned_data.get("item_name"), author=request.user)
            try:
                new_item.save()
            except Exception as e:
                errors.append(e)
        context = {
            "items": Item.objects.all(),
            "user": request.user,
            "form": form,
            "errors": errors
        }
        return render(request, 'index.html', context)
    else:
        return redirect('/login')
