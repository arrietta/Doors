import json
import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .telegram_bot import send_message_to_bot, send_photo_to_bot
from .forms import DoorForm, SaveForm
from .models import Shape, Molding, Portal, Color, Door, Bevel, Basket


def identification(request):
    unique_id = request.session.get('unique_id', 'Not available')
    if not unique_id or unique_id == 'Not available':
        unique_id = str(uuid.uuid4())
        request.session['unique_id'] = unique_id
    else:
        unique_id = request.session.get('unique_id', 'Not available')
    return unique_id


def main(request):
    unique_id = identification(request)
    print(unique_id)
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

    if request.method == 'POST':
        form = DoorForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main.html', {'data': data, 'unique_id': unique_id})
    # result = Door.objects.get(pk=switch)
    # img = result.get_image()
    #
    # message = f"{result}"
    #
    # send_photo_to_bot(img)
    # send_message_to_bot(message)


def basket(request):
    unique_id = identification(request)
    orders = Basket.objects.filter(code=unique_id)

    return render(request, 'order.html', {'orders': orders})


@csrf_exempt
def delete(request, pk):
    if request.method == 'POST':
        basket = Basket.objects.get(pk=pk)
        basket.delete()

    return JsonResponse({'message': 'Data saved deleted'})


@csrf_exempt
def save(request):
    if request.method == 'POST':
        data_to_save = json.loads(request.body)['data']
        for data in data_to_save:
            basket = Basket.objects.get(pk=data['id'])
            basket.count = data['count']
            basket.save()

    return JsonResponse({'message': 'Data saved successfully'})
