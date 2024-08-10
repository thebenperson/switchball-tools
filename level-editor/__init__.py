# Copyright (C) 2023-2024 Ben Stockett.
# This file is part of switchball-tools.

# switchball-tools is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.

# switchball-tools is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# switchball-tools. If not, see <https://www.gnu.org/licenses/>.

###############################################################################

bl_info = {
	"name": "Switchball Level Editor",
	"author": "Ben Stockett",
	"version": (0, 1),
	"blender": (2, 80, 0),
	"location": "View3D > Add > Mesh > New Object",
	"description": "Switchball Level Editor",
	"doc_url": "https://github.com/thebenperson/switchball-tools",
	"category": "3D View"
}

import bpy

import importlib
import inspect
import math
import os
import pkgutil

from . type  import TYPE
from . panel import OBJECT_PT_SWITCHBALL_TOOLS

from . import objects

###############################################################################

class SWITCHBALL_TOOLS_addon_preferences(bpy.types.AddonPreferences):

	bl_idname = __name__

	install_path: bpy.props.StringProperty (

		description = "Game Install Path",
		subtype     = "DIR_PATH"

	)

	use_hd_models: bpy.props.BoolProperty (

		description = "Use HD models (Switchball HD Only)",

	)

	def draw(self, context):

		row = self.layout.row()
		row.prop(self, "install_path",  text = "Game Install Path")
		row.prop(self, "use_hd_models", text = "Use HD Models")

###############################################################################

# Dropdown menu
# View3D > Add > Switchball

class SWITCHBALL_TOOLS_MT_add(bpy.types.Menu):

	bl_idname = "SWITCHBALL_TOOLS_MT_add"
	bl_label  = "Switchball"

	def menu(self, cls):

		self.layout.menu(cls.bl_idname, icon = cls.icon)

	def draw(self, context):

		self.menu(SWITCHBALL_TOOLS_MT_add_balls)
		self.menu(SWITCHBALL_TOOLS_MT_add_decoration)
		self.menu(SWITCHBALL_TOOLS_MT_add_props)
		self.menu(SWITCHBALL_TOOLS_MT_add_building)
		self.menu(SWITCHBALL_TOOLS_MT_add_large)
		self.menu(SWITCHBALL_TOOLS_MT_add_active)
		self.menu(SWITCHBALL_TOOLS_MT_add_mechanics)
		self.menu(SWITCHBALL_TOOLS_MT_add_meta)
		self.menu(SWITCHBALL_TOOLS_MT_add_unsupported)

def draw_item(self, context):

	self.layout.menu(SWITCHBALL_TOOLS_MT_add.bl_idname)

###############################################################################

# Base class for dropdown menu items

class SWITCHBALL_TOOLS_MT_add_impl:

	def draw(self, context):

		for i in range(len(self.items)):

			if i: self.layout.separator()

			items = self.items[i]

			if not isinstance(items, tuple):
				items = (items,)

			for type in items:

				operator = self.layout.operator (

					"switchball_tools.add",
					text = type,
					icon = "ADD"

				)

				operator.type = type

###############################################################################

