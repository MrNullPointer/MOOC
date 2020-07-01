def can_two_movies_fill_flight(movie_lengths, flight_length):
    
    # Determine if two movie runtimes add up to the flight length
    checked_movies = set()

    for movie in movie_lengths:
        if (flight_length - movie) in checked_movies:
            return True
        checked_movies.add(movie)
        
    return False


print(can_two_movies_fill_flight([2, 4], 1)) #False

print(can_two_movies_fill_flight([2, 4], 6))

print(can_two_movies_fill_flight([3, 8], 6))

print(can_two_movies_fill_flight([3, 8, 3], 6))

print(can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7))

print(can_two_movies_fill_flight([4, 3, 2], 5))

print(can_two_movies_fill_flight([6], 6))

print(can_two_movies_fill_flight([], 2))