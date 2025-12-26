AES-Inspired 128-bit Toy Cipher (ECB Mode)
Overview
This project is an educational, AES-inspired 128-bit block cipher implemented in Python.
It closely follows the structural design of AES-128 (state representation, round structure, key expansion, and transformations) while intentionally simplifying certain aspects for learning purposes.
The implementation supports ECB (Electronic Codebook) mode and includes both encryption and decryption, along with input validation and test coverage.
Project Goals
Understand the internal working of AES-like block ciphers
Implement AES round transformations step-by-step
Learn key expansion (key schedule) mechanics
Practice clean code organization and testing
Demonstrate cryptography fundamentals in a resume-ready project
Features
128-bit block size (16 bytes)
AES-style state matrix (column-major order)
AES-based S-Box and Inverse S-Box
SubBytes / InvSubBytes
ShiftRows / InvShiftRows
MixColumns / InvMixColumns (GF(2⁸) arithmetic)
AddRoundKey
AES-like Key Expansion (11 round keys)
Proper AES round structure:
Pre-round AddRoundKey
9 full rounds
Final round without MixColumns
ECB mode encryption and decryption
Input validation and exception handling
Unit-style test cases
File Structure
core.py – Core cryptographic primitives (S-Box, GF math, state transforms)
key_schedule.py – AES-inspired key expansion logic
ecb.py – ECB encryption and decryption implementation
io_utils.py – Input handling, block splitting, validation
test.py – Functional and edge-case tests
README.md – Project documentation
How It Works (High Level)
Plaintext is split into 16-byte blocks
Each block is converted into a 4×4 state matrix
A master key is expanded into 11 round keys
Encryption applies:
Pre-round AddRoundKey
9 rounds of SubBytes → ShiftRows → MixColumns → AddRoundKey
Final round without MixColumns
Decryption reverses the process using inverse operations
ECB mode concatenates encrypted blocks without chaining
Usage
Encryption
Input: plaintext string + 16-character key
Output: hexadecimal ciphertext string
Decryption
Input: hexadecimal ciphertext + same key
Output: original plaintext
Testing
The project includes a test suite that validates:
Normal encryption/decryption round-trips
Exact, short, and multi-block inputs
Invalid inputs (empty message, invalid hex, wrong length)
Edge-case handling
Important Notes
This is not a production-secure implementation
ECB mode is insecure for real-world usage
Padding is simplified for learning clarity
The cipher is intended strictly for educational and demonstration purposes
Learning Outcomes
Practical understanding of AES internals
Experience with finite field arithmetic
Clean modular Python design
Defensive programming with exceptions
Writing cryptography-focused tests
Future Improvements
Add CBC or CTR mode
Implement standard PKCS#7 padding
Support byte-level inputs
Add performance benchmarks
Extend to AES-192 / AES-256 structures
Disclaimer
This project is an AES-inspired toy cipher, not a full AES implementation.
It should not be used to protect real data.
Author
Ashay Mukund Joshi
Electronics & Telecommunication Engineering
Aspiring Software / FinTech Engineer