import json
import uuid

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .telegram_bot import send_message_to_bot, send_photo_to_bot
from .forms import DoorForm
from .models import  Door, Basket


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
    doors = Door.objects.all()
    data = json.loads(serializers.serialize('json', doors))
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
        order = Basket.objects.get(pk=pk)
        order.delete()

    return JsonResponse({'message': 'Data saved deleted'})


@csrf_exempt
def save(request):
    if request.method == 'POST':
        data_to_save = json.loads(request.body)['data']
        for data in data_to_save:
            order = Basket.objects.get(pk=data['id'])
            order.count = data['count']
            order.save()

    return JsonResponse({'message': 'Data saved successfully'})
