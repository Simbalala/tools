import datetime
import hashlib
import os
import _thread
import time

begin_time = datetime.datetime.now()
salt = os.urandom(32)  # Remember this
password = '1234'

hash = hashlib.pbkdf2_hmac(
    'sha256',  # The hash digest algorithm for HMAC
    password.encode('utf-8'),  # Convert the password to bytes
    salt,  # Provide the salt
    100000  # It is recommended to use at least 100,000 iterations of SHA-256
)


def brutforce(nameThread, start, end):
    i = 0
    print("Start:" + nameThread + " " + str(datetime.datetime.now()))
    while(start <= end):
        # print(((i*100)/999999999))
        # brut = hashlib.pbkdf2_hmac(
        #     'sha256',  # The hash digest algorithm for HMAC
        #     str(i).encode('utf-8'),  # Convert the password to bytes
        #     salt,  # Provide the salt
        #     100000  # It is recommended to use at least 100,000 iterations of SHA-256
        # )
        if i == password:
            print(i)
            break
        i += 1
    if i != end:
        print(nameThread + " " + str(i))
        print(datetime.datetime.now() - begin_time)

# Define a function for the thread


# Create two threads as follows
try:
    _thread.start_new_thread(brutforce, ("Thread-1", 0, 249999999))
    # _thread.start_new_thread(brutforce, ("Thread-2", 249999999, 249999999*2))
    # _thread.start_new_thread(brutforce, ("Thread-3", 249999999*2, 249999999*3))
    # _thread.start_new_thread(brutforce, ("Thread-4", 249999999*3, 999999999))

except:
    print("Error: unable to start thread")

while 1:
    pass
