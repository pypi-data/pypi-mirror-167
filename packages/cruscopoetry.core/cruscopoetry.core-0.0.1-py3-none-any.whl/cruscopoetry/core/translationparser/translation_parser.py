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

import re
from ..base_parser import BaseParser
from .metadata_parser import TranslationMetadata
from .text_parser import TranslationText
from .notes_parser import TranslationNotes, NullTranslationNotes
import os


class TranslationParser(BaseParser):
	"""Represents the parsing of a translation file."""

	def __init__(self, file_path: str):
		super().__init__(file_path)
		with open(self.path, 'r') as myfile:
			translation = myfile.read()
		
		parser = SectionsParser(translation)
		metadata, text, notes = parser.sections
		self.metadata = TranslationMetadata(metadata)
		self.text = TranslationText(text)
		self.notes = TranslationNotes(notes) if notes != None else NullTranslationNotes
		
	def __repr__(self):
		return "METADATA|\n%sTEXT\n%s\nNOTES\n%s"%(self.metadata.__repr__(), self.text.__repr__(), self.notes.__repr__())


class SectionsParser:

	def __init__(self, poem_translation: str):
		regex_pattern = "^.*?METADATA" + os.linesep + "(?P<metadata>.*?)" + os.linesep + "TEXT" + os.linesep + "(?P<text>.*?)(" + os.linesep + "NOTES" + os.linesep + "(?P<notes>.*?))?" + "$"
		regex = re.compile(regex_pattern, re.DOTALL)
		matches = regex.match(poem_translation)
		metadata = matches.group("metadata")
		text = matches.group("text")
		notes = matches.group("notes")
		self.sections: tuple = (metadata, text, notes)
