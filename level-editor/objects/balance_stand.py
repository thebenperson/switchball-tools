from .. type import TYPE

from . model import MODEL

class BALANCE_STAND(TYPE):

	SUPER = MODEL

	siblings = ((

		"BALANCE_LARGE",

		(0, 0, 0),
		(0, 0, 0.98)

	),)
