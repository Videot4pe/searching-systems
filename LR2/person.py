from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import gram, type
# from natasha.grammars.name import NAME
from name import NAME

Person = fact(
    'Person',
    ['position', 'description', 'name']
)

DESCRIPTION = rule(
    and_(
        type('RU'),
        not_(
            or_(
                gram('VERB'),
                gram('INFN'),
                gram('PREP'),
                gram('CONJ'),
                gram('NPRO'),
            ),
        ),
    )
).repeatable(max=5).optional()

POSITION = morph_pipeline(['президент', 'генерал', 'министр'])

PERSON = rule(
    POSITION.interpretation(Person.position.inflected()),
    DESCRIPTION.interpretation(Person.description),
    NAME.interpretation(Person.name)
).interpretation(Person)
