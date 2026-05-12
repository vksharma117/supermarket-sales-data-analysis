CREATE DATABASE supermarket_sales;

USE supermarket_sales;

SELECT * FROM supermarket_sales_dataset;

SELECT `Product line` , SUM(Total) FROM supermarket_sales_dataset
GROUP BY `Product line`
ORDER BY SUM(Total) DESC;

SELECT City , SUM(Total) FROM supermarket_sales_dataset
GROUP BY city
ORDER BY SUM(Total) DESC;

SELECT Payment , COUNT(*) FROM supermarket_sales_dataset
GROUP BY Payment
ORDER BY COUNT(*) DESC;

SELECT `Customer type` , SUM(Total) FROM supermarket_sales_dataset
GROUP BY `Customer type`
ORDER BY SUM(Total) DESC;

SELECT `Product line` , AVG(`Customer stratification rating`) FROM supermarket_sales_dataset
GROUP BY `Product line`
ORDER BY AVG(`Customer stratification rating`) DESC;

SELECT AVG(`Gross income`) FROM supermarket_sales_dataset;

SET SQL_SAFE_UPDATES = 0;

ALTER TABLE supermarket_sales_dataset 
ADD COLUMN new_date DATE;

UPDATE supermarket_sales_dataset
SET new_date = STR_TO_DATE(Date,'%m/%d/%Y');

SELECT MONTHNAME(new_date) AS month , SUM(Total) AS total_sales FROM supermarket_sales_dataset
GROUP BY month
ORDER BY MIN(new_date);

SET SQL_SAFE_UPDATES = 1;