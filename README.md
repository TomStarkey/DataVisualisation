# DataVisualisation
A script that automates the process of fetching data from multiple sources and puts them into an integrated spreadsheet.

# The Vision
The task was to find a way to cherry pick some data from a database that functions as the backend of an established piece of software, which does not provide the desired data visualisation with the chosen data.
## Structure
The project would use SQL to make queries to this database, which would then be passed to a Python script to visualise the data. *It is currently an ongoing project*. Therefore it does not reflect the end result. *However* the vision is to use SQL views in order to get the data required from several different tables into precisely the format desired. This will then be stored in the *queries_dict.py* file. Each key of the dictionary is a descriptive name, each value will be a single call to the view which has already been made on the database. This abstracts the SQL code, removing the complexity from the Python scripts. This way when a connection is made, the python script need only call the descriptive name of one of the keys in the dictionary, and the required information will appear, in a view, having already been managed behind the scenes in the SQL code.
## Python files
There are several Python files in this programme. This was done to declutter the code and assign less purposes, in some case single purposes, to the files themselves.

For instance *queries_dict.py* is just a dictionary. This keeps that information from bloating the other files. *Queries.py* is a file that contains classes which simplify the process of producing different types of graphs. It takes functions from the *visuals.py* file which contains the detailed code that uses matplotlib to produce graphs. This abstracts the complexity of the graph making away from the Queries.py file which in turn abstracts it away from the query.py file. 

In query.py you will see an example of a single query that connects to the database, collects the data and then uses the QueryBar class from *Query.py* in order to produce a bar chart visualising that data.

When the project is complete, there will be multiple visualisations such as that one, compiled onto a dashboard using the dash library. You can see the beginnings of that in the *datavis.py* file.

## Patience
That is the project so far. The work is done in my own time alongside work and other commitments, therefore the progress is slow. Slow, but gradually getting there.

### Openness
I am open to any feedback as this is the beginning of my journey in software development. However, I will not be openning this repository up to contributions.
