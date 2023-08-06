#    This file is part of CruscoPoetry.
#
#    CruscoPoetry is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CruscoPoetry is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CruscoPoetry.  If not, see <http://www.gnu.org/licenses/>.
from .joiners import Joiners
from .exceptions import InvalidLanguageError, InvalidCountryError, InvalidScriptError, MandatoryFieldError
from .utils import MetadataDict, MetadataValidator


class JsonMetadata:
	"""Class representing the metadata of a JSON-serialized poem. It behaves as a normal Python dictionary, but several validations are carried out while trying to set or delete items.
	
	Args:
		jdict (dict): the dictionary resulting from the JSON parsing and corresponding to the metadata section of the poem.
	
	Attrs:
		jdict (MetadataDict): the MetadataDict instance resulting from the JSON parsing.
	"""
	MANDATORY_FIELDS = ("title", "author", "language", "script", "country")

	def __init__(self, jdict):

		requirements = [
			("title", True, True, MetadataValidator.NO_CONTROL),
			("author", True, True, MetadataValidator.NO_CONTROL),
			("language", True, True, MetadataValidator.LANGUAGE),
			("country", True, True, MetadataValidator.COUNTRY),
			("script", True, True, MetadataValidator.SCRIPT),
		]
		validator = MetadataValidator(requirements)
		self.jdict = MetadataDict(jdict, validator)

	def json_dict(self):
		"""Returns the metadata dictionary with eventual updates."""
		return self.jdict.dict
		
	def __getitem__(self, key):
		"""As dict.__getitem__(key)"""
		return self.jdict.__getitem__(key)
		
	def __setitem__(self, key, value):
		"""As dict.__setitem__(key, value), but an error is raised if a field who requires a certain code (es. ISO639-3 for 'language' field) receive an invalid value"""
		self.jdict.__setitem__(key, value)
		
	def __delitem__(self, key):
		"""As dict.__delitem__(key), but an error is raised if one attemps to delete a mandatory field."""
		self.jdict.__delitem__(key)

	def __len__(self):
		"""As dict.__len__()"""
		return len(self.jdict)
	
	def __iter__(self):
		"""As dict.__iter__()"""
		return iter(self.jdict)
		
	def keys(self):
		"""As dict.keys()"""
		return self.jdict.keys()
		
	def values(self):
		"""As dict.values()"""
		return self.jdict.values()
		
	def items(self):
		"""As dict.items()"""
		return self.jdict.items()

	@property
	def title(self):
		"""The poem's title"""
		return self.jdict["title"]
	
	@title.setter
	def title(self, value):
		self.jdict["title"] = value
	
	@title.deleter
	def title(self):
		del self.jdict["title"]

	@property
	def author(self):
		"""The poem's author"""
		return self.jdict["author"]
	
	@author.setter
	def author(self, value):
		self.jdict["author"] = value
	
	@author.deleter
	def author(self):
		del self.jdict["author"]

	@property
	def language(self):
		"""The poem's language"""
		return self.jdict["language"]
	
	@language.setter
	def language(self, value):
		self.jdict["language"] = value
	
	@language.deleter
	def language(self):
		del self.jdict["language"]

	@property
	def script(self):
		"""The poem's script"""
		return self.jdict["script"]
	
	@script.setter
	def script(self, value):
		self.jdict["script"] = value
	
	@script.deleter
	def script(self):
		del self.jdict["script"]

	@property
	def country(self):
		"""The poem's country"""
		return self.jdict["country"]
	
	@country.setter
	def country(self, value):
		self.jdict["country"] = value
	
	@country.deleter
	def country(self):
		del self.jdict["country"]
			
	def mandatory_keys(self) -> list:
		"""The keys of the mandatory metadata fields"""
		return self.jdict.mandatory_keys()
			
	def mandatory_values(self) -> list:
		"""The values of the mandatory metadata fields"""
		return self.jdict.mandatory_values()
			
	def mandatory_items(self) -> list:
		"""The item pairs of the mandatory metadata fields"""
		return self.jdict.mandatory_items()
	
	def optional_keys(self) -> list:
		"""The keys of the optional metadata fields"""
		return self.jdict.optional_keys()
	
	def optional_values(self) -> list:
		"""The values of the optional metadata fields"""
		return self.jdict.optional_values()
	
	def optional_items(self) -> list:
		"""The item pairs of the optional metadata fields"""
		return self.jdict.optional_items()

	@property
	def as_text(self):
		"""A plain text representation of the metadata (useful if one wants to build back the txt source file)"""
		ret_string = "METADATA" + Joiners.LINES + self.jdict.as_text
		return ret_string
