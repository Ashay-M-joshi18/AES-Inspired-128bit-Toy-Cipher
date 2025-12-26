import ecb

def test_encrypt_decrypt():
    key = "0123456789abcdef"  # 16 char key

    # Normal test cases
    normal_cases = [
        "Hello World",  # short
        "This is a test message for AES ECB encryption.",  # longer
        "A" * 16,  # exact block
        "A" * 15,  # one less
        "A" * 17,  # one more
        "Special chars: !@#$%^&*()",  # special chars
        "12345678901234567890123456789012",  # 32 chars
    ]

    for i, message in enumerate(normal_cases, 1):
        try:
            encrypted = ecb.encrypt_ecb(message, key)
            decrypted = ecb.decrypt_ecb(encrypted, key)
            assert message == decrypted, f"Round trip failed: Original '{message[:20]}...', Decrypted '{decrypted[:20]}...'"
            print(f"Test {i} passed: '{message[:20]}...' round trip successful")
        except Exception as e:
            print(f"Test {i} failed: {e}")

    # Edge cases that should raise exceptions
    # For empty message, encrypt should raise
    try:
        ecb.encrypt_ecb("", key)
        print("Test 8 failed: Should have raised ValueError for empty message")
    except ValueError as e:
        print(f"Test 8 passed: {e}")
    except Exception as e:
        print(f"Test 8 failed: Wrong exception {e}")

    # For invalid ciphertext, decrypt should raise
    try:
        ecb.decrypt_ecb("invalid", key)
        print("Test 9 failed: Should have raised exception for invalid ciphertext")
    except Exception as e:
        print(f"Test 9 passed: {e}")

    # For ciphertext not multiple of 32
    try:
        ecb.decrypt_ecb("a" * 30, key)
        print("Test 10 failed: Should have raised ValueError for length not multiple of 32")
    except ValueError as e:
        print(f"Test 10 passed: {e}")
    except Exception as e:
        print(f"Test 10 failed: Wrong exception {e}")

    # For non-hex ciphertext
    try:
        ecb.decrypt_ecb("gggggggggggggggggggggggggggggggg", key)  # 32 chars but not hex
        print("Test 11 failed: Should have raised exception for non-hex")
    except Exception as e:
        print(f"Test 11 passed: {e}")

if __name__ == "__main__":
    test_encrypt_decrypt()
    
