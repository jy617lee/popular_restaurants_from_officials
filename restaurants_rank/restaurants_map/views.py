from django.shortcuts import render, get_object_or_404
from .forms import EmailForm
from django.utils import timezone

# Create your views here.
def input_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.register_date = timezone.now()
            email.save()
        return render(request, 'restaurants_map/complete_email.html', {})
    else:
        form = EmailForm()
        return render(request, 'restaurants_map/input_email.html', {'form': form})
