# Introduction
RSA step by step functions with Python

This is a step-by-step walkthrough of the commonly used and industry standard RSA algorithm using Python. The algorithm is used to send messages and information securely over the internet. For example if person A and person B want to exchange an encoded message. Person A sends person B their public key. Person B then encodes their response and sends it back to person A. Person A then decodes the message with their private key. This process is effective against criminals and anyone else wanting to read the message or information because only the public key is included in the message, any intersepted messages can only be encoded but it's a very difficult process to decode the original message without knowing the details of the encoding. The process uses large prime numbers that are very hard to factor, this is the key to the security.

# Steps
The three main steps of the process are 

- Generating the public and private keys
- Encoding the message
- Decoding the message

## Functions
Go to the RSA.py section to see my functions. The general flow is 
- Building blocks for the private and public keys (coverting the text to integers and the integers to strings)
- FME function
- Euclidean Algorith function
- Public key function (uses the Euclidean function)
- Private key function
- Encode function
- Decode function
