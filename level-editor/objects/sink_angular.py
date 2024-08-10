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

from . sink import SINK

class SINK_ANGULAR(TYPE, bpy.types.PropertyGroup):

	SUPER = SINK

	rotation_direction: bpy.props.EnumProperty (

		name = "Rotation direction",

		items = (

			( "cw",  "Clockwise",         "Rotate clockwise"         ),
			( "ccw", "Counter Clockwise", "Rotate counter clockwise" )

		)

	)

	rotation_speed: bpy.props.EnumProperty (

		name = "Rotation Speed",

		items = (

			( "none",   "None",   "Disable rotation"    ),
			( "slow",   "Slow",   "Rotate slowly"       ),
			( "medium", "Medium", "Rotate medium speed" ),
			( "fast",   "Fast",   "Rotate fast"         )

		)

	)

class SINK_ANGULAR_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_SINK_ANGULAR"
	bl_label  = "Angular Sink Properties"

	type = SINK_ANGULAR
