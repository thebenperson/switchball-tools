class PARAM:

	def __init__(self, name: str, value, description = None, min = None, max = None):

		self.name  = name
		self.value = value

		self.description = description

		self.min = min
		self.max = max

	def new(param):

		name      = param.get("name")
		value     = param.get("value")
		data_type = param.get("data_type")

		match data_type:

			case "bool":  value = (value == "true")
			case "int":   value = int(value)
			case "float": value = float(value)

			case "string": pass
			case _:

				raise ValueError(f"Unknown parameter type \"{ self.data_type }\"")

		return PARAM(name, value)

	def export(self):

		pass
