# github automated cli
## ![Python_logo_Selenium](https://i.ibb.co/p22K38X/selenium-with-python.png)

## Automation App Using Python and Selenium

<table>
    <tr>
        <td>
            You may manage your GitHub account using this CLI by doing actions like creating a new repository on GitHub and setting up the repository on your local machine. In the same way, you can do other actions like delete the repository and update some settings of it.

            This tool uses Selenium with Python, and Chrome to make the automated task.
        </td>
    </tr>
</table>

## Installation and Usage (UNIX Systems)

1- Clone this project, on your local machine:

```bash
$git clone https://github.com/jefferson10147/github-automated-cli.git
```

2- Create a Python virtual environment (Optional):

```bash
$python3 -m venv ./your_venv
```

2.1- Activate env:

```bash
$source your_venv/bin/activate
```

4- Install dependencies:

```bash
$pip install -r requirements.txt
```

5- Download the Chromedriver from [here](https://chromedriver.chromium.org/downloads) and move the executable file inside the root directory. Please make sure that you have selected the right version of your browser.

6- Create the .env file with the following structure:

```env
USERNAME=your_github_username
PASSWORD=your_github_password
```

7- Take a look at the file Settings/settings.py it has more configuration that you may change into the class.

8- You may execute the command to see the usage:
```bash
$python3 main.py --version
```

## Examples:

- To create the repository on GitHub and set it up locally:
```bash
$python3 main.py --create --name 'You repository name' --local --private
```

- To delete the repository on GitHub:
```bash
$python3 main.py --delete --name 'You repository name'
```