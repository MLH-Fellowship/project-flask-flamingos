# Flask-Blog

Minimal Flask template to get started on your blog application for MLH Fellowship Production Engineering track.

## Getting Started

To make a copy of the Flask website, just use [generate your own here](https://github.com/MLH-Fellowship/flask-blog/generate).

You don't need to submit any pull requests to thie repository. This is just a template to help you get started

## Installation

Make sure you have python3 and pip installed


Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage


Create a .env file using the example.env template


Start flask development server

1. Add `FLASK_ENV=development` to .env
2.
    ```bash
    $ docker-compose up
    ```
3. Access it at `http://127.0.0.1:5000`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
