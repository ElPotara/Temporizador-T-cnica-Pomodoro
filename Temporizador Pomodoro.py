# temporizador_pomodoro.py

import time
import sys

def temporizador(minutos):
    """
    Inicia una cuenta regresiva en la terminal por una cantidad de minutos.
    """
    segundos = minutos * 60
    while segundos:
        mins, secs = divmod(segundos, 60)
        formato_tiempo = f'{mins:02d}:{secs:02d}'
        # \r permite que la línea se sobrescriba en la terminal
        sys.stdout.write(f'\rTiempo restante: {formato_tiempo} ')
        sys.stdout.flush()
        time.sleep(1)
        segundos -= 1
    print("\n¡Tiempo terminado!")

if __name__ == "__main__":
    print("--- Temporizador Pomodoro ---")
    try:
        while True:
            print("\nIniciando ciclo de trabajo de 25 minutos...")
            temporizador(25)
            print("¡Hora de un descanso de 5 minutos!")
            temporizador(5)

            continuar = input("¿Quieres empezar otro ciclo de Pomodoro? (s/n): ").lower()
            if continuar != 's':
                break
        print("¡Buen trabajo!")
    except KeyboardInterrupt:
        print("\n\nTemporizador cancelado. ¡Hasta la próxima!")