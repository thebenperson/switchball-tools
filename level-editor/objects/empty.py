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

from .. type import TYPE

from .. bases.object_world import OBJECT_WORLD

class EMPTY(TYPE):

	SUPER = OBJECT_WORLD

	types = (

		"CAMERA_LOOKAT",
		"FLUID_CONTACT",
		"LEVEL_FINISH_POINT"

	)

	def new(type, options, object):

		object = bpy.data.objects.new(type, None)

		try: object.empty_display_type = options.get("empty_type")
		except: pass

		try: object.empty_display_size = options.get("empty_size")
		except: pass

		return __class__.next_new(type, options, object)
