from django.shortcuts import render
from .models import Member
from django.views import generic

# Create your views here.
def member_list(request):
    members = Member.objects.all()
    return render(request, 'gym/member_list.html', {'member_list': members})
class MemberListView(generic.ListView):
    model = Member
class MemberDetailView(generic.DetailView):
    model = Member