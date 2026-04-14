WITH CrimsonSales AS (
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
)

SELECT name
FROM sales_person
WHERE sales_id NOT IN (
    SELECT sales_id 
    FROM CrimsonSales
);