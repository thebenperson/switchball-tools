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

import math
import struct
import sys

from .. type  import TYPE

from .. bases.object_world import OBJECT_WORLD

def use_hd_models():
	return bpy.context.preferences.addons["switchball-level-editor"].preferences.use_hd_models

def install_path():
	return bpy.context.preferences.addons["switchball-level-editor"].preferences.install_path

###############################################################################

# Base class for objects that have a 3D model

class MODEL(TYPE):

	SUPER = OBJECT_WORLD

	types = (

		"BALANCE_LARGE",

		"BALL_HOLDER",

		"BAR_HOLDER",
		"BAR_MEDIUM",
		"BAR_SMALL",

		"BRIDGE_2X2",
		"BRIDGE_2X4",

		"BRIDGE_BEND_2X2",
		"BRIDGE_BEND_3X3",
		"BRIDGE_BEND_4X4",

		"BRIDGE_BENT_SLOPE_3X3",
		"BRIDGE_BENT_SLOPE_4X4",

		"BRIDGE_END",
		"BRIDGE_HALFPIPE",

		"BRIDGE_SLOPE_18",
		"BRIDGE_SLOPE_18_END",
		"BRIDGE_SLOPE_18_START",
		"BRIDGE_SLOPE_26",
		"BRIDGE_SLOPE_26_END",
		"BRIDGE_SLOPE_26_START",
		"BRIDGE_SLOPE_45",
		"BRIDGE_SLOPE_45_END",
		"BRIDGE_SLOPE_45_START",

		"BRIDGE_STAIRS",

		"CANNON_BARREL",
		"CANNON_LID",
		"CANNON_STAND",

		"EDGE_CORNER_LARGE",
		"EDGE_CORNER_MEDIUM",
		"EDGE_CORNER_SMALL",

		"EDGE_CORNER_SMALL_MIRROR",

		"EDGE",
		"EDGE_ONE",
		"EDGE_TWO",

		"FAN_PROPELLER",
		"FLOORFAN_PROPELLER",

		"GYROCOPTER_PROPELLER",

		"LAMP_QUAD",
		"LAMP_SMALL",

		"MAST",
		"MELTER",
		"MORPH",
		"PIPE_BEND",
		"PIPE_BEND_SHORT",
		"PIPE",
		"PIPE_START",
		"POLE",
		"POLE_KNOB",
		"POLE_POST",
		"PUMP",
		"PUSHPOLE",
		"PUSHPOLE_STAND",
		"PUSHPROPELLER",
		"PUSHPROPELLER_STAND",
		"RAIL_BEND",
		"RAIL",
		"RAIL_END",
		"RAIL_SLOPE",
		"SWINGBOARD",
		"SWINGPOLE",
		"SWITCH_BUTTON",
		"TRENCH_BEND",
		"TRENCH",
		"TRENCH_SLOPE_DOWN",
		"TRENCH_SLOPE_UP",
		"WALL"

	)

	def new(type, options, object):

		# try to use cached mesh first

		try: object = bpy.data.objects.new(type, bpy.data.meshes[type])
		except: pass

		if object is not None:
			return __class__.next_new(type, options, object)

		file = open(f'{ install_path() }/data/bod/common/render/model/rm_{ type.lower() }{ "_hd" if use_hd_models() else "" }.aem', "rb")

###############################################################################

		# read file header

		# check if is a model file
		# TODO: make operator fail instead of crashing

		if file.read(8) != b"\x00\x00\x00\x000MEA":

			print(f"File \"{ path }\" is not a AEM file")
			sys.exit(0)

		file_size  = struct.unpack("<I", file.read(4))[0]
		dimensions = struct.unpack("<10f", file.read(40))

###############################################################################

		vertex_count  = struct.unpack("<I", file.read(4))[0]
		vertex_size   = struct.unpack("<I", file.read(4))[0]
		vertex_offset = struct.unpack("<I", file.read(4))[0]

###############################################################################

		zero = struct.unpack("<I", file.read(4))[0]

		vertex_order_size   = struct.unpack("<I", file.read(4))[0]
		vertex_order_offset = struct.unpack("<I", file.read(4))[0]

