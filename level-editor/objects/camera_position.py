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

from .. bases.object_world import OBJECT_WORLD

class CAMERA_POSITION(TYPE, bpy.types.PropertyGroup):

	SUPER = OBJECT_WORLD

	attached_to_zone_id: bpy.props.PointerProperty (

		type = bpy.types.Object,
		name = "Zone"

	)

	def new(type, **kwargs):

		camera = bpy.data.cameras.new(type)
		object = bpy.data.objects.new(type, camera)

		return __class__.next_new(object = object, type = type, **kwargs)

class CAMERA_POSITION_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_CAMERA_POSITION"
	bl_label  = "Camera Position Properties"

	type = CAMERA_POSITION
