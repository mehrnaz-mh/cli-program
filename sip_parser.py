import sys


# Function to read the content of a given SIP request filename.
def read_sip_request(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


# extract method, request-uri, headers, and body.
def parse_sip_request(content):
    lines = content.strip().split("\n")

    request_line = lines[0].split()
    method = request_line[0]
    request_uri = request_line[1]

    headers = {}

    body_index = content.find("\n\n")
    if body_index != -1:
        body = content[body_index + 2:]
    else:
        body = None

    # Loop through the remaining lines to parse headers.
    for line in lines[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            headers[key.lower()] = value

    return method, request_uri, headers, body


# Function to print parsed SIP request details.
def print_parsed_content(method, request_uri, headers, body):
    print("The given SIP message is a request with:")
    print(f"request-uri: {request_uri}")
    print(f"method: {method}")
    print("headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    print(f"body:\n{body}")


# Function to check if a specific header exists in the parsed headers.
def header_exists(header, headers):
    header_value = headers.get(header.lower())

    if header_value:
        return f"'{header}' exists with value: '{header_value}'", True
    else:
        return f"'{header}' does not exist in the SIP request.", False
