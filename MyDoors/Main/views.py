from django.shortcuts import render, redirect
from .forms import DoorForm
from .telegram_bot import send_message_to_bot  # Импортируйте функцию отправки сообщения

def main(request):
    if request.method == 'POST':
        form = DoorForm(request.POST)
        if form.is_valid():
            try:
                # Формируйте сообщение с данными из формы
                message = f"Shape: {form.cleaned_data['shape']}, Color: {form.cleaned_data['color']}, Molding: {form.cleaned_data['molding']}, Portal: {form.cleaned_data['portal']}"

                # Отправьте сообщение в Telegram бота
                send_message_to_bot(message)

                # Добавьте код сохранения данных в базу данных, если это необходимо

                return render(request, 'main.html', {'form': form, 'success': True})
            except Exception as e:
                return render(request, 'main.html', {'form': form, 'error': str(e)})
    else:
        form = DoorForm()

    return render(request, 'main.html', {'form': form})
