# Write your MySQL query statement below

```SQL
select product_id,sum(quantity) AS total_quantity from Sales GROUP BY product_id
```