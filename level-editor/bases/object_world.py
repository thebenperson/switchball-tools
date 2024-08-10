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

from .. panel import PANEL
from .. type  import TYPE

from . object import OBJECT

class OBJECT_WORLD(TYPE, bpy.types.PropertyGroup):

	SUPER = OBJECT

	dynamic: bpy.props.EnumProperty (

		items = (

			("default", "Default", "Default Value"),
			("false", "False", "Disabled"),
			("true", "True", "Enabled")

		),

		name        = "dynamic",
		description = "Enable Physics",
		default     = "default"

	)

	respawn: bpy.props.BoolProperty (

		name        = "respawn",
		description = "Respawn on Delete",
		default     = False

	)

	def from_xml(object, root):

		id = int(root.get("id"))
		global_id_map_reverse[id] = object

		# (X, Y, Z, W) position vector
		pos = list(float(root.get("pos_" + xyz)) for xyz in "xzy")
		pos.append(1)

		# (X, Y, Z, W) basis vectors

		basis_x = list(float(root.get("right_" + xyz)) for xyz in "xzy")
		basis_x.append(1)

		basis_z = list(float(root.get("up_" + xyz)) for xyz in "xzy")
		basis_z.append(1)

		basis_y = list(float(root.get("forward_" + xyz)) for xyz in "xzy")
		basis_y.append(1)

		matrix = mathutils.Matrix([ basis_x, basis_y, basis_z, pos ])
		matrix.transpose()

		object.matrix_basis = matrix
		__class__.next_from_xml(object, root)

	def to_xml(root, object):

		root.set("type", object["type"])
		root.set("id", str(global_id_map[object]))

		basis = object.matrix_basis

		basis_x = basis.col[0][0:3]
		basis_x = (basis_x[0], basis_x[2], basis_x[1])

		basis_y = basis.col[2][0:3]
		basis_y = (basis_y[0], basis_y[2], basis_y[1])

		basis_z = basis.col[1][0:3]
		basis_z = (basis_z[0], basis_z[2], basis_z[1])

		pos = basis.col[3][0:3]
		pos = (pos[0], pos[2], pos[1])

		for i in range(3):
			root.set("right_" + "xyz"[i], str(basis_x[i]))

		for i in range(3):
			root.set("up_" + "xyz"[i], str(basis_y[i]))

		for i in range(3):
			root.set("forward_" + "xyz"[i], str(basis_z[i]))

		for i in range(3):
			root.set("pos_" + "xyz"[i], str(pos[i]))

		__class__.next_to_xml(root, object)

class OBJECT_WORLD_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_OBJECT_WORLD"
	bl_label  = "Object Properties"

	type = OBJECT_WORLD
