from LostObjectsAPI.models import LostObject
import random

lo = [
    'Laptop',
    'Arduino',
    'Celullar',
    'Tupper',
    'Mouse',
    'Lapicera',
    'Cargador C',
    'Cargador V8',
    'Cargador iPhone',
    'Cable HDMI',
    'Cable VGA',
    'Cable USB',
    'Memoria USB',
    'Memoria SD',
    'Cámara',
    'Cuadro',
    'Libro',
    'Portafolio',
    'Acualera',
    'Planos',
    'Audífonos',
]

for i in range(1, 12):
    num = random.randint(0, 20)
    p = LostObject(object_name=lo[num],
                   place_id=random.randint(1, 11),
                   img="/src/images/"+lo[num].lower().replace(" ", "-")+'.jpg',
                   important=True if num == 0 or num == 1 or num == 2 else False)
    p.save()
ulrs = [
    'lost_object/',
    'lost_object/<int:id>',
    'lost_object/places/',
    'lost_object/by_place/<int:id>',
    'lost_object/by_important',
    'lost_object/by_not_important',
    'lost_object/by_name/<str:obj_name>',
    'student/',
    'student/<int:register>',]
