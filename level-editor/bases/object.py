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

import bpy

from .. param import PARAM
from .. type  import TYPE

from .. objects.level import set_property

# Base class of all objects

class OBJECT(TYPE, bpy.types.PropertyGroup):

	def new(type, options, object):

		# set object type
		object["type"] = type

		# add object to scene
		bpy.context.collection.objects.link(object)
		return object

	# must be called after derived class constructor
	def from_xml(object, root):

		# parse properties tag

		properties = root.find("properties")
		if properties:

			for param in properties.findall("param"):

				param = PARAM.new(param)
				set_property(object, param.name, param.value)

		# add children of root tag

		for i in root.findall("object"):

			type = i.get("type")
			cls  = TYPE.map[type]

			child = cls.new(type = type)
			cls.from_xml(object = child, root = i)

			if root.tag == "object":
				child.parent = object

	def to_xml(root, object):

		bases = TYPE.bases(object)
		properties = ET.SubElement(root, "properties")

		for jj in bases:

			for name in jj.__annotations__:

				pp = getattr(object, jj.__name__)
				if not pp.is_property_set(name): continue

				value = getattr(pp, name)
				if value is None: continue

				data_type = type(value).__name__
				match data_type:

					case "bool":

						value = "true" if value else "false"

					case "Object":

						data_type = "int"
						value = str(global_id_map[value])

					case "str":

						data_type = "string"

					case _:

						value = str(value)

				param = ET.SubElement(properties, "param")

				param.set("name", name)
				param.set("value", value)
				param.set("data_type", data_type)

		if len(properties) == 0:
			root.remove(properties)

		for i in object.children:

			newrooot = ET.SubElement(root, "object")
			cls = TYPE.map[i["type"]]
			cls.to_xml(newrooot, i)

		return object
