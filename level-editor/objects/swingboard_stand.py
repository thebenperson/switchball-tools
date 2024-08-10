from .. type import TYPE

from . sink_angular import SINK_ANGULAR

class SWINGBOARD_STAND(TYPE):

	SUPER = SINK_ANGULAR

	children = ((

		"SWINGBOARD",

		(0, 0, 45),
		(0, 0, 0.35)

	),)
