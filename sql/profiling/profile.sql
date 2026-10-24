-- Basic row and completeness checks for the ingested collisions table.
SELECT
    COUNT(*) AS collision_count,
    COUNT(*) FILTER (WHERE accident_index IS NULL) AS missing_accident_index,
    COUNT(*) FILTER (WHERE accident_year IS NULL) AS missing_accident_year
FROM collisions;
