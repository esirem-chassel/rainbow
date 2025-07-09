from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser

from gen.models import Flavor, Record
from gen.utils.generator import Generator

class Command(BaseCommand):
    help = "Add a new rainbow-able flavor"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('algo')
        parser.add_argument('maxlen', type=int)
        parser.add_argument('--salt', )

    def handle(self, *args: Any, **options: Any) -> str | None:
        flavor = Flavor()
        flavor.maxlen = options["maxlen"]
        flavor.salt = options["salt"] if options["salt"] else ''
        flavor.algo = options["algo"]
        flavor.name = f"A={flavor.algo}, L={flavor.maxlen}, S={'Y' if len(flavor.salt) else 'N'}"
        flavor.save()