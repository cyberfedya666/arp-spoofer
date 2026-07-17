# ARP Spoofer

ARP spoofing tool for MITM attacks. Redirects victim's traffic through your machine.

## Disclaimer

For educational purposes and authorized testing only. Only use on devices and networks you own or have permission to test.

## Requirements

Python 3.8+, scapy, Linux (root privileges).

## Installation

git clone https://github.com/cyberfedya666/arp-spoofer.git
cd arp-spoofer
pip install scapy

## Usage

Enable IP forwarding:

sudo sysctl -w net.ipv4.ip_forward=1

Run the spoofer:

sudo python3 arpspoof.py <victim_ip> <gateway_ip>

Example:

sudo python3 arpspoof.py 192.168.1.5 192.168.1.1

Stop with Ctrl+C. ARP tables will be restored.

## How it works

Sends fake ARP replies to the victim and the gateway. Victim thinks you are the gateway. Gateway thinks you are the victim. All traffic flows through you.

## License

MIT. For educational purposes.
