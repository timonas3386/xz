#!/bin/python3

import pandas as pd
KB = 1024
MB = 1024 * KB
GB = 1024 * MB

block_size = 64
block_num = 8 * GB // block_size
block_start = 0

blocks = [0] * block_num


def bytes_to_blocks(offset, length):
    """
    offset: starts to write
    length: length of write request
    return: how many blocks need to write
    """
    # check if offset is align 64
    num = 0
    region1 = 0
    remainder = offset % block_size
    if remainder != 0:
        region1 = block_size - remainder
        length -= region1
        if length <= 0:
            return 1
        num += 1
    num += length // block_size
    if length % block_size != 0:
        num += 1
    return num


def write_blocks(offset, length):
    global max_offset
    for i in range(length):
        blocks[offset + i] += 1


mode = ['compression', 'decompression']
comprssion_type = ['6', '0', '1']
for t in comprssion_type:
    max_offset = 0
    for m in mode:
        df = pd.read_csv(m + t + ".csv", delimiter=",")
        df.columns = ['offset', 'len']
        for index, row in df.iterrows():
            block_length = bytes_to_blocks(row['offset'], row['len'])
            block_offset = row['offset'] // block_size
            max_offset = max(max_offset, block_offset + block_length)
            block_offset = (block_start + block_offset) % block_num
            write_blocks(block_offset, block_length)
    block_start = (max_offset + 1) % block_num
with open("block_count.txt", "w") as f:
    for i in blocks:
        f.write(str(i) + "\n")
