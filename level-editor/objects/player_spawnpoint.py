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

class PLAYER_SPAWNPOINT(TYPE, bpy.types.PropertyGroup):

	SUPER = EMPTY
	empty_type = "SPHERE"

	checkpoint_id: bpy.props.PointerProperty (

		name = "Checkpoint",
		type = bpy.types.Object

	)

	airball_can_spawn: bpy.props.BoolProperty (

		name = "Airball can spawn",
		default = False

	)

	default_ball: bpy.props.EnumProperty (

		name = "Default Ball",

		items = (

			( "marbleball", "Marbleball", "Marbleball" ),
			( "steelball",  "Metalball",  "Metalball"  ),
			( "airball",    "Airball",    "Airball"    ),
			( "powerball",  "Powerball",  "Powerball"  )

		)

	)

	first_spawnpoint: bpy.props.BoolProperty (

		name = "First spawn point",
		default = True

	)

	marbleball_can_spawn: bpy.props.BoolProperty (

		name = "Marbleball can spawn",
		default = False

	)

	order_number: bpy.props.IntProperty (

		name = "Order Number",
		default = 1, min = 1

	)

	powerball_can_spawn: bpy.props.BoolProperty (

		name = "Powerball can spawn",
		default = False

	)

	steelball_can_spawn: bpy.props.BoolProperty (

		name = "Steelball can spawn",
		default = False

	)

class PLAYER_SPAWNPOINT_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_PLAYER_SPAWNPOINT"
	bl_label  = "Player Spawnpoint Properties"

	type = PLAYER_SPAWNPOINT
