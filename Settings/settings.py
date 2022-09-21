from decouple import config


class Config:
    """
    General configuration
    """
    username = config('USERNAME')
    password = config('PASSWORD')
    driver_path = './chromedriver'
    local_path = '/Users/jeffersonmontilla/Documents'
    github_link = f'https://github.com/{username}/'
    main_branch_name = 'master'
