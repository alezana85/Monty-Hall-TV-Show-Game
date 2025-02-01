import random

def simulate_games(num_games=10000):
    """Simula varios juegos y retorna estadísticas"""
    switch_wins = 0
    stay_wins = 0
    
    for _ in range(num_games):
        # Inicializar puertas
        doors = ['Goat', 'Goat', 'Car']
        random.shuffle(doors)
        
        # Elección inicial aleatoria
        initial_choice = random.randint(0, 2)
        
        # Monty abre una puerta con cabra
        available_doors = [i for i in range(3) 
                         if i != initial_choice and doors[i] == 'Goat']
        monty_opens = random.choice(available_doors)
        
        # Probar ambas estrategias
        # Si no cambia de puerta
        if doors[initial_choice] == 'Car':
            stay_wins += 1
            
        # Si cambia de puerta
        switch_choice = next(i for i in range(3) 
                           if i != initial_choice and i != monty_opens)
        if doors[switch_choice] == 'Car':
            switch_wins += 1
    
    return {
        'cambiar_puerta': switch_wins/num_games * 100,
        'mantener_puerta': stay_wins/num_games * 100
    }

def monty_hall_game():
    global coche, cabra
    while True:
        # Inicializar puertas
        doors = ['Goat', 'Goat', 'Car']
        random.shuffle(doors)
        
        print("Bienvenido al juego de Monty Hall!")
        print("Hay tres puertas: 1, 2 y 3. Detrás de una de ellas hay un coche, y detrás de las otras dos hay cabras.")
        
        # Elección inicial del jugador
        choice = int(input("Elige una puerta (1, 2, 3): ")) - 1
        
        # Monty debe abrir una puerta con cabra que no sea la elegida por el jugador
        available_doors = []
        for i in range(3):
            if i != choice and doors[i] == 'Goat':
                available_doors.append(i)
        
        monty_choice = random.choice(available_doors)
        print(f"Monty abre la puerta {monty_choice + 1} y revela una cabra.")
        
        # Cambio de puerta
        switch = input("¿Quieres cambiar de puerta? (sí/no): ").lower() == 'sí'
        
        if switch:
            # La nueva elección debe ser la puerta que no fue ni la inicial ni la que abrió Monty
            choice = next(i for i in range(3) if i != choice and i != monty_choice)
        
        if doors[choice] == 'Car':
            print("¡Felicidades! ¡Has ganado el coche!")
            coche += 1
        else:
            print("Lo siento, has ganado una cabra.")
            cabra += 1
        
        retry = input("¿Quieres volver a intentarlo? (sí/no): ").lower()
        if retry == 'no':
            break

if __name__ == "__main__":
    print("¿Qué deseas hacer?")
    print("1. Jugar el juego")
    print("2. Ver simulación de probabilidades")
    choice = input("Elige una opción (1/2): ")
    
    if choice == "1":
        coche = 0
        cabra = 0
        while True:
            monty_hall_game()
            print(f"Veces que ganaste el coche: {coche}")
            print(f"Veces que ganaste una cabra: {cabra}")
            retry = input("¿Quieres jugar otra vez? (sí/no): ").lower()
            if retry == 'no':
                break
    else:
        while True:
            try:
                num_juegos = int(input("¿Cuántos juegos quieres simular? (mínimo 1,000): "))
                if num_juegos >= 1000:
                    break
                print("Por favor, ingresa un número mayor o igual a 1,000")
            except ValueError:
                print("Por favor, ingresa un número válido")
        
        resultados = simulate_games(num_juegos)
        print(f"\nResultados de la simulación de {num_juegos:,} juegos:")
        print(f"Probabilidad de ganar cambiando de puerta: {resultados['cambiar_puerta']:.1f}%")
        print(f"Probabilidad de ganar manteniendo la puerta: {resultados['mantener_puerta']:.1f}%")
