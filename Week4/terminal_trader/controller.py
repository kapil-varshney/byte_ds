#!/usr/bin env python3

import model


def navigate():

    print("Welcome to the Terminal Trading Platform")
    new_or_returning_user()
    tasks()


def new_or_returning_user():

    print("Are you a returning user or a new user?")
    choice = input("1. Returning user\n2. New user\n")
    if choice == '1':
        returning_user()
    elif choice == '2':
        new_user()
    else:
        print("\nPlease enter a valid selection.")
        invalid_selection(new_or_returning_user)


def returning_user():

    username = input("\nPlease enter your username: ")
    password = input("Please enter your password: ")

    if model.identity_verified(username, password):
        print("Username and Password verified")
        return True
    else:
        print("\nIncorrect username and/or password.")
        invalid_selection(returning_user)


def new_user():

    username = input("\nPlease create a username.\n")

    if model.username_available(username):
        print("\nUsername is available. Please continue...")
    else:
        print("\nUsername not available. Please try another username.")
        invalid_selection(new_user)

    password = input("Please create a password.\n")
    name = input("Please enter your name\n")

    model.create_user(username, password, name)
    print("Congratulation, you are now a part of Terminal Trader family.")
    print("\nRedirecting you to the login page...")
    returning_user()


def invalid_selection(funct):
    user_input = input("Enter 0 to exit. Press any other key to try again.\n")
    if user_input == '0':
        user_exit()
    else:
        funct()


def user_exit():
    print("\nThank you for visiting. Have a good day.")
    exit(-1)


def tasks():
    print("\nWhat do you want to do today?")
    print("1. Search companies")
    print("2. Retrieve market data for a stock")
    print("3. Buy or Sell stocks")
    print("4. View your portfolio")
    print("0. Exit")

    user_input = input()

    if user_input == '1':
        search_companies()
    elif user_input == '2':
        retrieve_market_data()
    elif user_input == '3':
        buy_sell_stocks()
    elif user_input == '4':
        view_portfolio()
    elif user_input == '0':
        user_exit()
    else:
        print("Please enter a valid selection")
        tasks()


def search_companies():

    user_input = input("Which company are you trying to lookup?\n")
    print("\nRetrieving company information...\n")
    print(model.retrieve_company_data(user_input))


def retrieve_market_data():
    user_input = input("Enter the ticker symbol (all caps) for the stock you are looking at.\n")
    print("\nRetrieving market data...\n")
    print(model.retrieve_quote(user_input))


def buy_sell_stocks():
    pass
    user_input = input("\nDo you want to buy or sell a stock?\n1. Buy\n2. Sell\n")
    if user_input == '1':
        buy()
    elif user_input == '2':
        sell()
    else:
        print("Please enter a valid selection.")
        invalid_selection(buy_sell_stocks)




def view_portfolio():
    pass


navigate()
