# CIDR

Classless Inter-Domain Routing (CIDR) (also known as slash notation) is an IP address allocation method. It provides a granual means of addressing IP networks.

Imagine you have a group of houses on a street. Instead of just saying "all the houses on this street," you can specify exactly which houses you mean by using a street name and a house number range. For example, "Maple Street, houses 10-20" would be more specific than just saying "Maple Street."

## IP's

`192.164.1.0`

Can be broken down into four parts, or octets, separated by a period.

`192` - `164` - `1` - `0`

Each octet is made up of 8 binary bits. This means these binary bits are either `0` or `1`.

`128.196.64.0`

`10000000.11000000.01000000.00000000`

The combinations inside each octets covers every number from 0 to 255.

Here is the format of the bits, in order:

`128` - `64` - `32` - `16` - `8` - `4` - `2` - `1`

Using this format:

`10000000` would be equal to 128.

`01000000` would be equal to 64.

`01100000` would be 64 + 32, equal to 96.

Therefore:

10000000.11000000.01000000.00000000 = 128.196.64.0

## CIDR

`192.168.2.64/26`

Here we have a prefix length (the number after the slash).

What does this `/26` mean?

Looking back at our understanding of IP addresses now. Here is the Subnet mask of this address:

Subnet Mask: `11111111.11111111.11111111.11000000`

IP Address :  `11000000.10101000.00000010.01000000`

Notice, the first 26 digits of the Subnet Mask are all 1's, with the remaining 6 (out of a total 32) being 0's.

This means that everything up to (and including) the 26th digit, on the left side, cannot be changed. It is a fixed network portion.

This means:
- The lowest usable Host address = `192.168.2.65`
  - cannot be the same as the network address (64).
- The highest usable Host address = `192.168.2.254`
  - cannot be the same as the broadcast address (255).
- All numbers in between these fixed numbers are usable IPs, and can be hosts.
- 
CIDR is simply the combination of an IP address with the subnet mask length. However, CIDR is more flexible, as the prefix length indicates exactly how many bits are used for the network portion. This allows for more precise control over subnetting.

1. Street Name: In CIDR, the street name is like the base IP address (e.g., 192.168.2.64).
2. House Number Range: The house number range is represented by a number after a slash (e.g., /26). It tells you how many houses are included.


So, "192.168.2.64/26" means all the addresses from 192.168.2.65 to 192.168.1.254.