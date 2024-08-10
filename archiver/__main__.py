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

import sys

import batch

usage = f"Usage: { sys.argv[0] } [ c | x ] input output"

if len(sys.argv) != 4:

	print(usage)
	sys.exit()

match sys.argv[1]:

	case 'c': batch.create(sys.argv[3], sys.argv[2])
	case 'x': batch.extract(sys.argv[3], sys.argv[2])

	case _:

		print(usage)

