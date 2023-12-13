queries_dict = {
    "Top 10 Cities": "SELECT COUNT(*) AS count, CITY FROM customers GROUP BY CITY HAVING COUNT(*) > 10 ORDER BY "
                      "count DESC LIMIT 10",
    "Customer type": "SELECT COUNT(*) AS count, customer_type FROM customersGROUP BY customer_type ORDER BY count DESC",
}