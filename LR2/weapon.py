# [ракета/установка/бомбардировщик/…] + [несколько слов, но не глаголы, например «дальнего действия»] + [«несколько слов»]
from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import gram, type

from weaponName import WEAPON_NAME

Weapon = fact(
    'Weapon',
    ['type', 'description', 'name']
)

ANY_RU_WORD = type('RU')
ANY_LATIN_WORD = type('LATIN')

DESCRIPTION = rule(
    and_(
        ANY_RU_WORD,
        or_(
            gram('NOUN'),
            gram('ADJF'),
            gram('NUMR'),
        ),
    )
).repeatable(min=0, max=4).optional().interpretation(Weapon.description)

TYPE = morph_pipeline(['ракета', 'установка', 'бомбардировщик'])

WEAPON = rule(
    TYPE.interpretation(Weapon.type.inflected()),
    DESCRIPTION.interpretation(Weapon.description),
    WEAPON_NAME.interpretation(Weapon.name)
).interpretation(Weapon)
