from django.shortcuts import render
from .models import Community
# Create your views here.
def org_homepage(request):
    a = Community.objects.all()
    return render(request, 'organizations/home.html',{'communities':a, 'test':a[0]})
