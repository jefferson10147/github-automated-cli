import os
from decouple import config


class Config:
    """
    General configuration
    """
    username = config('USERNAME')
    password = config('PASSWORD')
    driver_path = './chromedriver'

    @staticmethod
    def get_driver_path(self):
        return self.driver_path
