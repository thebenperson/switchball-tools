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

class MORPH(TYPE, bpy.types.PropertyGroup):

	SUPER = MODEL

	children = ((

		"BAR_MEDIUM",

		(0, 180, 22.5),
		(-0.46, -0.23, 0.19)

	), (

		"BAR_MEDIUM",

		(0, 0, 157.5),
		(-0.46, 0.23, 0.11)

	), (

		"BAR_MEDIUM",

		(0, 0, 22.5),
		(0.46, 0.23, 0.11)

	), (

		"BAR_MEDIUM",

		(0, -180, -22.5),
		(0.46, -0.23, 0.19)

	))

	morph_to: bpy.props.EnumProperty (

		description = "Morph to",

		items = (

			( "marbleball", "Marbleball", "Marbleball" ),
			( "steelball",  "Steelball",  "Steelball"  ),
			( "airball",    "Airball",    "Airball"    ),
			( "powerball",  "Powerball",  "Powerball"  )

		)

	)

class MORPH_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_MORPH"
	bl_label  = "Morph Properties"

	type = MORPH
