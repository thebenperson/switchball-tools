# Copyright (C) 2023-2024 Ben Stockett.
# This file is part of switchball-tools.

# switchball-tools is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.

# switchball-tools is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# switchball-tools. If not, see <https://www.gnu.org/licenses/>.

###############################################################################

import pathlib
import os
import struct
import sys

import fin

batch_magic = b"THIS IS A BATCH FILE"

def walk(input):

	for i in os.walk(input, topdown = False):

		# filter files
		if not i[2]: continue

		for file in i[2]:
			yield [ pathlib.Path(i[0], file), 0 ]

def create(output, input):

	output = open(output, "wb")

	output.write(batch_magic)
	output.write(bytes([0] * 12))

	files = tuple(walk(input))
	output.write(struct.pack("<I", len(files)))

	for i in files:

		# don't know the offset or size yet

		i[1] = output.tell()
		output.seek(8, 1)

		name = str(i[0].relative_to(input)).replace('/', '\\')

		output.write(struct.pack("<I", len(name)))
		output.write(name.encode("utf-8"))

	offset = output.tell()

	for i in files:

		output.seek(i[1])
		output.write(struct.pack("<I", offset))

		path = i[0]
		file = path.open("rb")

		size = path.stat().st_size

		compressed = bytes(fin.compress(read(file, size)))
		if len(compressed) < size:

			output.write(struct.pack("<I", len(compressed)))
			output.seek(offset)

			output.write(b"VNZ")
			output.write(struct.pack("<I", len(compressed)))
			output.write(struct.pack("<I", size))

			generator = (i for i in compressed)
			print(path, size, len(compressed))

		else:

			output.write(struct.pack("<I", size))
			output.seek(offset)

			file.seek(0)

			generator = read(file, size)
			print(path, size)

		generator = encrypt(generator)
		output.write(bytes(generator))

		offset = output.tell()

def extract(dir, input):

	path = pathlib.Path(dir)
	if not path.exists():

		print(f"Directory \"{ dir }\" does not exist", file = sys.stderr)
		return

	input = open(input, "rb")

	magic = input.read(len(batch_magic))
	if magic != batch_magic:

		print("Input is not a BATCH file", file = sys.stderr)
		return

	# skip padding
	input.seek(12, 1)

	num_entries = struct.unpack("<I", input.read(4))[0]

	for i in range(num_entries):
		extract_entry(path, input)

def extract_entry(dir, input):

	offset, size, path_size = struct.unpack("<3I", input.read(12))
	path = input.read(path_size).decode("utf-8")
	path = path.replace('\\', '/')

	position = input.tell()
	input.seek(offset)

	path = dir.joinpath(path)
	path.parent.mkdir(exist_ok = True, parents = True)

	if not size:

		path.touch()
		input.seek(position)
		return

	output = path.open(mode = "wb")

	generator = read(input, size)
	generator = decrypt(generator)

	vnz = input.read(3)
	if vnz == b"VNZ":

		compressed_size, uncompressed_size = struct.unpack("<2I", input.read(8))
		if compressed_size != size:

			print(f"Size mismatch { compressed_size } != { size }", file = sys.stderr)
			return

		size = uncompressed_size
		generator = fin.decompress(generator)

	else:

		input.seek(-3, 1)

	print(path, size)

	output.write(bytes(generator))
	input.seek(position)

def read(input, size):

	for i in range(size):
		yield input.read(1)[0]

def encrypt(input):

	last = 0

	for i in input:

		last = ((i + last) ^ 0x02) & 0xFF
		yield last

def decrypt(input):

	last = 0

	for i in input:

		yield ((i ^ 0x02) - last) & 0xFF
		last = i

