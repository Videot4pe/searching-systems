# [ракета/установка/бомбардировщик/…] + [несколько слов, но не глаголы, например «дальнего действия»] + [«несколько слов»]
from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import gram, type, Predicate
from yargy import Parser

class isCapital(Predicate):
  def __call__(self, token):
    return token.value[0].isupper()

class isNum(Predicate):
  def __call__(self, token):
    return any(char.isdigit() for char in token.value)

class isDefis(Predicate):
  def __call__(self, token):
    return '-' in token.value

IS_CAPITAL = isCapital()
DEFIS = isDefis()
NUM = isNum()

WeaponName = fact(
    'WeaponName',
    ['name']
)

NAME = rule(IS_CAPITAL, DEFIS, NUM)

WEAPON_NAME = rule(
  NAME.interpretation(WeaponName.name)
).interpretation(WeaponName)