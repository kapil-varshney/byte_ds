#!/usr/bin/env python3

from wrapper import Scraper
from orm import ORM

import pandas as pd
import time


class Model:

    scraper_on = True
    goog_df = pd.DataFrame(columns=['LastPrice',
                                     'Change',
                                     'ChangePercent',
                                     'Timestamp',
                                     'MSDate',
                                     'MarketCap',
                                     'Volume',
                                     'ChangeYTD',
                                     'ChangePercentYTD',
                                     'High',
                                     'Low',
                                     'Open'])
    msft_df = pd.DataFrame(columns=['LastPrice',
                                    'Change',
                                    'ChangePercent',
                                    'Timestamp',
                                    'MSDate',
                                    'MarketCap',
                                    'Volume',
                                    'ChangeYTD',
                                    'ChangePercentYTD',
                                    'High',
                                    'Low',
                                    'Open'])

    @classmethod
    def scrape(cls):

        while cls.scraper_on:
            goog_quote = Scraper().get_quote('GOOGL')
            msft_quote = Scraper().get_quote('MSFT')

            if goog_quote['Status'] == 'SUCCESS':
                ORM.update_goog(goog_quote)
            else:
                print("There was a fetch error.")

            if msft_quote['Status'] == 'SUCCESS':
                ORM.update_msft(msft_quote)
            else:
                print("There was a fetch error.")

            time.sleep(5)
            print(time.ctime())

            #cls.scraper_on = False

    @classmethod
    def get_data(cls, company_name):
        df = ORM.retrieve_tables(company_name)
        return df

    """
    scrape_df(), scrape_call() are used to hold the scraped data in a data frame to be passed to the ORM.
    The data will be passed to the ORM only when user is done with scraping (Ctrl+C input). 
    ORM then can write the data frame into the respective SQL table at once.
    
    Underlying Hypothesis is that holding the data in the memory(dataframe) and then writing it to database
    will save time, as compared to writing into the database one row at a time.
        
    """

    @classmethod
    def scrape_df(cls):

        while cls.scraper_on:
            goog_quote = Scraper().get_quote('GOOGL')
            msft_quote = Scraper().get_quote('MSFT')

            if goog_quote['Status'] == 'SUCCESS':
                a_dict = {k: pd.Series([str(v)], index=[0]) for k, v in goog_quote.items()}
                append_df = pd.DataFrame.from_dict(a_dict)
                #cls.goog_df.append(append_df, ignore_index=True)
                cls.goog_df = pd.concat([cls.goog_df, append_df])

            else:
                print("There was a fetch error.")

            if msft_quote['Status'] == 'SUCCESS':
                a_dict = {k: pd.Series([str(v)], index=[0]) for k, v in msft_quote.items()}
                append_df = pd.DataFrame.from_dict(a_dict)
                # cls.msft_df.append(append_df, ignore_index=True)
                cls.msft_df = pd.concat([cls.msft_df, append_df])

            else:
                print("There was a fetch error.")

            time.sleep(5)
            print(time.ctime())
            #cls.scraper_on = False

        print(cls.goog_df)
        print(cls.msft_df)

    @classmethod
    def scraper_call(cls):
        print("\nPress Ctrl+C anytime to stop scraping\n")
        print("\nRetrieving information from Markit API...\n")
        try:
            cls.scrape_df()
        except KeyboardInterrupt:
            print("\nStopped Scraping\n")

            cls.goog_df = cls.goog_df.reset_index()
            cls.msft_df = cls.msft_df.reset_index()

            print(cls.goog_df)
            print(cls.msft_df)
            #ORM.update_goog_df(cls.goog_df)
            #ORM.update_msft_df(cls.msft_df)


if __name__ == "__main__":
    #Model.scrape_df()
    Model.scraper_call()
