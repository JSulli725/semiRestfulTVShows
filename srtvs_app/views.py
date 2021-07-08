from django.shortcuts import redirect, render
from .models import Show

# Create your views here.


def redirHome(request):
    return redirect('/shows')

def showForm(request):
    return render(request, 'showForm.html')

def allShows(request):
    context = {
        "allShows": Show.objects.all()
    }
    return render(request, 'allShows.html', context)

def addShow(request):
    this_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'] ,
        releaseDate = request.POST['releaseDate'],
        description = request.POST['description'])
    return redirect(f'/shows/{this_show.id}')

def grabShow(request, this_show):
    context = {
        "show": Show.objects.get(id=this_show)
        }
    return render(request, 'showInfo.html', context)

def editShow(request, show_id):
    context = {
        "edit_show":Show.objects.get(id=show_id)
    }
    return render(request, 'editShow.html', context)
    
def updateShow(request, show_id):
    updated_show = Show.objects.get(id=show_id)
    updated_show.title = request.POST['title']
    updated_show.network = request.POST['network']
    updated_show.releaseDate = request.POST['releaseDate']
    updated_show.description = request.POST['description']
    updated_show.save()
    return redirect(f'/shows/{updated_show.id}')

def destroyShow(request, show_id):
    destroy_show = Show.objects.get(id=show_id)
    destroy_show.delete()
    return redirect(f'/shows')


