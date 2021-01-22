from random import randint
import math 


def known_primes(len_of_bit):

    defaults_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    maximum_prime = pow(2, len_of_bit + 1) - 1
    minimum_prime = pow(2, len_of_bit)

    while 1:
        p = randint(minimum_prime, maximum_prime)
        for num in defaults_prime:
            if p % num == 0:
                break
            if num == 53 and p % num != 0:
                return p

def nods(x, y):

    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y

def Rabin(p):

    k = int(math.log(p, 2))
    d = p - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        x = randint(1, p - 1)
        if nods(x, p) > 1:
            return False
        if pow(x, d, p) == 1 or pow(x, d, p) == (p - 1):
            continue
        else:
            pseudo = False
            for r in range(1, s):
                xr = pow(x, d * pow(2, r), p)
                if xr == p - 1:
                    pseudo = True
                elif xr == 1:
                    return False
            if not pseudo:
                return False
    return True


def primes(len_of_bit):

    print()
    while True:
        p = known_primes(len_of_bit)

        if Rabin(p):
            print("Prime number: " + str(hex(p)))
            break
        else:
            print("Not prime number: " + str(hex(p)))
            continue
    return p


def pair_of_key(len_of_bit):

    p = primes(len_of_bit)
    q = primes(len_of_bit)

    while p == q:
        q = primes(len_of_bit)

    n = p * q
    euler = (q - 1) * (p - 1)

    e = randint(2, (euler - 1))

    while nods(e, euler) != 1:
        e = randint(2, (euler - 1))

    d = pow(e, 1, euler)

    o_key = [e, n]
    s_key = [d, n]

    print("\np = {}".format(hex(p)), "\nq = {}".format(hex(q)), "\nn = {}".format(hex(n)), "\ne = {}".format(hex(e)), "\nd = {}".format(hex(d)))

    return [o_key, s_key]

print("\nAlice:")
A_keys = pair_of_key(512)
Ao_key = A_keys[0]
As_key = A_keys[1]

print("\nBob:\n\nCONFIDENTIAL KEY DISTRIBUTION PROTOCOL\n\nSender:")
so_key, ss_key = pair_of_key(512)
print("\n\nReceiver:")
receiver_o_key, receiver_s_key = pair_of_key(512)


def encrypt(texts, o_key):
    shifrtext = pow(texts, o_key[0], o_key[1])
    return shifrtext


def decrypt(shifrtext, s_key):
    decrypted_texts = pow(shifrtext, s_key[0], s_key[1])
    return decrypted_texts


def sign(texts, s_key):
    digital_sign = encrypt(texts, s_key)
    return digital_sign


def verify(texts, digital_sign, o_key):
    if texts == decrypt(digital_sign, o_key):
        return True
    else:
        return False


def send(texts, ss_key, receiver_o_key):
    shifrtext = encrypt(texts, receiver_o_key)
    digital_sign = sign(texts, ss_key)
    encrypted_digital_sign = encrypt(digital_sign, receiver_o_key)
    return shifrtext, encrypted_digital_sign


def receive(shifrtext_and_digital_sign, so_key, receiver_s_key):
    shifrtext, encrypted_digital_sign = shifrtext_and_digital_sign
    texts = decrypt(shifrtext, receiver_s_key)
    digital_sign = decrypt(encrypted_digital_sign, receiver_s_key)
    verification = verify(texts, digital_sign, so_key)
    return texts, verification



texts = randint(0, pow(2, 512 - 1))
print("\ntexts:", hex(texts))

sent_texts = send(texts, ss_key, receiver_o_key)
print("\nSent texts:\n\tEncrypted texts: {}\n\tEncrypted digital_sign: {}\n\n".format(hex(sent_texts[0]), hex(sent_texts[1])))
checked_texts = receive(sent_texts, so_key, receiver_s_key)
print("Received texts:\n\ttexts: {}\n\tVerification: {}\n\n".format(hex(checked_texts[0]), checked_texts[1]),"\n\nCONFIDENTIAL KEY DISTRIBUTION PROTOCOL WITH SITE\n\nSender:\n")
so_key, ss_key = pair_of_key(512) #Site
print("\n\nReceiver:")
receiver_o_key = [int(input("\tEnter public exponent: "), 16), int(input("\tEnter modulus: "), 16)]

texts = randint(0, pow(2, 512 - 1))
print("\ntexts:", hex(texts))

sent_texts = send(texts, ss_key, receiver_o_key)
print("\nSent texts:\n\tEncrypted texts: {}\n\tEncrypted digital_sign: {}".format(hex(sent_texts[0]), hex(sent_texts[1],)),"\n\tModulus: {}\n\tPublic exponent: {}\n\n".format(hex(so_key[1]), hex(so_key[0])))
