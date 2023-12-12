from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time

class WaitForDBCommand(BaseCommand):
    help = "Waits for the database to become available before proceeding."

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for the database to become available...")

        while True:
            try:
                connections['default'].ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is now available."))
                break
            except OperationalError:
                self.stdout.write("Database is not available yet, retrying in 1 second...")
                time.sleep(1)