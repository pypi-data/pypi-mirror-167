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
from .exceptions import *
from .utils import MetadataDict, MetadataValidator
from .joiners import Joiners


class JsonTranslation:
	"""Represents one of the possible translations of the poem.
	
	Args:
		jdict (dict): the section of the JSON file representing the translation's metadata
	
	Args:
		jdict (MetadataDict): the section of the JSON file representing the translation's metadata
	"""

	def __init__(self, jdict):
		requirements = [
			("id", True, False, MetadataValidator.NO_CONTROL),
			("language", True, False, MetadataValidator.LANGUAGE),
		]
		validator = MetadataValidator(requirements)
		self.jdict = MetadataDict(jdict, validator)

	def json_dict(self):
		"""Returns the translation metadata dictionary with eventual updates."""
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
	def id(self):
		"""The id of the translation. This property can not be modified."""
		return self.jdict["id"]
	
	@id.setter
	def id(self, value):
		self.jdict["id"] = value
		
	@property
	def language(self):
		"""The language of the translation. This property can not be modified."""
		return self.jdict["language"]
	
	@language.setter
	def language(self, value):
		self.jdict["language"] = value
			
	def mandatory_keys(self):
		"""The keys of the mandatory metadata fields"""
		return self.jdict.mandatory_keys()
	
	def optional_keys(self):
		"""The keys of the optional metadata fields"""
		return self.jdict.optional_keys()
		
	def update(self, meta_dict: dict):
		"""Updates the translation data with the information enclosed in meta_dict."""
		self.jdict.update(meta_dict)
		
	@property
	def as_text(self):
		"""A plain text representation of the translation's metadata (useful if one wants to build back the txt file)"""
		return self.jdict.as_text
		
	def __str__(self):
		return "%s(%r)"%(self.__class__.__name__, self.jdict.dict)


class JsonTranslations:

	def __init__(self, tr_array: list):
		self.tr_array = tr_array
		self._iter_index = 0
		
	def __contains__(self, translation_id: str):
		"""Checks if the translation with id ``translation_id`` is in the translations list."""
		return self.get_translation_by_id(translation_id) != None
	
	def get_translation_by_id(self, tr_id: str):
		"""Returns the translation with the given id. If for some reasons more translations with the same id are stored in the json file, 
		it will always return the first one."""
		for translation in self:
			if translation.id == tr_id:
				return translation
		return None
		
	def __str__(self):
		return "%r"%self.tr_array
		
	def __len__(self):
		"""Returns the number of translations contained in the instance."""
		return len(self.tr_array)

	def __next__(self):
		if self._iter_index < len(self.tr_array):
			to_yield = JsonTranslation(self.tr_array[self._iter_index])
			self._iter_index += 1
			return to_yield
		else:
			self._iter_index = 0
			raise StopIteration

	def __iter__(self):
		self._iter_index = 0
		return self
		
	def json_dict(self):
		"""Returns the metadata dictionaries of all the translations."""
		return self.tr_array
		
	def append(self, metadata_dict: dict):
		"Appends a new translation to self.jdict if there isn't already one with the same id. If there is, it will update it."
		meta_id = metadata_dict["id"]
		old_translation = self.get_translation_by_id(meta_id)
		if old_translation == None:
			self.tr_array.append(metadata_dict)
		else:
			old_translation.update(metadata_dict)
			
	def delete(self, tr_id: str):
		"""Deletes the translation whose id is tr_id"""
		for index, tr_dict in enumerate(self.tr_array):
			if tr_dict["id"] == tr_id:
				self.jdict.pop(index)
				break
		
	@property
	def as_text(self):
		ret_str = Joiners.LINES + "TRANSLATIONS:"
		for translation in self:
			ret_str += Joiners.LINES + translation.as_text
		return ret_str
