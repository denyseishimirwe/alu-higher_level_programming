#!/bin/bash
# This script runs the SQL query to list all databases

# Show the initial databases
echo "Correct output: initial databases sorted"
mysql -hlocalhost -uroot -p < 0-list_databases.sql

# Create multiple databases
echo "Creating multiple databases..."
mysql -hlocalhost -uroot -p -e "CREATE DATABASE db1;"
mysql -hlocalhost -uroot -p -e "CREATE DATABASE db2;"
mysql -hlocalhost -uroot -p -e "CREATE DATABASE db3;"

# Show the databases after creation of new databases
echo "Correct output: after creation of multiple databases"
mysql -hlocalhost -uroot -p < 0-list_databases.sql

