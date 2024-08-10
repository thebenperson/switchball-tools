from .. type import TYPE

from .. objects.model import MODEL

class PLATFORM(TYPE):

	SUPER = MODEL

	def model_set_materials(object):

		MODEL.set_material(object, 3, "PLATFORM_SIDE")
		MODEL.set_material(object, 4, "PLATFORM_FLOOR")
