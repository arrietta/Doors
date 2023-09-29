from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .telegram_bot import send_message_to_bot
from .models import Shape, Molding, Portal, Color, Door


def get_moldings_by_shape(request):
    shape_id = request.GET.get('shape_id')
    moldings = Molding.objects.filter(shape_id=shape_id)
    data = [{'id': molding.id, 'name': molding.name} for molding in moldings]
    return JsonResponse(data, safe=False)


def get_portals_by_molding(request):
    molding_id = request.GET.get('molding_id')
    portals = Portal.objects.filter(molding_id=molding_id)
    data = [{'id': portal.id, 'name': portal.name} for portal in portals]
    return JsonResponse(data, safe=False)

def get_colors_by_portal(request):
    portal_id = request.GET.get('portal_id')
    colors = Color.objects.filter(portal_id=portal_id)
    data = [{'id': color.id, 'name': color.name} for color in colors]
    return JsonResponse(data, safe=False)



@login_required
def main(request):

    shapes = Shape.objects.all()
    moldings = Molding.objects.all()
    portals = Portal.objects.all()
    colors = Color.objects.all()  # Fetch color data from the Color model
    filtered_doors = Door.objects.all()

    switch = request.GET.get('shape')

    if switch != '' :

        shape = Shape.objects.get(pk=switch)
        molding = Molding.objects.get(pk=request.GET.get('molding'))
        portal = Portal.objects.get(pk= request.GET.get('portal'))
        color = request.GET.get('color')

        message = f"Selected data: Shape={shape}, Molding={molding}, Portal={portal}, Color={color}"

        send_message_to_bot(message)

        # Render the filtered doors and message in your template
        return redirect('home')
     # You can filter doors here based on form selections
    else:
        return render(request, 'main.html', {
            'shapes': shapes,
            'moldings': moldings,
            'portals': portals,
            'colors': colors,  # Pass the colors data to the template
            'filtered_doors': filtered_doors
        })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name for your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render()
