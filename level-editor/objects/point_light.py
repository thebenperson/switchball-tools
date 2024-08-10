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

class POINT_LIGHT(TYPE):

	SUPER = OBJECT_WORLD

	def new(type, options, object):

		light = bpy.data.lights.new(type, "POINT")
		light.energy = 30

		#color = tuple(self.properties[i].value for i in ("red", "green", "blue"))
		#light.color = color if color > (0, 0, 0) else (1, 1, 1)

		object = bpy.data.objects.new(type, light)
		return __class__.next_new(type, options, object)
