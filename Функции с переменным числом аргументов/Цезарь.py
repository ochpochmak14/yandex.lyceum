def encrypt_caesar(msg, shift=3):
    encrypted_msg = []
    for char in msg:
        if 'А' <= char <= 'Я':
            encrypted_msg.append(chr((ord(char) - ord('А') + shift) % 32 + ord('А')))
        elif 'а' <= char <= 'я':
            encrypted_msg.append(chr((ord(char) - ord('а') + shift) % 32 + ord('а')))
        else:
            encrypted_msg.append(char)
    return ''.join(encrypted_msg)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)