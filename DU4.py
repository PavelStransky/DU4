import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()


def main():
    print("10 ľudí:")
    print(birthday_coincidence_probability(10))   #pravdepodobnosť 11% pre 10 ľudí
    
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

    for _ in range(100000):
        birthdays = np.sort(generator.integers(1, 366, size=group_size))
    
        lastBirthday = 0                   
        for birthday in birthdays:
            if birthday == lastBirthday:
                hits += 1
                break
            lastBirthday = birthday
    
    probability = hits / 100000
    error = np.sqrt(hits) / 100000

    return probability, error


if __name__ == "__main__":
    main()