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

from .text_element import *
from ..translationparser.translation_parser import TranslationParser
import re
from .utils import TreeDict


class JsonPhoneme(JsonNumberedElement):
	"""Represents the phoneme of a syllable"""
	
	#since the phoneme dictionary is highly customable, we just store it in the jdict attribute:
	def __init__(self, index, jdict: dict):
		super().__init__(index, jdict)


class JsonSyllable(JsonNumberedElement):
	"""Represents the Syllable section of a Cruscopoetry poem serialized in JSON format."""
	
	PHONEME_CLASS = JsonPhoneme
	
	#since the syllables in cruscopoetry are highly customazable, we just store the dictionary.
	def __init__(self, index, jdict):
		super().__init__(index, jdict)


class JsonWord(JsonNumberedElement):
	"""Represents the Word section of a Cruscopoetry poem serialized in JSON format."""

	SYLLABLE_CLASS = JsonSyllable
	PHONEME_CLASS = JsonPhoneme
	
	def __init__(self, index, jdict):
		super().__init__(index, jdict)

	@property
	def string(self):
		return self.jdict["string"]
	
	@string.setter
	def transcription(self, value):
		self.jdict["string"] = value


class JsonColon(JsonNumberedElement):
	"""Represents the Colon section of a Cruscopoetry poem serialized in JSON format."""

	WORD_CLASS = JsonWord
	SYLLABLE_CLASS = JsonSyllable
	PHONEME_CLASS = JsonPhoneme
	
	def __init__(self, index, jdict):

		if jdict["pwib"] == "true":
			jdict["pwib"] = True
		else:
			jdict["pwib"] = False

		if jdict["fwib"] == "true":
			jdict["fwib"] = True
		else:
			jdict["fwib"] = False

		super().__init__(index, jdict)

	@property
	def pwib(self):
		return self.jdict["pwib"]

	@property
	def fwib(self):
		return self.jdict["fwib"]

	@property
	def transcription(self):
		return self.jdict["transcription"]
	
	@transcription.setter
	def transcription(self, value):
		self.jdict["transcription"] = value
		
	@property
	def phonetics(self):
		return Joiners.WORDS.join(word.string for word in self.iter_words())
		
	@property
	def as_text(self):
		return self._compare(self.transcription, self.phonetics)
			
	def _compare(self, transcription, phonetics):
		ret_str = ""
		word_finder = re.compile("([\\w\\[\\]|]+)|([^\\w\\[\\]|])")
		tr_list = list(result for result in word_finder.findall(transcription))
		ph_tuple = tuple(result for result in word_finder.findall(phonetics) if result[0] != "")

		i = 0
		while i < len(ph_tuple):
			if tr_list[i][0] == "":
				ret_str += tr_list[i][1]
				tr_list.pop(i)
				continue

			if tr_list[i][0].lower() == ph_tuple[i][0]:
				ret_str += tr_list[i][0]

			elif re.sub("[\\[\\]|]", "", ph_tuple[i][0]) == tr_list[i][0]:
				ret_str += ph_tuple[i][0]

			else:
				ret_str += "<%s|%s>"%(tr_list[i][0], ph_tuple[i][0])

			i += 1
		return ret_str


