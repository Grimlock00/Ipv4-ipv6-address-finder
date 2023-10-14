# Ipv4-ipv6-address-finder

This Python script is a simple utility to resolve both IPv4 and IPv6 addresses for a given URL (domain name) using the `socket` library. It allows you to enter a URL, and it attempts to find both IPv4 and IPv6 addresses, providing the results.

## How it Works

The script functions as follows:

1. Imports the `socket` library to perform DNS resolution.

2. Defines a function `get_ip_addresses(url)` that takes a URL as input and attempts to resolve both its IPv4 and IPv6 addresses. It returns the addresses if found or `None` if not.

3. In the main part of the script, it prompts the user to enter a URL.

4. It invokes the `get_ip_addresses(url)` function to obtain the IPv4 and IPv6 addresses.

5. It prints the results, informing the user whether IPv4 and/or IPv6 addresses were found or not.

## Usage# IP Address Resolver

This Python script is a simple utility to resolve both IPv4 and IPv6 addresses for a given URL (domain name) using the `socket` library. It allows you to enter a URL, and it attempts to find both IPv4 and IPv6 addresses, providing the results.

## How it Works

The script functions as follows:

1. Imports the `socket` library to perform DNS resolution.

2. Defines a function `get_ip_addresses(url)` that takes a URL as input and attempts to resolve both its IPv4 and IPv6 addresses. It returns the addresses if found or `None` if not.

3. In the main part of the script, it prompts the user to enter a URL.

4. It invokes the `get_ip_addresses(url)` function to obtain the IPv4 and IPv6 addresses.

5. It prints the results, informing the user whether IPv4 and/or IPv6 addresses were found or not.

## Usage

1. Clone this repository or download the script.

2. Ensure you have Python installed on your system.

3. Run the script.

4. Enter the URL for which you want to resolve IP addresses.

5. The script will provide the IPv4 and IPv6 addresses, if available.

## Prerequisites

- Python (tested on Python 3.6+)

## Author

- Dinesh P Bhadhrecha
