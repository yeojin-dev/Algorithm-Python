SELECT ROUND(s.lat_n, 4) median FROM station s
WHERE (SELECT COUNT(lat_n) FROM station WHERE lat_n < s.lat_n) = (SELECT COUNT(Lat_N) FROM station WHERE lat_n > s.lat_n);
