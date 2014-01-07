# Copyright 2013 Philip N. Klein
# Edited 20140106 by David Prager Branner

def dict2list(dct, keylist):
    return [dct[i] for i in keylist if i in dct]

def list2dict(L, keylist):
    return {i:j for i, j in zip(keylist, L)}

def listrange2dict(L):
    return {i:j for i, j in enumerate(L)}
