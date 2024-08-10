from .. type import TYPE

from . sink import SINK

class PUSHPOLE_STAND(TYPE):

	SUPER = SINK

	children = ((

		"PUSHPOLE",

		(0, 0, 0),
		(0, 0, 0.2)

	),)
