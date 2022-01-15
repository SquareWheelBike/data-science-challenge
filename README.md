## Question 1
---

> a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.

A good way to evaluate this data might be to remove outliers. This can be accomplished by removing quantiles that are more than 1 standard deviation away from the mean. With a dataset with outliers so far from the mean, this only removes the far high outliers. 

---

> b. What metric would you report for this dataset?

I would probably report the average of values in the interquartile range.

```py
std = df['order_amount'].std()
mean = df['order_amount'].mean()
q1, q3 = mean - std, mean + std
df = df[(df['order_amount'] > q1) & (d['order_amount'] < q3)]
```

---

> c. What is its value?

$400.04

--- 

## Question 2

---

> a. How many orders were shipped by Speedy Express in total?

### SQL Statement:
```sql
SELECT count(OrderID) FROM orders 
WHERE ShipperID=(
    SELECT ShipperID FROM [Shippers] 
    WHERE ShipperName='Speedy Express')
```

### Result:
| count(OrderID) |
| --- |
| 54 |

 ---

> b. What is the last name of the employee with the most orders?

### SQL Statement:
```sql
SELECT LastName 
FROM (
    SELECT LastName, MAX(NumberOfOrders) asNumberOfOrders
    FROM (
        SELECT Employees.LastName, COUNT(Orders.OrderID) ASNumberOfOrders
        FROM (Orders
            INNER JOIN Employees ON Orders.EmployeeID =Employees.EmployeeID)
        GROUP BY LastName
    )
);
```

### Result:
| LastName | 
| -------- | 
Peacock | 

---

> c. What product was ordered the most by customers in Germany?
    
### SQL Statement:
```sql
SELECT ProductName FROM [Products]
WHERE ProductID=(
    SELECT ProductID FROM (
        SELECT ProductID, MAX(OrderedCount) AS TimesOrdered FROM (
            SELECT ProductID, COUNT(*) AS OrderedCount FROM OrderDetails
            WHERE OrderID IN ( 
                SELECT OrderID FROM Orders WHERE CustomerID IN (
                    SELECT CustomerID FROM Customers WHERE Country='Germany'
                )
            )
            GROUP BY ProductID
        )
    )
);
```

### Result:

| ProductName |
| ----------- |
| Gorgonzola Telino |

** I interpreted this as 'the product with the most orders' rather than 'most total stock purchased'. The top item ordered was only ordered 5 times, this is the count of orders made containing the item, NOT the volume of stock purchased. **

-----------------------------------------------

NOTE: This is my first time using SQL, I have my first class in it next semester. I have probably committed some sins here but it is what it is. 
