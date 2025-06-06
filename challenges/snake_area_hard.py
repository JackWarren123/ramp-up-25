def snakefill(n):
    num_squares = n ** 2
    num_times_eaten = 0
    length = 1
    while True:
        length *= 2
        if length > num_squares:
            break
        num_times_eaten += 1
    return num_times_eaten
