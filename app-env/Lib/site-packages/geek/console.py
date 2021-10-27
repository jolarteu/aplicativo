from .generators import Generator
from .providers import MarvelProvider


def run():
    generator = Generator()
    generator.add_provider(MarvelProvider)

    print(generator.get_random_name())
