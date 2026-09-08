select
    id,
    first_name,
    last_name
from {{ ref('stg_customers') }}
where id is not null
