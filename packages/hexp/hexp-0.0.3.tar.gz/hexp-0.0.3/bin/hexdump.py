import os
from ctypes import *
import ctypes.util
from binascii import unhexlify
import time

def cprint_hex_w_unicode(data):
    libc = CDLL(ctypes.util.find_library("c"))
    for i in range(0, len(data), 16):
        libc.printf(b"%08x ", i)
        libc.printf(b"%s  %s |%s|\n", bytes(" ".join(data[i:i+8]), "ascii"), bytes(" ".join(data[i+8:i+16]), "ascii"), bytes(repr(unhexlify("".join(data[i:i+16])).decode("utf-8", "replace")), "utf-8"))

def cprint_hex_wout_unicode(data):
    libc = CDLL(ctypes.util.find_library("c"))
    for i in range(0, len(data), 16):
        libc.printf(b"%08x ", i)
        libc.printf(b"%s  %s\n", bytes(" ".join(data[i:i+8]), "ascii"), bytes(" ".join(data[i+8:i+16]), "ascii"))