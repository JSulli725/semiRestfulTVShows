from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Show

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
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return render(request, 'showForm.html')
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
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/{show_id}/edit')
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


