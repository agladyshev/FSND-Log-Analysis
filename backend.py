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
    db, cursor = connect()
    cursor.execute(
        "SELECT title, views FROM topArticles")
    articles = cursor.fetchall()
    db.close()
    return articles


def getTopAuthors():
    """Returns the list of top authors"""
    db, cursor = connect()
    cursor.execute(
        "SELECT author, views FROM topAuthors")
    authors = cursor.fetchall()
    db.close()
    return authors


def getBadDays():
    """Returns the list of days with a large percent of request failures"""
    db, cursor = connect()
    cursor.execute(
        "SELECT date, errpercent FROM badDays")
    days = cursor.fetchall()
    db.close()
    return days
