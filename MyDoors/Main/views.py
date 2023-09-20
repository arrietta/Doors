from django.shortcuts import render
from .forms import DoorForm
from .telegram_bot import send_message_to_bot


def main(request):
    if request.method == 'POST':
        form = DoorForm(request.POST)
        if form.is_valid():
            try:
                message = f"Shape: {form.cleaned_data['shape']},\n Color: {form.cleaned_data['color']},\n" \
                          f" Molding: {form.cleaned_data['molding']},\n Portal: {form.cleaned_data['portal']}"

                send_message_to_bot(message)

                return render(request, 'main.html', {'form': form, 'success': True})
            except Exception as e:
                return render(request, 'main.html', {'form': form, 'error': str(e)})
    else:
        form = DoorForm()

    return render(request, 'main.html', {'form': form})
