SELECT DISTINCT city FROM station
    WHERE left(city, 1) in ('a', 'e', 'i', 'o', 'u')
    AND right(city, 1) in ('a', 'e', 'i', 'o', 'u')
