-- display top 3 cities with highes temperature during july and august
SELECT `state`, MAX(`value`) as max_temp FROM temperatures
GROUP BY `state`
ORDER BY state ASC;
