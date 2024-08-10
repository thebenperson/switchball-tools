import bpy

class TYPE:

	map = {}

	def add(cls):

		if hasattr(cls, "types"):

			for i in cls.types:

				print("ADD " + i)
				TYPE.map[i] = cls

		else:

			print("ADD " + cls.__name__)
			TYPE.map[cls.__name__] = cls

	def bases(object):

		cls = TYPE.map(object["type"])
		bases = []

		while True:

			if issubclass(cls, bpy.types.PropertyGroup):
				bases.append(cls)

			try: cls = cls.SUPER
			except: break

		return bases

	@classmethod
	def get(cls, option):

		try: return getattr(cls, option)
		except: pass

		try: return cls.SUPER.get(option)
		except: return None

	@classmethod
	def issubclass(cls, base):

		if cls == base: return True

		try: return cls.SUPER.issubclass(base)
		except: return False

	@classmethod
	def new(cls, type, options = None, object = None):

		if options is None: options = cls
		return cls.SUPER.new(type, options, object)

	@classmethod
	def next_new(cls, type, options = None, object = None):

		if options is None: options = cls
		return cls.SUPER.new(type, options, object)

	@classmethod
	def from_xml(cls, object, root):

		cls.SUPER.from_xml(object, root)

	@classmethod
	def next_from_xml(cls, object, root):

		cls.SUPER.from_xml(object, root)

	@classmethod
	def to_xml(cls, root, object):

		cls.SUPER.to_xml(root, object)

	@classmethod
	def next_to_xml(cls, root, object):

		cls.SUPER.to_xml(root, object)


