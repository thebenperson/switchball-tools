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

class GENERATOR(TYPE, bpy.types.PropertyGroup):

	SUPER = MODEL

	generate_to: bpy.props.EnumProperty (

		name = "Generate to",

		items = (

			( "boost",    "Boost",  "Boost"  ),
			( "jump",     "Jump",   "Jump"   ),
			( "magnetic", "Magnet", "Magnet" )

		)

	)

class GENERATOR_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_GENERATOR"
	bl_label  = "Generator Properties"

	type = GENERATOR
