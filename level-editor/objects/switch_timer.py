import bpy

from .. panel import PANEL
from .. type  import TYPE

from . sink import SINK

class SWITCH_TIMER(TYPE, bpy.types.PropertyGroup):

	SUPER = SINK

	children = ((

		"SWITCH_BUTTON",

		(0, 0, 0),
		(0, 0, 0)

	),)

	first_object_to_activate: bpy.props.PointerProperty (

		name = "First object to activate",
		type = bpy.types.Object

	)

	second_object_to_activate: bpy.props.PointerProperty (

		name = "Second object to activate",
		type = bpy.types.Object

	)

	third_object_to_activate: bpy.props.PointerProperty (

		name = "Third object to activate",
		type = bpy.types.Object

	)

	time: bpy.props.IntProperty(

		name = "Timer",

		subtype = "TIME_ABSOLUTE",
		default = 1, min = 1

	)

class SWITCH_TIMER_PANEL(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_SWITCH_TIMER"
	bl_label  = "Switch Properties"

	type = SWITCH_TIMER
