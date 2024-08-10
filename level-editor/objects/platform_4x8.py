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

from .. type  import TYPE

from .. bases.platform_small import PLATFORM_SMALL

class PLATFORM_4X8(TYPE):

	SUPER = PLATFORM_SMALL

	siblings = ((

		"ENGINE_SMALL",

		(0, 0, 45),
		(1.95, -1.94, 0.56)

	), (

		"ENGINE_SMALL",

		(0, 0, -45),
		(-1.98, -1.96, 0.55)

	), (

		"ENGINE_SMALL",

		(0, 0, -135),
		(-1.98, 1.95, 0.56)

	), (

		"ENGINE_SMALL",

		(0, 0, 135),
		(1.95, 1.95, 0.55)

	), (

		"EDGE_CORNER_SMALL",

		(0, 0, 0),
		(1.5, -1.5, 1.99)

	), (

		"EDGE_CORNER_SMALL_MIRROR",

		(0, 0, 0),
		(-1.5, -1.5, 1.99)

	), (

		"EDGE_CORNER_SMALL",

		(0, 0, 180),
		(-1.5, 1.5, 1.99)

	), (

		"EDGE_CORNER_SMALL_MIRROR",

		(0, 0, 180),
		(1.5, 1.5, 1.99)

	), (

		"EDGE_TWO",

		(0, 0, -90),
		(0, -1.88, 1.99)

	), (

		"EDGE_TWO",

		(0, 0, 180),
		(-1.88, 0, 1.99)

	), (

		"EDGE_TWO",

		(0, 0, 90),
		(0, 1.88, 1.99)

	), (

		"EDGE_TWO",

		(0, 0, 0),
		(1.88, 0, 1.99)

	))
