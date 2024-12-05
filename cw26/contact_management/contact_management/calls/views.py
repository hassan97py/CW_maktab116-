from django.shortcuts import render, redirect
from .forms import CallForm
from django.contrib import messages
import logging

from django.core.mail import send_mail

def send_confirmation_email(email):
    send_mail(
        'تایید تماس',
        'تماس شما با موفقیت ثبت شد.',
        '118mohammadi@gmail.com',
        [email],
        fail_silently=False,
    )


logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            call = form.save()
            logger.info(f'New call from {call.name}: {call.message}')
            messages.success(request, "تماس با موفقیت ثبت شد.")
            # ارسال ایمیل تایید (گام 6)
            send_confirmation_email(call.email)
            return redirect('contact')
        else:
            messages.error(request, "خطا در ثبت تماس. لطفا دوباره تلاش کنید.")
    else:
        form = CallForm()
    return render(request, 'calls/contact.html', {'form': form})
