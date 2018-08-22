from django.shortcuts import render, get_object_or_404
from .forms import EmailForm
from django.utils import timezone

# Create your views here.
def input_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email_text = request.POST['input_email']
            email = form.save(commit=False)
            email.email_addr = email_text
            email.register_date = timezone.now()
            email.save()
        return render(request, 'restaurants_map/complete_email.html', {})
    else:
        form = EmailForm()
        return render(request, 'restaurants_map/input_email.html', {'form': form})

def dining_list(request):
    return render(request, 'restaurants_map/dining_list.html', {})

def official_report(request):
    return render(request, 'restaurants_map/official_report.html', {})

def secret_dinings(request):
    return render(request, 'restaurants_map/secret_dinings.html', {})
