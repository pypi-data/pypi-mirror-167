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
from .text_element import Joiners


class JsonNote:
	"""Represent a note from a Cruscopoetry Json file.

	Attrs:
		jdict (dict): the dictionary from which the note is istantiated;
		index (integer): the index of the notes in the array containing all the notes in the JSON file.
	"""

	def __init__(self, index, jdict):
		self.index = index
		self.jdict = jdict
	
	def json_dict(self):
		return self.jdict
	
	@property
	def number(self):
		"""The number of the note, that is, a progressive integer (starting from 1) which is assigned to each note following their order of occurrence in the txt source file."""
		return self.index+1
		
	@property
	def label(self):
		"""The note's label if it exists, else None."""
		return self.jdict["label"]
	
	@label.setter
	def label(self, value):
		self.jdict["label"] = value
		
	@property
	def reference(self):
		return self.jdict["reference"]
		
	@reference.setter
	def reference(self, value):
		self.jdict["reference"] = value
		
	@property
	def text(self):
		return self.jdict["text"]
		
	@text.setter
	def text(self, value):
		self.jdict["text"] = value
		
	@property
	def translations(self):
		return self.jdict["translations"]
	
	@property
	def as_text(self):
		return Joiners.NOTES.join((self.reference, self.text))
		
	def _get_translation_index_by_id(self, translation_id: str):
		for i in range(len(self.translations)):
			if self.translations[i][0] == translation_id:
				return i
		return None
		
	def get_translation_by_id(self, translation_id: str):
		for i in range(len(self.translations)):
			if self.translations[i][0] == translation_id:
				return self.translations[i][1]
		return None
	
	def add_translation(self, translation_id: str, translation):
		
		#translations are pairs of strings: (translation_id, translation.text). First, we search the id:
		translation_index = self._get_translation_index_by_id(translation_id)

		#then we append or update the translation:
		if translation_index == None:
			self.translations.append((translation_id, translation.text))
		else:
			self.translations[translation_index] == (translation_id, translation.text)
			
	def delete_translation(self, translation_id: str):
		translation_index = self._get_translation_index_by_id(translation_id)
		if translation_index != None:
			self.translations.pop(translation_index)
			

class JsonNotes:
	"""Represents the all the notes of a CruscoPoetry json poem."""
	
	def __init__(self, jarray):
		self.jarray = jarray
		
	def json_dict(self):
		return self.jarray
	
	def iter_notes_dict(self):
		yield from self.jarray
	
	def iter_notes(self):
		for index, note in enumerate(self.iter_notes_dict()):
			yield JsonNote(index, note)

	def __len__(self):
		return len(self.jarray)
			
	def _get_note_by_number(self, number: int) -> JsonNote:
		for note in self.iter_notes():
			if note.number == number:
				return note
		return None 
			
	def _get_note_by_reference(self, reference: str) -> JsonNote:
		for note in self.iter_notes():
			if note.label == reference:
				return note
		return None 
			
	def add_translation(self, translation_obj):
		translation_notes = translation_obj.notes
		for translation in translation_notes:
			if translation.reference != None:
				source = self._get_note_by_reference(translation.reference)
			else:
				source = self._get_note_by_number(translation.number)
			if source != None:
				source.add_translation(translation_obj.metadata.translation_id, translation)
			
	def delete_translation(self, translation_id: int):
		for note in self.iter_notes():
			note.delete_translation(translation_id)
		
	@property
	def as_text(self):
		ret_string = "NOTES"
		for note in self.iter_notes():
			ret_string += "\n%s"%note.as_text
		return ret_string
