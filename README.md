# SIP Parser CLI

Parse SIP requests from `.txt` files following the RFC3261 format with this simple command-line utility.

## Features

- Parse SIP requests and extract method, request-URI, headers, and body.
- Display parsed SIP details.
- Check for the existence of specific headers in the SIP request.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Tests](#tests)

## Installation

### Prerequisites

- Python 3.8 or above

### Steps

1. Clone the repository:

```bash
git clone https://github.com/mehrnaz-mh/cli-program.git
```

2. Navigate to the project directory:

```bash
cd cli-program
```

3. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

## Usage

Once you've download the source code and run the installation steps, you can run the following command to access the application's usage description:

```bash
$ python -m cli <filename>.txt --help
usage: cli.py [-h] [-p] [-e HEADER] filename

Parse a SIP request in a .txt file.

positional arguments:
  filename              Path to the .txt file containing
                        the SIP request.

options:
  -h, --help            show this help message and exit
  -p, --print           Print the parsed content of the SIP
                        request.
  -e HEADER, --exists HEADER
                        Check if the given header exists in
                        the SIP request.
```

### Parse and Display SIP Details

```bash
python -m cli <filename>.txt --print
```

### Check Header Existence

```bash
python -m cli <filename>.txt --exists <header_name>
```

Replace `<filename>` with the name of your `.txt` file containing the SIP request and `<header_name>` with the header you want to check.

## Tests

To run the unit tests, make sure you've installed `pytest`:

```bash
pip install pytest
```

Then, run:

```bash
pytest test_sip_parser.py
```
