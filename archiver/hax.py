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

def extract(dir, input):

	path = pathlib.Path(dir)
	if not path.exists():

		print(f"Directory \"{ dir }\" does not exist", file = sys.stderr)
		return

	input = open(input, "rb")

	num_entries = struct.unpack("<I", input.read(4))[0]

	for i in range(num_entries):
		extract_entry(path, input)
