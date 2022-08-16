#!/bin/bash

index="6 0 1"

for i in $index; do
        ./src/xz/.libs/xz -k -L compression${i}.csv ubuntu-20.04.4-desktop-amd64.iso &
done
for i in $index; do
        ./src/xz/.libs/xz -k -d -L decompression${i}.csv ubuntu-20.04.4-desktop-amd64.iso.xz &
done