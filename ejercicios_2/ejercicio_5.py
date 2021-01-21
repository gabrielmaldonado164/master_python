"""
Ejercicio 5.
    -Crear una lista con el contenido de esta tabla:

    Accion  Aventura    Deportes
    GTA     Assasins    FIFA 21
    COD     CRASH       PES 21
    PUGB    THE WITCHER  NBA 21

    -Mostrar esta informacion ordenadamente
"""

tabla = [
    {
        'categoria':'ACCION',
        'juegos':['GTA','COD','PUGB']
    },

    {
        'categoria':'AVENTURA',
        'juegos':['ASSASINS','CRASH','THE WITCHER']
    },

    {
        'categoria':'DEPORTE',
        'juegos':['FIFA 21', 'PES 21', 'NBA 21']
    }
]

for categoria in tabla:
    print(f'--------------- {categoria["categoria"]}---------------------')
    for juego in categoria['juegos']:#Al ser juegos una lista, lo debo recorrer. Por eso en este apartado indico que itere con categoria y el subindice JUEGOS
        print(juego)