class JsonLine(JsonNumberedElement):
	"""Represents the Line section of a Cruscopoetry poem serialized in JSON format."""

	COLON_CLASS = JsonColon
	WORD_CLASS = JsonWord
	SYLLABLE_CLASS = JsonSyllable
	PHONEME_CLASS = JsonPhoneme
	
	def __init__(self, index, jdict):
		super().__init__(index, jdict)

	@property
	def label(self):
		return self.jdict["label"]
	
	@label.setter
	def label(self, value):
		self.jdict["label"] = value
		
	@property
	def transcription(self):
		ret_str = ""
		for colon in self.iter_cola():
			if colon.index != 0:
				if colon.pwib:
					ret_str += Joiners.WORD_INTERNAL_COLA_TRANSCRIPTION
				else:
					ret_str += Joiners.COLA_TRANSCRIPTION
			ret_str += colon.transcription
		return ret_str
		
	@property
	def as_text(self):
		ret_str = ""
		for colon in self.iter_cola():
			if colon.index != 0:
				if colon.pwib:
					ret_str += Joiners.WORD_INTERNAL_COLA
				else:
					ret_str += Joiners.COLA
			ret_str += colon.as_text
		return ret_str
		
	@property
	def translations(self):
		return self.jdict["translations"]
	#rather than adding a set translation function, we can directly operate on it, since it is a list

	def __contains__(self, tr_id: str):
		"""Returns True if a translation (identified by id) is stored in the object."""
		return self._get_translation_index_by_id(tr_id) != None
	
	def get_translation_by_id(self, tr_id: str):
		for translation in self.translations:
			if translation[0] == tr_id:
				return translation[1]
		return None
	
	def _get_translation_index_by_id(self, tr_id: str):
		for i in range(len(self.translations)):
			if self.translations[i][0] == tr_id:
				return i
		return None
		
	def delete_translation(self, tr_id: str):
		"""Deletes a translation from the line by given id. If the line has not this translation, nothing happens."""
		for i in range(len(self.translations)):
			if self.translations[i][0] == tr_id:
				self.translations.pop(i)
				break
	
	def add_translation(self, tr_obj, tr_id: str):
		"""Adds a translation to the line. If the line already has a translation with the same id, it will update it."""
		old_translation_index = self._get_translation_index_by_id(tr_id)
		if old_translation_index == None:
			self.translations.append(
				(tr_id, tr_obj.line)
			)
		else:
			self.translations[old_translation_index] = (tr_id, tr_obj.line)

	def iter_stanzas_dict(self):
		"""For impossible iterations, we just yield form an emtpy list."""
		yield from []

	def iter_lines_dict(self):
		yield from []

	def iter_cola_dict(self):
		yield from self.jdict["cola"]


class JsonStanza(JsonNumberedElement):
	"""Represents the Stanza section of a Cruscopoetry poem serialized in JSON format."""

	LINE_CLASS = JsonLine
	COLON_CLASS = JsonColon
	WORD_CLASS = JsonWord
	SYLLABLE_CLASS = JsonSyllable
	PHONEME_CLASS = JsonPhoneme
	
	def __init__(self, index, jdict):
		super().__init__(index, jdict)

	def iter_stanzas_dict(self):
		"""For impossible iterations, we just yield form an emtpy list."""
		yield from []

	def iter_lines_dict(self):
		yield from self.jdict["lines"]
		
	def iter_words_dict(self):
		for line in self.iter_lines():
			yield from line.iter_words_dict()

	@property
	def as_text(self):
		return Joiners.LINES.join((line.as_text for line in self.iter_lines()))
		
	@property
	def transcription(self):
		return Joiners.LINES.join((line.transcription for line in self.iter_lines()))		


class JsonText(JsonElement):
	"""Represents the Text section of a Cruscopoetry poem serialized in JSON format."""

	STANZA_CLASS = JsonStanza
	LINE_CLASS = JsonLine
	COLON_CLASS = JsonColon
	WORD_CLASS = JsonWord
	SYLLABLE_CLASS = JsonSyllable
	PHONEME_CLASS = JsonPhoneme
	
	def __init__(self, jdict):
		super().__init__(TreeDict(jdict))

	def get_line_by_number(self, number: int):
		"""Gets a line by its number (numbers start from 1). Returns None if no line is found."""
		for line in self.iter_lines():
			if line.number == number:
				return line
		return None

	def get_line_by_label(self, label: str):
		"""Gets a line by its label. Labels here must not include the $ start character. Returns None if no line is found."""
		for line in self.iter_lines():
			if line.label == label:
				return line
		return None
		
	def iter_words_dict(self):
		for stanza in self.iter_stanzas():
			yield from stanza.iter_words_dict()
		
	@property
	def as_text(self):
		return "TEXT\n" + Joiners.STANZAS.join((stanza.as_text for stanza in self.iter_stanzas()))
		
	@property
	def labels_to_indexes_dict(self) -> dict:
		"""Returns a dictionary where each line's label, if exists, is mapped to the line's index(integers starting from 0)."""
		ret_dict = {line.label: line.index for line in self.iter_lines() if line.label != None}
		return ret_dict

	def add_translation(self, tr_object: TranslationParser):
		for line in tr_object.text.lines:
			if line.label != None:
				destination = self.get_line_by_label(line.label)
			else:
				destination = self.get_line_by_number(line.number)
			
			if destination != None:
				destination.add_translation(line, tr_object.metadata.translation_id)
			else:
				self.print_warning("no line found for translation line " + line.__repr__())
		
	def delete_translation(self, tr_id: str):
		"""Deletes a translation from the text lines by given id. If the lines have not this translation, nothing happens."""
		for line in self.iter_lines():
			line.delete_translation(tr_id)


	def print_warning(self, message):
		print("\033[1;33;40mWarning\033[m. " + message)
