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
from .metadata_renderer import MetadataRenderer
from .notes_renderer import NotesRenderer
from .text_body_renderer import TextBodyRenderer
from ..abstractrenderer import AbstractRenderer, TranslationArrangement
import os


class TextRenderer(AbstractRenderer):
	"""This class is a concrete implementation of :class:`cruscopoetry.renderers.AbstractRenderer` for plain text.
	
	Args:
		path (str): the path of the JSON file that must be rendered.
	"""
	
	def __init__(self, path: str):
		super().__init__(path)
		self.metadata = MetadataRenderer(self.json.metadata, self.json.translations)
		self.body = TextBodyRenderer(self.json.text)

		#to render the notes, we will also need a dictionary to map each verse label to its number:
		lines_map = self.json.text.labels_to_indexes_dict
		self.notes = NotesRenderer(self.json.notes, lines_map)
		

	def render(self, translation_id: str = None, translation_arrangement: int = None, indent: str = None, number_after: int = None) -> str:
		"""Builds the view and returns it as a string (this function doesn't save it on a file.
		
		Args:
			translation_id (str): the id of the translation to insert into the view, or None if no translation is desired.
			translation_arrangement (int): an integer between AbstractViewer.NO_TRANSLATION , AbstractViewer.AFTER_TEXT , AbstractViewer.STANZA_BY_STANZA and AbstractViewer.LINE_BY_LINE.
		
		Returns
			view (str): the view of the text as string.
		"""
		super().render(translation_id, translation_arrangement)
		if translation_arrangement == None:
			if translation_id == None:
				translation_arrangement = TranslationArrangement.NO_TRANSLATION
			else:
				translation_arrangement = TranslationArrangement.AFTER_TEXT
		ret_str = ''
		ret_str += self.metadata.render(translation_id, indent)
		ret_str += os.linesep + "TEXT" + os.linesep
		ret_str += self.body.render(translation_id, translation_arrangement, indent, number_after)
		ret_str += os.linesep + "NOTES" + os.linesep
		#regarding notes, we will render only their source text if translation_arrangement != NO_TRANSLATION, else only their translated text.
		ret_str += self.notes.render(translation_id, translation_arrangement != TranslationArrangement.NO_TRANSLATION, indent)
		return ret_str
		
