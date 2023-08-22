import argparse
import sip_parser

# Main function definition.
def main():
    # Create a new argument parser object.
    parser = argparse.ArgumentParser(description='Parse a SIP request in a .txt file.')
    
    parser.add_argument('filename', type=str, help='Path to the .txt file containing the SIP request.')
    parser.add_argument('-p', '--print', action='store_true', help='Print the parsed content of the SIP request.')
    parser.add_argument('-e', '--exists', type=str, metavar='HEADER', help='Check if the given header exists in the SIP request.')

    # Parse the arguments provided by the user when running the program.
    args = parser.parse_args()
        
    content = sip_parser.read_sip_request(args.filename)
    method, request_uri, headers, body = sip_parser.parse_sip_request(content)

    # If the '--print' option was provided, print the parsed content.
    if args.print:
        sip_parser.print_parsed_content(method, request_uri, headers, body)

    # If the '--exists' option was provided, check if the specified header exists and print the result.
    if args.exists:
        message, exists = sip_parser.header_exists(args.exists, headers)
        print(message)


if __name__ == "__main__":
    main()
