from decouple import config


class Config:
    """
    General configuration
    """
    username = config('USERNAME')
    password = config('PASSWORD')
    driver_path = './chromedriver'
    local_path = '/Users/jeffersonmontilla/Documents'
