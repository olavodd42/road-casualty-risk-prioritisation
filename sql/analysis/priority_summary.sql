-- Starter prioritisation view; refine weights in docs/metric_definitions.md.
SELECT
    accident_year,
    road_type,
    SUM(number_of_casualties) AS casualties,
    COUNT(*) AS collisions
FROM collisions
GROUP BY accident_year, road_type
ORDER BY casualties DESC;
