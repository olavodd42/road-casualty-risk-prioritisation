select
    cast(accident_index as varchar) as accident_index,
    cast(accident_year as integer) as accident_year,
    *
        exclude (accident_index, accident_year)
from {{ source('roadsafety', 'collisions') }}
