def can_two_movies_fill_flight(movie_lengths, flight_length):
    
    # Determine if two movie runtimes add up to the flight length
    movie_set = set()
    for movies in movie_lengths:
        diff = flight_length - movies
        if diff in movie_set:
            return True
        movie_set.add(movies)
    return False


print(can_two_movies_fill_flight([2, 4], 1)) #False

print(can_two_movies_fill_flight([2, 4], 6))

print(can_two_movies_fill_flight([3, 8], 6))

print(can_two_movies_fill_flight([3, 8, 3], 6))

print(can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7))

print(can_two_movies_fill_flight([4, 3, 2], 5))

print(can_two_movies_fill_flight([6], 6))

print(can_two_movies_fill_flight([], 2))