#!/usr/bin/env python2
#
# backend.py -- connects to the db and execute queries on demand
#

import psycopg2
import random


def connect(database_name="news"):
    """
    Connects to the PostgreSQL database.
    Returns a database connection and a cursor."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Database connection failed")


def getTopArticles():
    """Returns the list of top aricles"""
    return execute_query("SELECT title, views FROM topArticles")


def getTopAuthors():
    """Returns the list of top authors"""
    return execute_query("SELECT author, views FROM topAuthors")


def getBadDays():
    """Returns the list of days with a large percent of request failures"""
    return execute_query("SELECT date, errpercent FROM badDays")


def execute_query(query):
    try:
        db, cursor = connect()
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)