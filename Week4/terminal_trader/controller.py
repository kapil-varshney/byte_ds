#!/usr/bin/env python3

import model


class Controller:

    username = ''

    @classmethod
    def navigate(cls):

        print("Welcome to the Terminal Trading Platform")
        cls.new_or_returning_user()
        cls.tasks()

    @classmethod
    def new_or_returning_user(cls):

        print("Are you a returning user or a new user?")
        choice = input("1. Returning user\n2. New user\n")
        if choice == '1':
            cls.returning_user()
        elif choice == '2':
            cls.new_user()
        else:
            print("\nPlease enter a valid selection.")
            cls.invalid_selection(cls.new_or_returning_user)

    @classmethod
    def returning_user(cls):

        username = input("\nPlease enter your username: ")
        password = input("Please enter your password: ")

        if model.identity_verified(username, password):
            print("Username and Password verified")
            cls.username = username
            return True
        else:
            print("\nIncorrect username and/or password.")
            cls.invalid_selection(cls.returning_user)

    @classmethod
    def new_user(cls):

        username = input("\nPlease create a username.\n")

        if model.username_available(username):
            print("\nUsername is available. Please continue...")
            password = input("Please create a password.\n")
            name = input("Please enter your name\n")
            model.create_user(username, password, name)
            print("Congratulation, you are now a part of Terminal Trader family.")
            print("\nRedirecting you to the login page...")
            cls.returning_user()
        else:
            print("\nUsername not available.")
            cls.invalid_selection(cls.new_user)

    @classmethod
    def tasks(cls):
        print("\nWhat do you want to do today?")
        print("1. Search companies")
        print("2. Retrieve market data for a stock")
        print("3. Buy stocks")
        print("4. Sell stocks")
        print("5. View your portfolio")
        print("0. Exit")

        user_input = input()

        if user_input == '1':
            df = cls.search_companies()
            if df.empty:
                print("Invalid company or data not available")
            else:
                print(df)
            cls.tasks()

        elif user_input == '2':
            print(cls.retrieve_market_data())
            cls.tasks()

        elif user_input == '3':
            cls.buy()

        elif user_input == '4':
            cls.sell()

        elif user_input == '5':
            df = cls.view_portfolio()
            if df.empty:
                print("You don't hold any stocks\n")
            else:
                print(df)
            cls.tasks()

        elif user_input == '0':
            cls.user_exit()

        else:
            print("Please enter a valid selection")
            cls.tasks()

    @classmethod
    def search_companies(cls):

        user_input = input("Which company are you trying to lookup?\n")
        print("\nRetrieving company information...\n")
        return model.retrieve_company_data(user_input)

    @classmethod
    def retrieve_market_data(cls):
        user_input = input("Enter the ticker symbol (all caps) for the stock you are looking at.\n")
        print("\nRetrieving market data...\n")
        return model.retrieve_market_data(user_input)

    @classmethod
    def buy(cls):

        df = cls.search_companies()
        if df.empty:
            print("Invalid company or data not available")
            cls.tasks()
        else:
            print(df)

        ticker_symbol = input("\nPlease enter the ticker of the stock you are interested in.\n")
        if ticker_symbol not in list(df['Symbol']):
            print("Enter a valid ticker")
            cls.invalid_selection(cls.buy)

        market_data = model.retrieve_market_data(ticker_symbol)
        print("The last price of", market_data['Symbol'], "is:", market_data['LastPrice'], "as of", market_data['Timestamp'])

        if market_data['LastPrice'] == 0:
            print("\nThis stock is worth nothing. Please select another stock.\n")
            cls.buy()

        user_input = input("\nDo you want to proceed?\n1. Yes\n2. No (Go to the previous options)\n")

        if user_input == '1':
            cls.buy_stock(market_data['Symbol'])
        elif user_input == '2':
            cls.tasks()
        else:
            print("Please enter a valid selection")
            cls.invalid_selection(cls.buy)

    @classmethod
    def buy_stock(cls, ticker_symbol):
        balance = model.retrieve_balance(cls.username)
        print("\nYou have $", balance)
        num_of_stocks = int(input("How many stocks do you wanna buy?\n"))

        if model.enough_balance(cls.username, ticker_symbol, num_of_stocks):
            model.make_purchase(cls.username, ticker_symbol, num_of_stocks)
        else:
            user_input = input("\nYou don't have sufficient balance.\n1. Try different volume.\n2. Pick some other stock.\n0. Exit.")
            if user_input == '1':
                cls.buy_stock(ticker_symbol)
            elif user_input == '2':
                cls.buy()
            elif user_input == '0':
                cls.user_exit()
            else:
                print("Please enter a valid selection.")
                cls.invalid_selection(cls.buy)

        print("\nUpdated")
        print(cls.view_portfolio())
        cls.tasks()

    @classmethod
    def sell(cls):

        df = model.get_portfolio(cls.username)
        print(df)

        ticker_symbol = input("Enter the ticker for the stock you want to sell: ")
        if ticker_symbol not in list(df['symbol']):
            print("You don't own that stock.")
            cls.invalid_selection(cls.sell)

        market_data = model.retrieve_market_data(ticker_symbol)
        print("The last price of", market_data['Symbol'], "is:", market_data['LastPrice'], "as of",
              market_data['Timestamp'])

        volume = int(input("How many stock do you want to sell? "))
        if volume < int(df[df['symbol'] == ticker_symbol]['quantity']):
            model.sell_stocks(cls.username, ticker_symbol, volume)
        else:
            user_input = input("\nYou don't have sufficient volume.\n1. Try different volume.\n2. Pick some other stock.\n0. Exit.")
            if user_input == '1':
                cls.sell()
            elif user_input == '2':
                cls.sell()
            elif user_input == '0':
                cls.user_exit()
            else:
                print("Please enter a valid selection.")
                cls.invalid_selection(cls.buy)

        print("\nUpdated")
        print(cls.view_portfolio())
        cls.tasks()

    @classmethod
    def view_portfolio(cls):
        print("\nBalance: ", model.retrieve_balance(cls.username))
        print("\n*****Portfolio*****\n")
        return model.get_portfolio(cls.username)

    @classmethod
    def invalid_selection(cls, funct):
        user_input = input("Enter 0 to exit. Press any other key to try again.\n")
        if user_input == '0':
            cls.user_exit()
        else:
            funct()

    @classmethod
    def user_exit(cls):
        print("\nThank you for visiting. Have a good day.")
        exit(-1)

    @classmethod
    def test(cls):
        df = cls.view_portfolio()
        print(df[df['symbol'] == 'GOOG']['quantity'])


if __name__ == '__main__':
    Controller.navigate()

    # Controller.buy()
    # Controller.tasks()
    # Controller.buy_stock('AAPL')
    # print(Controller.view_portfolio())
    # Controller.sell()
    # Controller.test()