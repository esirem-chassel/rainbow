from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser

from gen.models import Flavor, Record
from gen.utils.generator import Generator

class Command(BaseCommand):
    help = "Generates a new batch of rainbows"
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--nb', default=1)
        parser.add_argument('--src')

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Starting generating... ")
        flavors = Flavor.objects.all()
        shortestFlavor = 20
        for flavor in flavors:
            shortestFlavor = min(flavor.maxlen, shortestFlavor)
        src = options["src"] if options["src"] else None
        nb = int(options["nb"]) if options["nb"] else 1
        if src and nb > 1: # overrides if src was given
            nb = 1
        for i in range(nb):
            g = Generator(shortestFlavor)
            if src == None:
                # generates a random string that is not already generated, based on the shortest flavor ever
                exists = True
                while(exists):
                    src = g.generateSrc()
                    ls = Record.objects.filter(src=src)
                    exists = 0 < ls.count()
                    if exists:
                        self.stdout.write(f"Src {src} exists, reloading... ")
            else:
                g.setSrc(src)
            self.stdout.write(f"Generating {len(flavors)} flavors ", ending='')
            for flavor in flavors:
                r = Record(src=src, flavor=flavor)
                r.res = g.generateTrg(flavor.algo, flavor.salt)
                r.save()
                self.stdout.write(".", ending='')
            src = None
            self.stdout.write("")
        self.stdout.write(" DONE.")