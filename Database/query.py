# Imports 3rd party
from getpass import getpass
from mysql.connector import connect, Error, errorcode
# Local files
from visuals import bar_chart

# Queries
from queries_dict import queries_dict
from Queries import QueryBar

city_population_bar = QueryBar(queries_dict["Top 10 Cities"], "Cities", "Top 10 cities where customers reside", "Number of customers")

def make_query(query_obj):
    try:
        with connect(
                host="localhost",
                user=input("Enter user name."),
                password=getpass("Enter your password"),
                database=input("Enter DB name")
        ) as connection:

            x = []
            y = []

            with connection.cursor() as cursor:
                cursor.execute(query_obj.sql)
                result = cursor.fetchall()
                for row in result:
                    x.append(row[1])
                    y.append(row[0])

                query_obj.xdata = x
                query_obj.ydata = y
                query_obj.produce_chart()

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

make_query(city_population_bar)
