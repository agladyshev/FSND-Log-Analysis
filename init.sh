#!/bin/bash

clear
echo "======================="
echo "Preparing News database"
echo "======================="
echo
psql -f createdb.sql
psql -d news -f newsdata.sql
psql -f views.sql