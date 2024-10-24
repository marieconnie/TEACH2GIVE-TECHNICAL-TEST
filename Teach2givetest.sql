-- Query to display results for the year 2020, ordered by driver points.

SELECT driver_name AS Driver, 
       points AS Points,
       team_name AS Team
FROM race_results
WHERE year = 2020
ORDER BY points DESC;
