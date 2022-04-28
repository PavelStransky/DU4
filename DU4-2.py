import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()

def main():
    tries = 100000
    dimensions=range(1, 15)
    maxobjem = 0
    dimenzia = 0

    result = np.asarray([volume(tries, dimension) for dimension in dimensions])

    for dimension in dimensions:
        volumes = volume(tries, dimension)
        ball_volume = volumes[0]
        chyba = volumes[1]
        hits = volumes[2]
        print(f"V{dimension}={ball_volume} += {chyba} (Počet zásahov: {hits})")
        if(ball_volume > maxobjem):
            maxobjem = ball_volume
            dimenzia = dimension

    print("\n")
    print(f"Najvacsi objem: {maxobjem} a ten je pre dimenziu {dimenzia} ")

    volumes = result[:, 0]
    errors = result[:, 1]

    plt.errorbar(dimensions, volumes, yerr=errors)
    plt.title("Objem $d$-rozmernej jednotkovej gule")
    plt.xlabel("$d$")
    plt.ylabel("$V$")
    plt.show()
    

def volume(tries, dimension):
    hits = 0
    
    for _ in range(tries):
        random_vector = 2 * generator.random(dimension) - 1
        norm = np.linalg.norm(random_vector)
        
        if norm <= 1:
            hits += 1

    cube_volume = 2**dimension
    ball_volume = hits / tries * cube_volume
    error = np.sqrt(hits) / tries * cube_volume


    return ball_volume, error, hits


if __name__ == "__main__":
    main()