from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser

from gen.models import Flavor, Record
from gen.utils.generator import Generator

class Command(BaseCommand):
    help = "Generates a new batch of rainbows"

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Starting generating... ")
        flavors = Flavor.objects.all()
        shortestFlavor = 20
        for flavor in flavors:
            shortestFlavor = min(flavor.maxlen, shortestFlavor)
        # generates a random string that is not already generated, based on the shortest flavor ever
        g = Generator(shortestFlavor)
        exists = True
        while(exists):
            src = g.generateSrc()
            ls = Record.objects.filter(src=src)
            exists = 0 < ls.count()
            if exists:
                self.stdout.write(f"Src {src} exists, reloading... ")
        self.stdout.write(f"Generating {len(flavors)} flavors... ", ending='')
        for flavor in flavors:
            r = Record(src=src, flavor=flavor)
            r.res = g.generateTrg(flavor.algo, flavor.salt)
            r.save()
            self.stdout.write(".", ending='')
        self.stdout.write(" DONE.")