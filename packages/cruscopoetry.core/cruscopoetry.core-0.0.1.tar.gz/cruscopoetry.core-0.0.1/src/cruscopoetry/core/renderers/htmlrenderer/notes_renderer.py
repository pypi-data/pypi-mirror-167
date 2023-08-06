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
from .utils import HtmlNode, TextNode


class NoteRenderer:

	def __init__(self, jnote, lines_map):
		self.jnote = jnote
		self.lines_map = lines_map
		
	@property
	def reference(self):
		"""If a note is referenced by verse number or by 'all', it returns the note's reference. If otherwise the note is recerenced by a verse label, it will return the verse number."""
		if ((self.jnote.reference.isdigit()) or (self.jnote.reference == "all")):
			return self.jnote.reference
		else:
			index = self.lines_map[self.jnote.reference]
			return str(index+1)
	
	def _make_link(self, reference: str):
		if reference == "all":
			return "#" + "text_table"
		else:
			return "#line_" + reference
		
	def render(self, translation_id, render_translation):

		reference_node = HtmlNode("a", {"href": self._make_link(self.reference)}, TextNode(self.reference))
		reference_cell = HtmlNode("td", {"class": "reference"}, reference_node)

		if render_translation:
			text = self.jnote.get_translation_by_id(translation_id)
			text = text if text != None else ' '
		else:
			text = self.jnote.text

		text_cell = HtmlNode("td", {"class": "text"}, text)

		note_row = HtmlNode("tr", {"class": "note"}, [reference_cell, text_cell])
		return note_row


class NotesRenderer:

	def __init__(self, jnotes, lines_map):
		self.notes = tuple(NoteRenderer(note, lines_map) for note in jnotes.iter_notes())
		
	def render(self, translation_id: str, render_translation: bool):
		section_div = HtmlNode("div", {"id": "notes_section"})
		title = HtmlNode("h1", {"id": "notes_title"}, "Notes")
		section_div.append(title)
		table = HtmlNode("table", {"id": "notes_table"})
		section_div.append(table)
		notes = [note.render(translation_id, render_translation) for note in self.notes]
		table.extend(notes)
		return section_div
		
		
		
		
		
		
		
		
		
		
		

