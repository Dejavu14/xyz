import json
import os
import os.path
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

print("==== Pilih Jenis Data ====")
print("1.Log To Json ")
print("2.Log To Plaintext")
print("==========================")

pilihan = input('Input Pilihan Anda:')

if pilihan == 'json':

    i = 1
    result = {}

    with open('/var/log/auth.log') as f:
        lines = f.readlines()
        for line in lines:
            r = line.split(':')
            result[i] = {'timestamp': r[0], 'name': r[1]}
            i += 1

    print(result)

    with open('data.json', 'w') as fp:
        json.dump(result, fp)


elif pilihan == 'plaintext':

    shutil.copyfile('/var/log/auth.log', '/var/log/authcopy.log')

    my_file = '/var/log/authcopy.log'

    base = os.path.splitext(my_file)[0]

    os.rename(my_file, base + '.txt')

else:
    shutil.copyfile('/var/log/auth.log', '/var/log/authcopy.log')

    my_file = '/var/log/authcopy.log'

    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.txt')

# STEP PENGGUNAAN
# 1. Masuk user root terlebih dahulu sebelum menjalankan file script.
# 2. Running file "LogWithCondition"
# 3. Pilih Data yaitu json atau plaintext untuk outputnya
