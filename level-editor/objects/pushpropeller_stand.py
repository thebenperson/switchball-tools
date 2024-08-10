from .. type import TYPE

from . sink_angular import SINK_ANGULAR

class PUSHPROPELLER_STAND(TYPE):

	SUPER = SINK_ANGULAR

	children = ((

		"PUSHPROPELLER",

		(0, 0, 0),
		(0, -0.7, 0.41)

	),)
