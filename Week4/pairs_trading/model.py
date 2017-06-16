#!/usr/bin/env python3

from wrapper import Scraper
from orm import ORM

import pandas as pd
import time


class Model:

    scraper_on = True

    @classmethod
    def scrape(cls):

        while cls.scraper_on:
            goog_quote = Scraper().get_quote('GOOGL')
            msft_quote = Scraper().get_quote('MSFT')

            if goog_quote['Status'] == 'SUCCESS':
                ORM.update_goog(goog_quote)

            if msft_quote['Status'] == 'SUCCESS':
                ORM.update_msft(msft_quote)

            time.sleep(5)
            print(time.ctime())
            #cls.scraper_on = False


    @classmethod
    def get_data(cls, company_name):
        df = ORM.retrieve_tables(company_name)
        return df

if __name__ == "__main__":
    Model.scrape()
