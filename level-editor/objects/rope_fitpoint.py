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

from . empty import EMPTY

class ROPE_FITPOINT(TYPE, bpy.types.PropertyGroup):

	SUPER = EMPTY

	empty_type = "SPHERE"
	empty_size = 0.2

	first_fitpoint: bpy.props.BoolProperty (

		name = "First fitpoint",
		default = True

	)

	next_fitpoint_id: bpy.props.PointerProperty (

		name = "Next fitpoint",
		type = bpy.types.Object

	)

	attached_to_id: bpy.props.PointerProperty (

		name = "Attached to",
		type = bpy.types.Object

	)

	mesh: bpy.props.StringProperty (

		name    = "Mesh to draw along rope",
		default = "rope_medium_medium.x"

	)

	slack: bpy.props.EnumProperty (

		name = "Rope slack",
		items = tuple([( "medium", "Medium", "Medium slack" )]),

		default = "medium"

	)

	num_links: bpy.props.IntProperty (

		name = "Number of links"

	)

class ROPE_FITPOINT_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_ROPE_FITPOINT"
	bl_label  = "Rope Properties"

	type = ROPE_FITPOINT
