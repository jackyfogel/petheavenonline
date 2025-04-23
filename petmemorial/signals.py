import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PetMemorial
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=PetMemorial)
def notify_user_when_published(sender, instance, created, **kwargs):
    print("🐾 SIGNAL TRIGGERED!")  # 💥 This tells us the signal is firing

    if not created and instance.status == 'published':
        base_url = os.getenv('BASE_URL', 'http://localhost:8000')  # fallback to local
        memorial_url = f"{base_url}/memorials/{instance.slug}/"

        send_mail(
            subject='Your Pet Memorial is Now Live 🐾',
            message=f"Dear {instance.user.username},\n\n"
                    f"Your memorial for {instance.pet_name} has been approved and is now live.\n\n"
                    f"View it here:\n{memorial_url}\n\n"
                    f"Thank you for using Pet Heaven Online 🕊️",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.user.email],
            fail_silently=False,
        )
