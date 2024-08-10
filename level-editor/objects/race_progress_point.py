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

class RACE_PROGRESS_POINT(TYPE, bpy.types.PropertyGroup):

	SUPER = EMPTY
	empty_type = "CUBE"

	order_number: bpy.props.IntProperty (

		name = "Order Number",
		default = 1, min = 1

	)

class RACE_PROGRESS_POINT_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_RACE_PROGRESS_POINT"
	bl_label  = "Race Progress Point Properties"

	type = RACE_PROGRESS_POINT
