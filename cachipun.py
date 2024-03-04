import random

# opciones del Cachipún para el coputador
opciones = ["Piedra", "Papel", "Tijeras"] 
cpu = random.choice(opciones)

# Opción del Jugador
jugador = (input('¿Piedra, Papel o Tijeras?'))

if jugador.capitalize() not in (opciones):
    print('Argumento inválido: Debe ser piedra, papel o tijera')
else:
    print(f'\nTu jugaste {jugador}')
    print(f'Computador jugó {cpu}')
    
    if (jugador == cpu):
        print('Empataste !!')

    else:
        if (jugador == 'Piedra' and cpu == 'Tijeras') or (jugador == 'Papel' and cpu == 'Piedra') or (jugador == 'Tijeras' and cpu == 'Papel'):
            print('Ganaste !!')
        else:
            print('Periste !!')
