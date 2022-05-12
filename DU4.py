import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()


def main():
    print("10 ľudí:")
    print(birthday_coincidence_probability(10))     #pravdepodobnosť 11% pre 10 ľudí
    
    pravdepodobnosť = 0
    group_size = 10
    while(pravdepodobnosť < 0.5):
        group_size += 1
        pravdepodobnosť = birthday_coincidence_probability(group_size)[0]

    print("\n")
    print(birthday_coincidence_probability(group_size))
    print(f"pravdepodobnost aspoň 50% je pre {group_size} ludi")


def birthday_coincidence_probability(group_size):
    hits = 0

    n = 100000  # Vždy, pokud se Vám nějaké číslo v programu opakuje, je dobré pro něj zavést proměnnou
                # (a pokud se Vám neopakuje, tak také).
                # Zamezí to zbytečným chybám, pokud toto číslo budete chtít změnit

    for _ in range(n):
        birthdays = np.sort(generator.integers(1, 366, size=group_size))
    
        lastBirthday = 0                   
        for birthday in birthdays:
            if birthday == lastBirthday:
                hits += 1
                break
            lastBirthday = birthday
    
    probability = hits / n
    error = np.sqrt(hits) / n

    return probability, error


if __name__ == "__main__":
    main()