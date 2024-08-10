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

# predictive compression algorithm
# the next byte is defined by the hash of the last two bytes

table = bytearray(0x8000)

def hash(b0, b1):

	return (b0 << 7) ^ b1

def compress(input):

	# assume space is the most common value

	for i in range(len(table)):
		table[i] = 0x20

	buffer = [ 0 ] * 8

	b0 = 0
	b1 = 0

	while True:

		mask = 0
		buffer_size = 0

		for i in range(8):

			index = hash(b0, b1)
			b0 = b1

			try: b1 = next(input)
			except StopIteration: break

			if table[index] == b1:

				# set mask bit
				mask |= (1 << i)

			else:

				table[index] = b1

				buffer[buffer_size] = b1
				buffer_size += 1

		if not i: break
		yield mask

		for i in range(buffer_size):
			yield buffer[i]

def decompress(input):

	# assume space is the most common value

	for i in range(len(table)):
		table[i] = 0x20

	b0 = 0
	b1 = 0

	while True:

		try: mask = next(input)
		except StopIteration: return

		for i in range(8):

			index = hash(b0, b1)
			b0 = b1

			if mask & (1 << i):

				b1 = table[index]

			else:

				try: b1 = next(input)
				except StopIteration: return

				table[index] = b1

			yield b1

