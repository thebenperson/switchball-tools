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
import mathutils

import math
import sys
import inspect
import xml.etree.ElementTree as ET

from bpy_extras.io_utils import ImportHelper, ExportHelper

from .. panel import PANEL
from .. type  import TYPE

from .. bases.object import OBJECT

global_id_map = {}
global_id_map_reverse = {}

def menu_func_import(self, context):
	self.layout.operator(ImportLevel.bl_idname, text="Switchball Level (.vnl)")

def menu_func_export(self, context):
	self.layout.operator(ExportLevel.bl_idname, text="Switchball Level (.vnl)")

def set_property(object, name, value):

	cls = TYPE.map[object["type"]]

	while True:

		if name in cls.__annotations__: break

		try: cls = cls.SUPER
		except:

			print(f"WARNING: Unknown property \"{ name }\"")
			return

	match cls.__annotations__[name].function:

		case bpy.props.PointerProperty:

			if type(value) == int:

				global_id_map[value] = ( object, name )
				return

		case bpy.props.EnumProperty:

			value = str(value).lower()

	attr = getattr(object, cls.__name__)
	setattr(attr, name, value)

class ImportLevel(bpy.types.Operator, ImportHelper):

	bl_idname = "switchball_tools.import"
	bl_label  = "Import Level"

	filename_ext = ".vnl"

	def execute(self, context):

		try: root = ET.parse(self.filepath).getroot()
		except ET.ParseError:

			self.report({ "ERROR" }, "Could not parse level")
			return { "CANCELLED" }

		cls = TYPE.map["LEVEL"]
		level = cls.new(type = "LEVEL")
		cls.from_xml(level, root)

		for id, entry in global_id_map.items():

			try: target = global_id_map_reverse[id]
			except:

				print("Could not find object ID", id)
				continue

			set_property(entry[0], entry[1], target)

		return { "FINISHED" }

class ExportLevel(bpy.types.Operator, ExportHelper):

	bl_idname = "switchball_tools.export"
	bl_label  = "Export Level"

	filename_ext = ".vnl"

	def execute(self, context):

		global_id_map.clear()
		global_id_map_reverse.clear()
		id = 1

		for i in bpy.data.objects:

			try: type = i["type"]
			except: continue

			if type == "LEVEL": continue
			global_id_map_reverse[id] = i
			global_id_map[i] = id
			id += 1

		level = bpy.data.objects["SKYBOX"]
		cls   = TYPE.map[level["type"]]

		root = ET.Element("level")
		cls.to_xml(root, level)

		for i in bpy.data.objects:

			if i.parent: continue

			try: type = i["type"]
			except: continue

			if type == "LEVEL": continue
			newroot = ET.SubElement(root, "object")

			cls = TYPE.map[type]
			cls.to_xml(newroot, i)

		tree = ET.ElementTree(root)
		ET.indent(tree, space='\t')

		with open(self.filepath, "w") as file:
			tree.write(file, encoding = "unicode")

		return { "FINISHED" }

class LEVEL(TYPE, bpy.types.PropertyGroup):

	SUPER = OBJECT

	world_type: bpy.props.EnumProperty (

		items = (

			( "sky_world",    "Sky World",       "Sky World"       ),
			( "ice_world",    "Ice World",       "Ice World"       ),
			( "iceworld",     "Ice World (Old)", "Ice World (Old)" ),
			( "desert_world", "Desert World",    "Desert World"    ),
			( "cave_world",   "Cave World",      "Cave World"      ),
			( "cloud_world",  "Cloud World",     "Cloud World"     ),
			( "lava_world",   "Lava World",      "Lava World"      )

		),

		name        = "world_type",
		description = "World Type"

	)

	def new(**kwargs):

		mesh   = bpy.data.meshes.new("Basic_Cube")
		object = bpy.data.objects.new("SKYBOX", mesh)

		object.scale *= 200

		return __class__.next_new(object = object, **kwargs)

class LEVEL_PANEL(PANEL, bpy.types.Panel):

	bl_label  = "Level Properties"
	bl_idname = "OBJECT_PT_LEVEL"

	type = LEVEL
