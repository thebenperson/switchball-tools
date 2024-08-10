import bpy

from . type import TYPE

class OBJECT_PT_SWITCHBALL_TOOLS(bpy.types.Panel):

	bl_idname = "OBJECT_PT_SWITCHBALL_TOOLS"
	bl_label  = "Switchball Properties"
	bl_space_type  = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context     = "object"

	def draw(self, context):

		self.layout.row().label(text = "Switchball Properties")

class PANEL:

	bl_space_type  = "PROPERTIES"
	bl_parent_id   = "OBJECT_PT_SWITCHBALL_TOOLS"
	bl_region_type = "WINDOW"
	bl_context     = "object"

	@classmethod
	def poll(cls, context):

		try: type = context.active_object["type"]
		except: return False

		derived = TYPE.map[type]
		return derived.issubclass(cls.type)

	def draw(self, context):

		for i in self.type.__annotations__:

			value = getattr(context.active_object, self.type.__name__)
			self.layout.row().prop(value, i)
