from random import randrange, shuffle

from django.core.management.base import BaseCommand
from questions.management.commands import _namegen
from questions.management.commands import _textgen
from questions.models import Profile, Question


class Command(BaseCommand):
    help = "Generates things"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass