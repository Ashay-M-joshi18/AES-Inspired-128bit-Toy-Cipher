from ecb import encrypt_ecb, decrypt_ecb

def test_single_block():
    message = "HELLO_AES_TEST!"
    key = "THIS_IS_16_KEY"

    cipher = encrypt_ecb(message, key)
    plain = decrypt_ecb(cipher, key)

    assert plain.strip() == message
    print("✅ Single-block test passed")


def test_multi_block():
    message = "AES inspired cipher built for educational purposes"
    key = "THIS_IS_16_KEY"

    cipher = encrypt_ecb(message, key)
    plain = decrypt_ecb(cipher, key)

    assert plain.strip() == message
    print("✅ Multi-block test passed")


def test_empty_string():
    message = ""
    key = "THIS_IS_16_KEY"

    cipher = encrypt_ecb(message, key)
    plain = decrypt_ecb(cipher, key)

    assert plain.strip() == message
    print("✅ Empty-string test passed")


if __name__ == "__main__":
    print("Running tests...\n")
    test_single_block()
    test_multi_block()
    test_empty_string()
    print("\n🎉 All tests passed successfully")