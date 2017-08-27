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
    print "To get the list of top authors, enter '1'"
    print "To get the list of top articles, enter '2'"
    print "To get the list of days with more than 1% of errors, enter '3'"
    print "To quit the program, enter 'q'\n"
    menu_choices = ['1', '2', '3', 'q']
    choice = getInput(menu_choices)
    if choice == 'q':
        return
    if choice == '1':
        topAuthors = getTopAuthors()
        print '\nTOP AUTHORS ARE:'
        for author, views in topAuthors:
            print('·{} – {} views'.format(author, views))
        mainMenu()
    if choice == '2':
        topArticles = getTopArticles()
        print '\nTOP ARTICLES ARE:'
        for article, views in topArticles:
            print('·{} – {} views'.format(article, views))
        mainMenu()
    if choice == '3':
        badDays = getBadDays()
        print '\nDAYS WITH MORE THAN 1% BAD REQUESTS:'
        for date, errors in badDays:
            print('·{:%B %d, %Y} – {}% of bad requests'.format(date, errors))
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


if __name__ == '__main__':
    mainMenu()