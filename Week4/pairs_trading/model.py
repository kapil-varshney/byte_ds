#!/usr/bin/env python3

from wrapper import Scraper

import pandas as pd


class Model:

    scraper_on = True

    @classmethod
    def scrape(cls):

        while cls.scraper_on:
            goog_quote = Scraper().get_quote('GOOGL')
            msft_quote = Scraper().get_quote('MSFT')

            if goog_quote['Status'] == 'SUCCESS':
                pass

            if msft_quote['Status'] == 'SUCCESS':
                pass

            cls.scraper_on = False


if __name__ == "__main__":
    Model.scrape()