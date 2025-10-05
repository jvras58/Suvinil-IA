import factory

from app.api.paint.paint_enums import (
    Environment,
    FinishType,
    PaintLine,
    SurfaceType,
)
from app.models.paint import Paint


class PaintFactory(factory.Factory):
    class Meta:
        model = Paint

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('color_name')
    color = factory.Faker('color_name')
    surface_type = factory.Faker(
        'random_element', elements=list(SurfaceType)
    )
    environment = factory.Faker(
        'random_element', elements=list(Environment)
    )
    finish_type = factory.Faker(
        'random_element', elements=list(FinishType)
    )
    features = factory.Faker('sentence', nb_words=10)
    paint_line = factory.Faker(
        'random_element', elements=list(PaintLine)
    )
    created_by_user_id = factory.Sequence(lambda n: n)
    audit_user_ip = factory.Faker('ipv4')
    audit_user_login = factory.Faker('user_name')