class SWITCHBALL_TOOLS_MT_add_balls (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_balls"
	bl_label  = "Balls"

	icon = "META_BALL"

	items = ((

		"AIRBALL",
		"AIRBALL_HOLO"

	), (

		"BALOON"

	), (

		"CANNONBALL_LARGE",
		"CANNONBALL_MEDIUM",
		"CANNONBALL_SMALL"

	), (

		"MARBLEBALL",
		"MARBLEBALL_GHOST",
		"MARBLEBALL_HOLO"

	), (

		"METALBALL",
		"METALBALL_HOLO"

	), (

		"POWERBALL",
		"POWERBALL_HOLO"

	), (

		"SPHERE"

	), (

		"STONEBALL_LARGE",
		"STONEBALL_MEDIUM",
		"STONEBALL_SMALL"

	))

###############################################################################

class SWITCHBALL_TOOLS_MT_add_props (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_props"
	bl_label  = "Props"

	icon = "PHYSICS"

	items = ((

		"BARREL_LARGE",
		"BARREL_MEDIUM",
		"BARREL_SMALL"

	), (

		"BOARD_CURVED",
		"BOARD_LARGE",
		"BOARD_MEDIUM",
		"BOARD_ONE_FIT",
		"BOARD_QUAD_FIT",
		"BOARD_SMALL"

	),

	(

		"METALCRATE_LARGE",
		"METALCRATE_MEDIUM",
		"METALCRATE_SMALL"

	), (

		"PLANK_LARGE",
		"PLANK_LOG",
		"PLANK_MEDIUM",
		"PLANK_SMALL"

	), (

		"WOODCRATE_LARGE",
		"WOODCRATE_MEDIUM",
		"WOODCRATE_SMALL"

	))

###############################################################################

class SWITCHBALL_TOOLS_MT_add_decoration (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_decoration"
	bl_label  = "Decoration"

	icon = "DECORATE"

	items = ((

		"BAR_HOLDER",
		"BAR_MEDIUM",
		"BAR_SMALL"

	), (

		"EDGE",
		"EDGE_ONE",
		"EDGE_TWO"

	), (

		"EDGE_CORNER_LARGE",
		"EDGE_CORNER_LARGE_MIRROR",
		"EDGE_CORNER_MEDIUM",
		"EDGE_CORNER_MEDIUM_MIRROR",
		"EDGE_CORNER_SMALL",
		"EDGE_CORNER_SMALL_MIRROR"

	), (

		"ENGINE_LARGE",
		"ENGINE_SMALL"

	), (

		"LAMP_QUAD",
		"LAMP_SMALL"

	), (

		"MAST"

	), (

		"NAIL_LARGE",
		"NAIL_MEDIUM",
		"NAIL_SMALL"

	), (

		"POLE",
		"POLE_KNOB",
		"POLE_POST"

	), (

		"ROPE_MEDIUM_MEDIUM"

	), (

		"WIRE"

	))

###############################################################################

class SWITCHBALL_TOOLS_MT_add_building (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_building"
	bl_label  = "Building Elements"

	icon = "MOD_BUILD"

	items = ((

		"PLANK_LOG"

	), (

		"RAIL",
		"RAIL_BEND",
		"RAIL_END",
		"RAIL_SLOPE"

	), (

		"WALL"

	))

###############################################################################

class SWITCHBALL_TOOLS_MT_add_large (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_large"
	bl_label  = "Large Elements"

	icon = "WORLD"

	items = ((

		"BRIDGE_2X2",
		"BRIDGE_2X4",
		"BRIDGE_BEND_2X2",
		"BRIDGE_BEND_3X3",
		"BRIDGE_BEND_4X4",
		"BRIDGE_BENT_SLOPE_LEFT_3X3",
		"BRIDGE_BENT_SLOPE_LEFT_4X4",
		"BRIDGE_BENT_SLOPE_RIGHT_3X3",
		"BRIDGE_BENT_SLOPE_RIGHT_4X4",
		"BRIDGE_END",
		"BRIDGE_HALFPIPE",
		"BRIDGE_SLOPE_18",
		"BRIDGE_SLOPE_18_END",
		"BRIDGE_SLOPE_18_START",
		"BRIDGE_SLOPE_26",
		"BRIDGE_SLOPE_26_END",
		"BRIDGE_SLOPE_26_START",
		"BRIDGE_SLOPE_45",
		"BRIDGE_SLOPE_45_END",
		"BRIDGE_SLOPE_45_START",
		"BRIDGE_STAIRS"

	), (

		"PIPE",
		"PIPE_BEND",
		"PIPE_BEND_SHORT",
		"PIPE_GLASS",
		"PIPE_GLASS_BEND",
		"PIPE_GLASS_BEND_SHORT",
		"PIPE_GLASS_START",
		"PIPE_START"

	), (

		"PLATFORM_10X12",
		"PLATFORM_12X12",
		"PLATFORM_4X12",
		"PLATFORM_4X4",
		"PLATFORM_4X8",
		"PLATFORM_6X12",
		"PLATFORM_6X6",
		"PLATFORM_6X8",
		"PLATFORM_8X12",
		"PLATFORM_8X8"

	), (

		"TRENCH",
		"TRENCH_BEND",
		"TRENCH_SLOPE_DOWN",
		"TRENCH_SLOPE_UP"

	))

###############################################################################

# active elements

class SWITCHBALL_TOOLS_MT_add_active (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_active"
	bl_label  = "Active Elements"

	icon = "SETTINGS"

	items = ((

		"CHECKPOINT"

	), (

		"GENERATOR",
		"BALL_HOLDER"

	), (

		"MORPH"

	), (

		"PUMP"

	))

###############################################################################

# mechanics

class SWITCHBALL_TOOLS_MT_add_mechanics (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_mechanics"
	bl_label  = "Game Mechanics"

	icon = "LIGHT"

	items = ((

		"BALANCE_LARGE",
		"BALANCE_STAND"

	), (

		"CANNON_BARREL",
		"CANNON_FOOT",
		"CANNON_LID",
		"CANNON_STAND"

	), (

		"CLOTH"

	), (

		"FAN",
		"FAN_PROPELLER"

	), (

		"FLOORFAN",
		"FLOORFAN_PROPELLER"

	), (

		"GYROCOPTER",
		"GYROCOPTER_PROPELLER"

	), (

		"HOVER_LARGE",
		"HOVER_SMALL"

	), (

		"MAGNET",
		"MAGNET_IN_ROPE"

	), (

		"PUSHPOLE",
		"PUSHPOLE_STAND"

	), (

		"PUSHPROPELLER",
		"PUSHPROPELLER_STAND"

	), (

		"SKYBOX"

	), (

		"SWINGBOARD",
		"SWINGBOARD_STAND"

	), (

		"SWINGPOLE",
		"SWINGPOLE_STAND"

	), (

		"SWITCH_BUTTON",
		"SWITCH_TIMER",
		"SWITCH_TOGGLE",
		"SWITCH_TRIGGER"

	))

###############################################################################

class SWITCHBALL_TOOLS_MT_add_unsupported (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_unsupported"
	bl_label  = "Unsupported Objects"

	icon = "ERROR"

	items = ((

		"ARROW_HELPER"

	), (

		"CHECKPOINT_OLD"

	), (

		"FLUID_CONTACT",
		"FLUID_EMITTER"

	), (

		"MELTBALL",
		"MELTER"

	), (

		"MENU_BOARD",
		"MENU_BOX"

	), (

		"TNTCRATE_LARGE",
		"TNTCRATE_MEDIUM",
		"TNTCRATE_SMALL"

	), (

		"WATERCANNON_BARREL",
		"WATERCANNON_FOOT",
		"WATERCANNON_LID",
		"WATERCANNON_STAND",
		"WATERCANNON_TANK"

	), (

		"WATERTANK",
		"WATERTANK_TAP"

	), (

		"WATERWHEEL",
		"WATERWHEEL_GEARWHEEL",
		"WATERWHEEL_GENERATOR",
		"WATERWHEEL_STAND"

	))

###############################################################################

# meta

class SWITCHBALL_TOOLS_MT_add_meta (

	SWITCHBALL_TOOLS_MT_add_impl,
	bpy.types.Menu

):

	bl_idname = "SWITCHBALL_TOOLS_MT_add_meta"
	bl_label  = "Meta Objects"

	icon = "EMPTY_AXIS"

	items = ((

		"ACHIEVEMENT_TRIGGER"

	), (

		"CAMERA_LOOKAT",
		"CAMERA_POSITION",
		"CAMERA_WAYPOINT",
		"CAMERA_ZONEPOINT"

	), (

		"CLOTH_FITPOINT",
		"ROPE_FITPOINT"

	), (

		"LEVEL_FINISH_POINT",
		"PLAYER_SPAWNPOINT"

	), (

		"OBJECT_SPAWNPOINT"

	), (

		"POINT_LIGHT"

	), (

		"RACE_PROGRESS_POINT",
		"TUTORIAL_TRIGGER",
		"WAYPOINT"

	))



###############################################################################

# Operator to add objects to level

class SWITCHBALL_TOOLS_OT_add(bpy.types.Operator):

	bl_idname = "switchball_tools.add"
	bl_label  = "Add Object"

	type: bpy.props.StringProperty()

	@classmethod
	def description(cls, context, properties):

		return "Add " + properties.type

	def execute(self, context):

		cls = TYPE.map[self.type]
		object = cls.new(self.type, cls, None)

		if hasattr(cls, "siblings"):

			for i in cls.siblings:

				sibling = TYPE.map[i[0]].new(i[0], TYPE.map[i[0]], None)

				sibling.rotation_euler = tuple(math.radians(d) for d in i[1])
				sibling.location       = i[2]

		if hasattr(cls, "children"):

			for i in cls.children:

				child = TYPE.map[i[0]].new(i[0], TYPE.map[i[0]], None)

				child.rotation_euler = tuple(math.radians(d) for d in i[1])
				child.location       = i[2]

				child.parent = object

		return { "FINISHED" }

###############################################################################

classes = (

	SWITCHBALL_TOOLS_addon_preferences,

	SWITCHBALL_TOOLS_MT_add,

	SWITCHBALL_TOOLS_MT_add_balls,
	SWITCHBALL_TOOLS_MT_add_unsupported,
	SWITCHBALL_TOOLS_MT_add_props,
	SWITCHBALL_TOOLS_MT_add_building,
	SWITCHBALL_TOOLS_MT_add_large,
	SWITCHBALL_TOOLS_MT_add_decoration,
	SWITCHBALL_TOOLS_MT_add_active,
	SWITCHBALL_TOOLS_MT_add_mechanics,
	SWITCHBALL_TOOLS_MT_add_meta,

	SWITCHBALL_TOOLS_OT_add

)

def register():

	for i in classes:
		bpy.utils.register_class(i)

	bpy.types.VIEW3D_MT_add.append(draw_item)

	bpy.utils.register_class(OBJECT_PT_SWITCHBALL_TOOLS)

	# for all files in objects/

	for module in pkgutil.iter_modules(objects.__path__):

		# import the file and register all types in it

		module = importlib.import_module('.' + module.name, objects.__name__)

		for cls in inspect.getmembers(module, inspect.isclass):

			if cls[1].__module__ != module.__name__: continue

			if (issubclass(cls[1], TYPE)):

				TYPE.add(cls[1])

			if issubclass(cls[1], bpy.types.bpy_struct):

				bpy.utils.register_class(cls[1])

			if issubclass(cls[1], bpy.types.PropertyGroup):

				setattr(bpy.types.Object, cls[0], bpy.props.PointerProperty(type = cls[1]))

	bpy.types.TOPBAR_MT_file_import.append(objects.level.menu_func_import)
	bpy.types.TOPBAR_MT_file_export.append(objects.level.menu_func_export)

def unregister():

	for i in classes:
		bpy.utils.unregister_class(i)

	bpy.types.VIEW3D_MT_add.remove(draw_item)

	for i in pkgutil.iter_modules([ "objects" ]):
		bpy.utils.unregister_class(i)

if __name__ == "__main__":
	register()

