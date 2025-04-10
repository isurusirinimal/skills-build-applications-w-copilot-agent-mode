import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_app.models import *  # Import your models here

# Add your test data population logic here
def populate():
    # Example: Creating a user
    # user = User.objects.create(username="testuser", email="testuser@example.com")
    # user.save()

    print("Database populated with test data.")

if __name__ == "__main__":
    print("Starting database population script...")
    populate()
