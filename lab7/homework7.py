from tinyec import registry
import secrets
import ecdsa


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


if __name__ == '__main__':
    curve = registry.get_curve('secp521r1')

    # Alice's side -- ECDSA generation of keys
    ska = ecdsa.SigningKey.generate()  # Secret key (signing key)
    pka = ska.verifying_key  # Public key (verifying key)

    # Alice's side ECDH generation of keys
    alicePrivKey = secrets.randbelow(curve.field.n)
    alicePubKey = alicePrivKey * curve.g
    print("Alice public ECDH key:", compress(alicePubKey))

    # Bob's side -- ECDSA generation of keys
    skb = ecdsa.SigningKey.generate()  # Secret key (signing key)
    pkb = skb.verifying_key  # Public key (verifying key)

    # Bob's side -- ECDH generation of keys
    bobPrivKey = secrets.randbelow(curve.field.n)
    bobPubKey = bobPrivKey * curve.g
    print("Bob public ECDH key:", compress(bobPubKey))

    print("\nNow sign and exchange the public keys for ECDH and ECDSA.\n")

    signature_ecdh_b = skb.sign(bytes(compress(bobPubKey), 'utf-8'))
    signature_ecdh_a = ska.sign(bytes(compress(alicePubKey), 'utf-8'))

    # Alice verifying signature and creating shared key
    if pkb.verify(signature_ecdh_b, bytes(compress(bobPubKey), 'utf-8')):
        print("Signature of Bob's public key is correct.")
    aliceSharedKey = alicePrivKey * bobPubKey
    print("Alice shared key: {}".format(compress(aliceSharedKey)))

    # Bob verifying signature and creating shared key
    if pka.verify(signature_ecdh_a, bytes(compress(alicePubKey), 'utf-8')):
        print("Signature of Alice's public key is correct.")
    bobSharedKey = bobPrivKey * alicePubKey
    print("Bob shared key: {}".format(compress(bobSharedKey)))

    print("Equal shared keys:", aliceSharedKey == bobSharedKey)
