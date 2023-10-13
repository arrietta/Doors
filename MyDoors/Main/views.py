import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .telegram_bot import send_message_to_bot
from .models import Shape, Molding, Portal, Color, Door, Bevel


@login_required
def main(request):
    shapes = Shape.objects.all()
    portals = Portal.objects.all()
    bevels = Bevel.objects.all()
    moldings = Molding.objects.all()

    colors = Color.objects.all()
    doors = Door.objects.all()

    data = {
        "shapes": [{'id': shape.pk, "name": shape.name} for shape in shapes],
        'portals': [{'id': portal.pk, 'name': portal.name, 'shape': str(portal.shape)} for portal in portals],
        'bevels': [{'id': bevel.pk, 'name': bevel.name, 'shape': str(bevel.shape), 'portal': str(bevel.portal)} for
                   bevel in bevels],
        'moldings': [
            {'id': molding.pk, 'name': molding.name, 'shape': str(molding.shape), 'portal': str(molding.portal),
             'bevel': str(molding.bevel)}
            for molding in moldings],
        'color': [{'id': color.pk, 'name': color.name} for color in colors],
        'door': [{'id': door.pk, 'shape': str(door.shape), 'portal': str(door.portal), 'bevel': str(door.bevel),
                  'molding': str(door.molding),
                  'color': str(door.color), 'image': door.image.url, 'price': str(door.price), } for door in doors],

    }

    switch = request.GET.get('shape')

    if switch:
        shape = Shape.objects.get(pk=switch)
        portal = Portal.objects.get(pk=request.GET.get('portal'))
        bevel = Bevel.objects.get(pk=request.GET.get('bevel'))
        molding = Molding.objects.get(pk=request.GET.get('molding'))

        color = request.GET.get('color')

        message = f"Selected data: Shape={shape},  Portal={portal}, Bevel={bevel}, Molding={molding}, Color={color}"

        send_message_to_bot(message)

    data_1 = json.dumps(data);
    return render(request, 'main.html', {'data': data_1})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name for your home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
