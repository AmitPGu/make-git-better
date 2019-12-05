import os


def check_2fa_login(password):
    # Need to get env variable
    twofa_password = os.environ["TWO_FA"]

    # TODO here we'll check the 2FA password.
    # We need to check the 2FA password from the environment variable against the user-provided password. Also, I heard that using hashes is secure - let's do that!
    import hashlib
    m = hashlib.sha512()
    m.update(twofa_password.encode())
    n = hashlib.sha512()
    n.update(password.encode())
    return m.hexdigest() == n.hexdigest()

