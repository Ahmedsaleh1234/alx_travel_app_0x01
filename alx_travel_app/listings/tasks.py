# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(booking_id):
    # Logic to get booking details and send email
    from .models import Booking  # Import here to avoid circular imports
    booking = Booking.objects.get(id=booking_id)
    send_mail(
        'Booking Confirmation',
        f'Thank you for your booking! Your booking ID is {booking.id}.',
        'from@example.com',
        [booking.user.email],
        fail_silently=False,
    )
