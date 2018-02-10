from django.shortcuts import render
from .models import Team
from .models import Player
from .models import Golfers

from .forms import GolfSelectForm

from django.http import HttpResponseRedirect


# Create your views here.

def main_page(request):

    money = Team.objects.order_by('-score','name')
    return render(request, 'main/leaderboard.html', {'money': money})


def golfer_list(request):
    golflist = Golfers.objects.all()

    if request.method == "POST":
        form = GolfSelectForm(request.POST)
        if form.is_valid():
            golfers = form.save(commit=False)
            golfers.selected = form.cleaned_data.get('golferName')


            golfers.save()
            return HttpResponseRedirect("")

    else:
        form = GolfSelectForm()

    return render(request,'main/golferlist.html',{'golflist': golflist,'form': form})
