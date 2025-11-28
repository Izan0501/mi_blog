import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_admin():
    username = "admin"
    email = "admin@user.com"
    password = "admin123"

    if not User.objects.filter(username=username).exists():
        admin_user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            rol="admin" 
        )
        print(f"✅ Superusuario '{admin_user.username}' creado con éxito")
    else:
        print("⚠️ El superusuario ya existe")

if __name__ == "__main__":
    create_admin()
