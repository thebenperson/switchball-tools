import bpy

from .. panel import PANEL
from .. type  import TYPE

from . model import MODEL

class PROP(TYPE, bpy.types.PropertyGroup):

	SUPER = MODEL

	dynamic: bpy.props.StringProperty (

		name = "Collisions enabled",
		default = "true"

	)

	respawn: bpy.props.BoolProperty (

		name = "Respawn",
		default = False

	)

	cloth_collision: bpy.props.BoolProperty (

		name = "Interact with cloth",
		default = False

	)

	fluid_collision: bpy.props.BoolProperty (

		name = "Interact with fluids",
		default = False

	)

	keep_position: bpy.props.BoolProperty (

		name = "Keep position",
		default = False

	)

	types = (

		"BARREL_LARGE",
		"BARREL_MEDIUM",
		"BARREL_SMALL",

		"BOARD_CURVED",
		"BOARD_LARGE",
		"BOARD_MEDIUM",
		"BOARD_ONE_FIT",
		"BOARD_QUAD_FIT",
		"BOARD_SMALL",

		"MAGNET_IN_ROPE",

		"PLANK_LARGE",
		"PLANK_LOG",
		"PLANK_MEDIUM",
		"PLANK_SMALL",

		"TNT_CRATE",

		"WOODCRATE_LARGE",
		"WOODCRATE_MEDIUM",
		"WOODCRATE_SMALL"

	)

class MODEL_PROP(PANEL, bpy.types.Panel):

	bl_idname = "OBJECT_PT_PROP"
	bl_label  = "Prop Properties"

	type = PROP
