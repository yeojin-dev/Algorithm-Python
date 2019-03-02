SELECT country.continent, ROUND(AVG(city.population) - 0.5) FROM city JOIN country ON city.countrycode = country.code GROUP BY country.continent;
