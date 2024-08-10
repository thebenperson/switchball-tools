from .. type import TYPE

from . sink_angular import SINK_ANGULAR

class FLOORFAN(TYPE):

	SUPER = SINK_ANGULAR

	children = ((

		"FLOORFAN_PROPELLER",

		(90, 0, 0),
		(0, 0, 0)

	),)
