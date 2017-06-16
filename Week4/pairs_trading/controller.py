#!/usr/bin/env python3

import model


class Controller:

    goog_name = 'Alphabet Inc'
    goog_symbol = 'GOOGL'

    msft_name = 'Microsoft Corp'
    msft_symbol = 'MSFT'

    @classmethod
    def navigate(cls):

        print("1. Start Scraping")
        print("2. Stop Scraping")
        print("3. View Data")
        print("0. Exit")
        user_input = input()

        if user_input == '1':
            cls.start_scraping()

        elif user_input == '2':
            cls.stop_scraping()

        elif user_input == '3':
            cls.view_data()

        elif user_input == '0':
            cls.user_exit()

        else:
            print("\nPlease enter a valid selection")
            cls.navigate()

    @classmethod
    def start_scraping(cls):
        pass

    @classmethod
    def stop_scraping(cls):
        pass

    @classmethod
    def view_data(cls):
        pass




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
