# standard libs
import datetime
import hashlib
import os
import sys

# custom funcs
def expect_hexstr(hexstr):
    """
        Small function to wrap type checking for hexadecimal string
    """
    try:
        int(hexstr, 16)
    except ValueError:
        sys.exit('Method expects hexadecimal string as input')

def sha256(ingest):
    """
        Wrapper for sha256 hashlib function with included UTF-8 formatting and
        output in Hexadecimal (Base16)
    """
    return hashlib.sha256(ingest.encode('utf-8')).hexdigest()

def get_nonce_hash():
    """
        Simple utility function to generate a hashed_nonce from the environment
        variable NONCE
    """
    try:
        return sha256(os.environ['NONCE'])
    except KeyError:
        sys.exit('Must set environment variable \'NONCE\'')

def bitflip(digest):
    """
        Take in hexadecimal string, convert to int, flip, and return
    """
    # check that digest is string
    expect_hexstr(digest)

    # get lenght of hexadecimal string
    dgst_len = len(digest)

    # create hexadecimal mask string with length = digest_len
    mask_xstr = '0x' + ('F' * dgst_len)

    # convert mask string to integer
    mask_int = int(mask_xstr, 16)

    # convert digest hexstr to int
    dgst_int = int(digest, 16)

    # flip bits
    flipped_idgst = ~ dgst_int & mask_int

    # re-encode in hexadecimal
    flipped_xdgst = format(flipped_idgst, 'x')

    # give back
    return flipped_xdgst

def encode_dtime(digest):
    """
        Returns a hexadecimal string encoded with datetime
    """
    # check that digest is string
    expect_hexstr(digest)

    # get current datetime
    dt = datetime.datetime.now().strftime('%y%m%d%H%M')

    # convert dt to integer
    dt_int = int(dt, 10)

    # convert digest to int
    dgst_int = int(digest, 16)

    # encode dt_int to dgst_int
    enc_idgst = dgst_int + dt_int

    # re-encode in hexadecimal
    enc_xdgst = format(enc_idgst, 'x')

    # give back
    return enc_xdgst

def scramble_hash(digest):
    """
        Returns bit flipped and re-hashed hexadecimal string
    """
    # check that digest is string
    expect_hexstr(digest)

    # flip bits
    flipped_xdgst = bitflip(digest)

    # re-hash
    flip_n_hash = sha256(flipped_xdgst)

    # give back
    return flip_n_hash
