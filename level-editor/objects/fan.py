from .. type import TYPE

from . sink_angular import SINK_ANGULAR

class FAN(TYPE):

	SUPER = SINK_ANGULAR

	children = ((

		"FAN_PROPELLER",

		(180, 0, 0),
		(0, -0.33, 0.5)

	),)
