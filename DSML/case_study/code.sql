==========
Question 1
==========

---------
Part 1.1
---------
/*
Data type of columns in a table
*/

-- Uploading the data 
COPY target.public.customers FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/customers.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.geolocation FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/geolocation.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.order_items FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/order_items.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.order_reviews FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/order_reviews.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV ACCEPTINVCHARS DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.orders FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/orders.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.payments FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/payments.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.products FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/products.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

COPY target.public.sellers FROM 's3://dsml-redshift-dataset-us-east-1/dataset/target/sellers.csv' IAM_ROLE 'arn:aws:iam::507922848584:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T165829' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'

--- Data types of columns 

-- Product column 

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'products';

-- Orders column 

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'orders';


---------
Part 1.2
---------
/*
Time period for which the data is given
*/

SELECT * 
FROM orders;

SELECT 
    MIN(order_purchase_timestamp) AS start_date,
    MAX(order_purchase_timestamp) AS last_date
FROM orders;

---------
Part 1.3
---------
/*
Cities and States of customers ordered during the given period
*/

SELECT * 
FROM orders;

SELECT * 
FROM customers;

SELECT  DISTINCT c.customer_city as city,  c.customer_state as state
FROM orders o
INNER JOIN customers c 
    ON o.customer_id = c.customer_id
ORDER BY state, city

==========
Question 2
==========

---------
Part 2.1
---------
/*
Is there a growing trend on e-commerce in Brazil? How can we describe a complete scenario? Can we see some seasonality with peaks at specific months?
*/

SELECT * 
FROM orders;

-- No. of orders in monthly baisis 

WITH A AS (
    SELECT 
        order_id, 
        order_purchase_timestamp, 
        EXTRACT(YEAR FROM order_purchase_timestamp) AS year,
        EXTRACT(MONTH FROM order_purchase_timestamp) AS month
    FROM orders
)

SELECT 
    year, 
    month, 
    COUNT(1) as no_of_orders,
    SUM(no_of_orders) OVER(PARTITION BY year ORDER BY month ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_monthly_sales_each_year
FROM A 
GROUP BY year, month
ORDER BY year, month

-- No. of orders year over year 

WITH A AS (
    SELECT 
        order_id, 
        order_purchase_timestamp, 
        EXTRACT(YEAR FROM order_purchase_timestamp) AS year,
        EXTRACT(MONTH FROM order_purchase_timestamp) AS month
    FROM orders
),

B AS (
    SELECT 
        A.*, 
        P.payment_value 
        FROM A 
        INNER JOIN 
            payments P 
            ON A.order_id = P.order_id
    ),

C AS (
    SELECT 
        year, 
        month, 
        SUM(payment_value) as total_sales
    FROM B 
    GROUP BY year, month
    ORDER BY year, month
)

SELECT 
    DISTINCT year, 
    SUM(total_sales) OVER(PARTITION BY year) AS total_sales, 
    AVG(total_sales) OVER(PARTITION BY year) AS avg_sales
FROM C 
ORDER BY year
----

---------
Part 2.2
---------

/*
What time do Brazilian customers tend to buy (Dawn, Morning, Afternoon or Night)?
*/

SELECT * 
FROM orders;

WITH A AS (
    SELECT 
        order_id,
        CASE 
            WHEN DATE_PART('hour', order_purchase_timestamp) >= 0 AND DATE_PART('hour', order_purchase_timestamp) < 6 THEN 'Dawn'
            WHEN DATE_PART('hour', order_purchase_timestamp) >= 6 AND DATE_PART('hour', order_purchase_timestamp) < 12 THEN 'Morning'
            WHEN DATE_PART('hour', order_purchase_timestamp) >= 12 AND DATE_PART('hour', order_purchase_timestamp) < 18 THEN 'Afternoon'
            ELSE 'Night' 
        END AS time_of_day 
    FROM orders 
) 

SELECT 
    time_of_day, 
    COUNT(1) AS no_of_orders,
    RANK() OVER(ORDER BY no_of_orders DESC) AS rank
FROM A 
GROUP BY time_of_day
ORDER BY no_of_orders DESC

==========
Question 3
==========

---------
Part 3.1
---------
/*
Evolution of E-commerce orders in the Brazil region:
*/





















