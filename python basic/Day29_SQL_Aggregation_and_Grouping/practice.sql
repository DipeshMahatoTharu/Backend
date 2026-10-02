    -- =====================================================================
    -- Day 29 SQL Practice — Aggregations, GROUP BY & HAVING
    -- =====================================================================

    -- Table schema reference:
    -- CREATE TABLE products (
    --     id SERIAL PRIMARY KEY,
    --     name VARCHAR(150),
    --     category VARCHAR(50),
    --     price NUMERIC(10, 2),
    --     stock INT,
    --     is_available BOOLEAN
    -- );

    -- =====================================================================
    -- TASK 1: Global Summary Statistics
    -- =====================================================================
    -- Compute the overall catalog summary:
    -- 1. Total number of products as 'total_products'
    -- 2. Average price rounded to 2 decimal places as 'avg_price'
    -- 3. Minimum price as 'min_price'
    -- 4. Maximum price as 'max_price'
    -- 5. Total inventory units in stock as 'total_units'

    -- TODO: Write SELECT query below:
    CREATE TABLE products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        category VARCHAR(50),
        price NUMERIC(10,2),
        stock INT,
        is_available BOOLEAN
    )
    SELECT 
        count(*) as total_products,
        ROUND(AVG(price),2) AS avg_price,
        MIN(price) as min_price,
        MAX(price) as max_price,
        sum(stock) as total_units
    FROM products;





    -- =====================================================================
    -- TASK 2: Category-Level Aggregation & Inventory Value
    -- =====================================================================
    -- Group the products table by 'category' and compute:
    -- 1. Category name
    -- 2. Total products in that category
    -- 3. Average price of products in that category
    -- 4. Total warehouse value for that category: SUM(price * stock)
    -- Filter out products where stock = 0 BEFORE aggregating.
    -- Order by total warehouse value descending.


    SELECT
        category,
        COUNT(*) AS total_products,
        AVG(price) AS avg_product,
        SUM(price * stock) AS total_sum
    FROM products
    WHERE stock > 0
    GROUP BY category
    ORDER BY total_sum DESC;


    -- =====================================================================
    -- TASK 3: Filtering Groups with HAVING
    -- =====================================================================
    -- Find all categories that meet BOTH of the following conditions:
    -- 1. Has MORE than 2 distinct products (COUNT(*) > 2)
    -- 2. Has an average product price GREATER than $50.00
    -- Order results by average price descending.

    -- TODO: Write query using GROUP BY and HAVING below:
    SELECT 
            category,
            count (*) as total_products,
            AVG(price) AS avg_price
        FROM products
        GROUP BY category
    

        HAVING count(*) >2  
            AND AVG(price) > 50.00
        ORDER BY avg_price DESC;


    -- =====================================================================
    -- TASK 4: Multi-Column Grouping
    -- =====================================================================
    -- Group products by BOTH 'category' AND 'is_available'.
    -- Compute: category, is_available, product count, and total stock.
    -- Order by category ASC, is_available DESC.

    -- TODO: Write multi-column grouping query below:


    SELECT 
        category,
        is_available,
        count(*)  as total_products,
        sum(stock) as  total_stock

        
    FROM products
    GROUP BY category  ,is_available
    ORDER BY category ASC,is_available DES


    -- =====================================================================
    -- TASK 5: Monthly Order & Revenue Analytics
    -- =====================================================================
    -- Given an 'orders' table (id, customer_id, order_date, total_amount, status):
    -- Write a query to report monthly performance for COMPLETED orders:
    -- 1. Month formatted as 'YYYY-MM' (SQLite: strftime('%Y-%m', order_date), Postgres: TO_CHAR(order_date, 'YYYY-MM'))
    -- 2. Total order count
    -- 3. Total gross revenue
    -- 4. Average order value (AOV) rounded to 2 decimal places
    -- Filter only status = 'COMPLETED'.
    -- Order chronologically by month ascending.

    -- TODO: Write monthly analytics query below:

    CREATE table orders(
        id INT PRIMARY KEY ,
        customer_id INT NOT NULL ,
        order_date DATE NOT NULL,
        total_amount  DECIMAL(10,2) NOT NULL,
        status VARCHAR(50) NOT NULL
    );

    SELECT 
        TO_CHAR(order_date,'YYYY-MM') AS month,
        COUNT(*) as total_order,
        SUM(total_amount) as gross_revenue,
        ROUND(AVG(total_amount),2) as aov,
        WHERE status ='COMPLETED'
        ORDER BY month ASC
        GROUP BY TO_CHAR(order_date,'YYYY-MM')
    FROM orders;

