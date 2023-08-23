import pytest
import sip_parser

# Test Data
sample_content = """
INVITE sip:bob@biloxi.com SIP/2.0
Via: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bKnashds8
Max-Forwards: 70
To: Bob <sip:bob@biloxi.com>
From: Alice <sip:alice@atlanta.com>;tag=1928301774
Call-ID: a84b4c76e66710
CSeq: 314159 INVITE
Contact: <sip:alice@pc33.atlanta.com>
Content-Type: plain/text
Content-Length: 3

abc"""


# Test the read_sip_request function
def test_read_sip_request_existing_file_returns_content():
    with open("temp_test_file.txt", "w") as file:
        file.write(sample_content)

    # Check if the function correctly reads and returns the content of the file
    result = sip_parser.read_sip_request("temp_test_file.txt")
    assert result == sample_content


# Test the parse_sip_request function
def test_parse_sip_request_valid_content_returns_parsed_data():
    method, request_uri, headers, body = sip_parser.parse_sip_request(
        sample_content)

    # Asserting expected parsed data
    assert method == "INVITE"
    assert request_uri == "sip:bob@biloxi.com"
    assert headers == {
        "via": "SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bKnashds8",
        "max-forwards": "70",
        "to": "Bob <sip:bob@biloxi.com>",
        "from": "Alice <sip:alice@atlanta.com>;tag=1928301774",
        "call-id": "a84b4c76e66710",
        "cseq": "314159 INVITE",
        "contact": "<sip:alice@pc33.atlanta.com>",
        "content-type": "plain/text",
        "content-length": "3"
    }
    assert body == "abc"


# Test the header_exists function
def test_header_exists_header_present_returns_true_with_value():
    _, _, headers, _ = sip_parser.parse_sip_request(sample_content)
    message, exists = sip_parser.header_exists("Via", headers)

    assert exists
    assert message == "'Via' exists with value: 'SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bKnashds8'"


# Test the `header_exists` function when the header is absent in the SIP request.
def test_header_exists_header_absent_returns_false():
    _, _, headers, _ = sip_parser.parse_sip_request(sample_content)
    message, exists = sip_parser.header_exists('Unknown-Header', headers)

    assert not exists
    assert message == "'Unknown-Header' does not exist in the SIP request."
