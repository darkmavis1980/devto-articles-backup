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

By default it will download the first 100 records, or whatever number you set in the `PER_PAGE` variable in the `conf.ini` file.
If you want to override that directly from the CLI, you can use the following optional flags:

- `-p, --page <number>` Set the pagination page number
- `-l, --limit <number>` Set the limit number for the pagination

Example:

```bash
# It will download the articles from 11 to 20
python3 ./fetcher.py someusername --page=2 --limit=10
```

The script will add the files in the `articles` folder, which can be changed by setting it in the `conf/conf.ini` file.

## Resources

- [Forem API](https://developers.forem.com/api)
