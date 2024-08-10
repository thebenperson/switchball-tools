from .. type import TYPE

from . model import MODEL

class CHECKPOINT(TYPE):

	SUPER = MODEL

	siblings = ((

		"PLAYER_SPAWNPOINT",

		(0, 0, 0),
		(0, 0, 0.84)

	),)
