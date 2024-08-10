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

from . model import MODEL

class CANNON_FOOT(TYPE, bpy.types.PropertyGroup):

	SUPER = MODEL

	children = ((

		"CANNON_STAND",

		(0, 0, 0),
		(0, 0, 0.24)

	), (

		"CANNON_BARREL",

		(0, 0, 0),
		(0, 0, 1)

	), (

		"CANNON_LID",

		(0, 0, 180),
		(0, 0.56, 0.5)

	))

	behaviour: bpy.props.EnumProperty (

		name = "Behavior",

		items = (

			( "idle",      "Idle",      "Open"      ),
			( "locked",    "Locked",    "Closed"    ),
			( "auto_fire", "Auto Fire", "Auto Fire" ),
			( "locked",    "Locked",    "Closed"    )

		)

	)

class CANNON_FOOT_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_CANNON_FOOT"
	bl_label  = "Cannon Properties"

	type = CANNON_FOOT