###############################################################################

		material_count  = struct.unpack("<I", file.read(4))[0]
		material_offset = struct.unpack("<I", file.read(4))[0]

		zero = struct.unpack("<I", file.read(4))[0]

		if material_count == 0: material_count = 1

###############################################################################

		verticies = []
		faces     = []
		uvs       = []
		colors    = []
		groups    = []

		for i in range(material_count):
			groups.append([])

		file.seek(vertex_offset);
		for i in range(vertex_count):

			vertex = struct.unpack(f"<5f", file.read(20))
			color  = struct.unpack(f"<4B", file.read(4))

			file.read(vertex_size - 28)

			material = struct.unpack(f"<I", file.read(4))[0]
			verticies.append((vertex[0], vertex[2], vertex[1]))

			uvs.append((vertex[3], 1 - vertex[4]))

			colors.append(color)
			groups[material].append(i)

		file.seek(vertex_order_offset);
		for i in range(vertex_order_size // 6):

			face = struct.unpack(f"<3H", file.read(6))
			faces.append((face[0], face[2], face[1]))

###############################################################################

		mesh = bpy.data.meshes.new(type)  # add the new mesh
		mesh.from_pydata(verticies, [], faces)

		uv = mesh.uv_layers.new(name="uv")

		for i in mesh.loops:
			uv.data[i.index].uv = uvs[i.vertex_index]

		color_layer = mesh.vertex_colors.new()

		for i in mesh.loops:
			color_layer.data[i.index].color = colors[i.vertex_index];

		object = bpy.data.objects.new(type, mesh)

		for i in range(material_count):

			g = object.vertex_groups.new(name = f"Group { i + 1 }")
			g.add(groups[i], 1, "REPLACE")

		was_set = False
		target = options

		while True:

			if hasattr(target, "model_set_materials"):

				target.model_set_materials(object)
				was_set = True

			try: target = target.SUPER
			except: break

		if not was_set:

			material_name = type
			material_name = material_name.removesuffix("_MIRROR")

			if options.get("model_sized"):

				material_name = material_name.removesuffix("_LARGE")
				material_name = material_name.removesuffix("_MEDIUM")
				material_name = material_name.removesuffix("_SMALL")

			MODEL.set_material(object, 0, material_name)

		return __class__.next_new(type, options, object)

	def set_group(object, idx):

		for polygon in object.data.polygons:

			if all([ all([ idx in [ g.group for g in i ] ]) for i in [ object.data.vertices[i].groups for i in polygon.vertices ] ]):

				polygon.material_index = len(object.data.materials) - 1

	def set_material(object, idx, name):

		print("set_material(" + str(idx) + ", " + name + ')')

		mat = bpy.data.materials.get(name)
		if mat is not None:

			object.data.materials.append(mat)
			if idx: MODEL.set_group(object, idx)

			return

		# load texture from file or cache

		try:

			texture = bpy.data.images.load (

				f"{ install_path() }/data/bod/common/render/texture/d_{ name.lower() }.dds",
				check_existing = True

			)

		except: texture = None

		if texture is None:

			try:

				texture = bpy.data.images.load (

					f"{ install_path() }/data/bod/shared1/render/texture/d_{ name.lower() }.dds",
					check_existing = True

				)

			except: pass

		if texture is None:

			try:

				texture = bpy.data.images.load (

					f"{ install_path() }/data/bod/sky_world/render/texture/d_{ name.lower() }.dds",
					check_existing = True

				)

			except: pass

		# create a new material

		mat = bpy.data.materials.new(name = name)
		mat.use_nodes = True

		output = mat.node_tree.nodes.get("Principled BSDF")

		# used for ambient occlusion
		color = mat.node_tree.nodes.new("ShaderNodeVertexColor")

		mix = mat.node_tree.nodes.new("ShaderNodeMixRGB")
		mix.blend_type = "MULTIPLY"
		mix.inputs[0].default_value = 1

		input = mat.node_tree.nodes.new("ShaderNodeTexImage")
		input.image = texture

		mat.node_tree.links.new(mix.inputs[1], color.outputs[0])
		mat.node_tree.links.new(mix.inputs[2], input.outputs[0])

		mat.node_tree.links.new(output.inputs[0], mix.outputs[0])

		object.data.materials.append(mat)
		if idx: MODEL.set_group(object, idx)


