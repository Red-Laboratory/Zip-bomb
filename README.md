# 💥 Zip bomb (ضغط القنبلة) ![](https://img.shields.io/apm/l/vim-mode)

![plot](./Screenshots/zipbomb_logo.jpg)

## What is it?

A zip bomb, also known as a decompression bomb  is a malicious archive file designed to crash or render useless the program or system reading it. It is often employed to disable antivirus software, in order to create an opening for more traditional malware.

A zip bomb allows a program to function normally, but, instead of hijacking the program's operation, creates an archive that requires an excessive amount of time, disk space, or memory to unpack.

## Usage:
`python3 ZipBomb_generator.py num_of_levels out_zip_file`

## How to create one?

To build a zip bomb you need to execute the python script:

`python3 ZipBomb_generator.py 10 bomb.zip` ('1' = 1.000.000 GB, i.e. '10' = 10.000.000 GB = 10.000 PB).

![plot](./Screenshots/zipbomb_1.png)

## Warning:

This zip file can hurt your system, you must understand all risks before doing anything. I don't want it to hurt anyone - it's here for analysis and tests which makes on prepared machines.

##
All material in this repository is in the public domain.
