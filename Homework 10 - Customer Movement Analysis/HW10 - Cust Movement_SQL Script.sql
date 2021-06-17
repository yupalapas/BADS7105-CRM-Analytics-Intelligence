with customer as 
(
select distinct cust_code ,
DATE_TRUNC(PARSE_DATE("%Y%m%d", CAST(SHOP_DATE AS STRING)) , Month) as cur_month ,
from `homework-10-cust-movement.DB_SUPERMARKET.CUSTOMER MOVEMENT`
),
customer_month as 
(
select cust_code, cur_month, LAG(cur_month,1) OVER (PARTITION BY cust_code ORDER BY cur_month) AS prev_month 
FROM customer
),
Report_cust1 as (
SELECT cust_code, cur_month , prev_month,
CASE WHEN DATE_DIFF (cur_month, prev_month, MONTH) = 1  THEN 'Repeat' 
    WHEN DATE_DIFF(cur_month, prev_month, MONTH) > 1 THEN 'Reactivated'
    WHEN DATE_DIFF(cur_month, prev_month, MONTH) IS NULL THEN 'New' End as Status
FROM customer_month
),
Report_cust2 as (
select cust_code ,cur_month ,DATE_ADD(cur_month, INTERVAL 1 MONTH) as Future_month ,
case when cur_month <= (select MAX(cur_month) from customer) then 'Churn' end as status 
from (
select cust_code , cur_month ,ROW_NUMBER() OVER ( PARTITION BY cust_code ORDER BY cur_month DESC ) as rwn
from customer) t where rwn = 1)


select cur_month ,status ,count(Cust_code) from(
select cust_code , cur_month , status 
from Report_cust1

UNION ALL 
select cust_code , Future_month , status
from Report_cust2 where Future_month <= (select MAX(cur_month) from customer) )

group by cur_month ,status 