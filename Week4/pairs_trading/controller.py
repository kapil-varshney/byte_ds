#!/usr/bin/env python3

from model import Model


class Controller:

    goog_name = 'Alphabet Inc'
    goog_symbol = 'GOOGL'

    msft_name = 'Microsoft Corp'
    msft_symbol = 'MSFT'

    @classmethod
    def navigate(cls):

        print("\nWelcome to the Pairs Trading platform...\n")
        print("1. Start Scraping")
        print("2. View Data")
        print("0. Exit")
        user_input = input()

        if user_input == '1':
            cls.start_scraping()

        elif user_input == '2':
            cls.view_data()

        elif user_input == '0':
            cls.user_exit()

        else:
            print("\nPlease enter a valid selection")

        cls.navigate()

    @classmethod
    def start_scraping(cls):
        print("\nPress Ctrl+C anytime to stop scraping\n")
        print("\nRetrieving information from Markit API...\n")
        try:
            Model.scrape()
        except KeyboardInterrupt:
            print("\nStopped Scraping\n")

    @classmethod
    def stop_scraping(cls):
        pass

    @classmethod
    def view_data(cls):

        user_input = input("\n1. Google\n2. Microsoft\n3. Previous Menu\n")
        if user_input == '1':
            company_name = 'google'
            print('\n', cls.goog_name, '\n')

        elif user_input == '2':
            company_name = 'microsoft'
            print('\n', cls.msft_name, '\n')

        elif user_input == '3':
            cls.navigate()

        else:
            print("Please enter a valid selection")
            cls.invalid_selection(cls.view_data)

        df = Model.get_data(company_name)
        if df.empty is True:
            print("No stored data available")
        else:
            print(df)

        cls.view_data()


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


if __name__ == '__main__':
    Controller.navigate()
