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

import os
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:

	print(f"Usage: { sys.argv[0] } [ installation path ]")
	sys.exit()

objects = {}

for i in os.scandir(sys.argv[1] + "/data/bod/common/script/level"):

	if not i.is_file(): continue

	tree  = ET.parse(i)
	level = tree.getroot()

	for object in level.findall("object"):

		type = object.get("type")

		properties = object.find("properties")
		if not properties: continue

		for param in properties.findall("param"):

			name = param.get("name")
			data_type = param.get("data_type")

			try: entry = objects[type]
			except:

				entry = set()
				objects[type] = entry

			entry.add((name, data_type))

sets = set()

for set in objects.values():

	if set not in sets:
		sets.add(frozenset(set))

for i in sorted(sets, key = lambda n: len(n)):
	print(i)

