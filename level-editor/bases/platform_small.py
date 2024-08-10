from .. type  import TYPE
from .. objects.model import MODEL

from . platform import PLATFORM

class PLATFORM_SMALL(TYPE):

	SUPER = PLATFORM

	def model_set_materials(object):

		MODEL.set_material(object, 0, "PLATFORM_SMALL");
