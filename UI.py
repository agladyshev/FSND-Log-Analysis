#!/usr/bin/env python
# coding: latin-1
#
# UI.py -- Log Analysis Reporter v1.0
# Making the best of your marketing strategy

from backend import *


def mainMenu():
    """
    Main interactive procedure.
    Allows to request analysis
    """
    print "\n"
    print "To get the list of top authors, enter 'AUTHORS'"
    print "To get the list of top articles, enter 'ARTICLES'"
    print "To get the list of days with more than 1% errors, enter 'LOGS'"
    print "To exit the program, enter 'EXIT'\n"
    menu_choices = ['authors', 'articles', 'logs', 'exit']
    choice = getInput(menu_choices)
    if choice == 'exit':
        return
    if choice == 'authors':
        topAuthors = getTopAuthors()
        print '\nTOP AUTHORS ARE:'
        for author in topAuthors:
            print '·%s – %s views' % (author[0], author[1])
        mainMenu()
    if choice == 'articles':
        topArticles = getTopArticles()
        print '\nTOP ARTICLES ARE:'
        for article in topArticles:
            print '·%s – %s views' % (article[0], article[1])
        mainMenu()
    if choice == 'logs':
        badDays = getBadDays()
        print '\nDAYS WITH MORE THAN 1% BAD REQUESTS:'
        for day in badDays:
            print '·%s – %s%% errors' % (day[0], day[1])
        mainMenu()


def getInput(menu_choices):
    """
    Helper interface function for menu navigation.
    Takes as input a list of valid input entries.
    Returns valid player's input.
    """
    choice = raw_input().lower()
    while choice not in menu_choices:
        print "Incorrect input, try again:"
        choice = raw_input().lower()
    return choice


mainMenu()
