from pathlib import Path
from random import Random
from typing import Union, Optional, List, Type

from .providers import Provider

generator_or_seed = Union[Path, int]


class Generator:
    def __init__(self, x: Optional[generator_or_seed] = None):
        if isinstance(x, Random):
            self._random = x
        else:
            self._random = Random(x)

        self._providers: List[Provider] = []
        self._adjectives: List[str] = [
            'admiring',
            'adoring',
            'affectionate',
            'agitated',
            'amazing',
            'angry',
            'awesome',
            'beautiful',
            'blissful',
            'bold',
            'boring',
            'brave',
            'busy',
            'charming',
            'clever',
            'cool',
            'compassionate',
            'competent',
            'condescending',
            'confident',
            'cranky',
            'crazy',
            'dazzling',
            'determined',
            'distracted',
            'dreamy',
            'eager',
            'ecstatic',
            'elastic',
            'elated',
            'elegant',
            'eloquent',
            'epic',
            'exciting',
            'fervent',
            'festive',
            'flamboyant',
            'focused',
            'friendly',
            'frosty',
            'funny',
            'gallant',
            'gifted',
            'goofy',
            'gracious',
            'great',
            'happy',
            'hardcore',
            'heuristic',
            'hopeful',
            'hungry',
            'infallible',
            'inspiring',
            'interesting',
            'intelligent',
            'jolly',
            'jovial',
            'keen',
            'kind',
            'laughing',
            'loving',
            'lucid',
            'magical',
            'mystifying',
            'modest',
            'musing',
            'naughty',
            'nervous',
            'nice',
            'nifty',
            'nostalgic',
            'objective',
            'optimistic',
            'peaceful',
            'pedantic',
            'pensive',
            'practical',
            'priceless',
            'quirky',
            'quizzical',
            'recursing',
            'relaxed',
            'reverent',
            'romantic',
            'sad',
            'serene',
            'sharp',
            'silly',
            'sleepy',
            'stoic',
            'strange',
            'stupefied',
            'suspicious',
            'sweet',
            'tender',
            'thirsty',
            'trusting',
            'unruffled',
            'upbeat',
            'vibrant',
            'vigilant',
            'vigorous',
            'wizardly',
            'wonderful',
            'xenodochial',
            'youthful',
            'zealous',
            'zen',
        ]

    def add_provider(self, provider_class: Type[Provider]):
        # noinspection PyTypeChecker
        self._providers.append(provider_class(self._random))

    def get_random_character(self) -> str:
        if not self._providers:
            raise RuntimeError('No provider added')

        return self._random.choice(self._providers).get_random_character()

    def get_random_name(self) -> str:
        if not self._providers:
            raise RuntimeError('No provider added')

        return '{}-{}'.format(self._random.choice(self._adjectives), self.get_random_character())
