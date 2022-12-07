# Dev.to Article fetcher

This simple CLI will download the articles for a give account to your local computer.

> **Note**
> The articles must be published, draft articles will not be downloaded

## Setup

Clone the `conf.sample.ini` file in the `conf/` folder, and name it `conf.ini`.

Run it in an virtual env:

```sh
pipenv shell
```

Then install dependencies:

```sh
# with pipenv
pipenv install

# or just pip
pip install -r requirements.txt
```

## Usage

Run the command, which expect one argument being the `username`:

```sh
python3 ./fetcher.py <username>

# example
python3 ./fetcher.py someusername
```

The script will add the files in the `articles` folder, which can be changed by setting it in the `conf/conf.ini` file.

## Resources

- [Forem API](https://developers.forem.com/api)
