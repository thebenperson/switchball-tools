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

class CAMERA_ZONEPOINT(TYPE, bpy.types.PropertyGroup):

	SUPER = EMPTY

	empty_type = "CUBE"
	empty_size = 0.1

	change_to_camera_mode: bpy.props.EnumProperty (

		items = (

			( "stationary", "Stationary", "Stationary camera mode" ),
			( "isometric",  "Isometric",  "Metalball camera mode"  ),
			( "chase",      "Chase",      "Follow the ball"        )

		),

		name        = "change_to_camera_mode",
		description = "Camera mode"

	)

	first_zone: bpy.props.BoolProperty (

		name = "first_zone",
		description = "First Zone",
		default = False

	)

	isometric_angle: bpy.props.EnumProperty(

		items = (

			(  "n", "North",     "Point north"     ),
			( "ne", "Northeast", "Point northeast" ),
			(  "e", "East",      "Point east"      ),
			( "se", "Southeast", "Point southeast" ),
			(  "s", "South",     "Point south"     ),
			( "sw", "Southwest", "Point southwest" ),
			(  "w", "West",      "Point west"      ),
			( "nw", "Northwest", "Point northwest" )

		),

		name        = "isometric_angle",
		description = "Isometric Angle"

	)

	zoom: bpy.props.EnumProperty(

		items = (

			( "close",  "Close",  "Close zoom"  ),
			( "normal", "Normal", "Normal zoom" ),
			( "far",    "Far",    "Far zoom"    )

		),

		name        = "zoom",
		description = "Camera zoom"

	)

class CAMERA_ZONEPOINT_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_CAMERA_ZONEPOINT"
	bl_label  = "Camera Zonepoint Properties"

	type = CAMERA_ZONEPOINT
