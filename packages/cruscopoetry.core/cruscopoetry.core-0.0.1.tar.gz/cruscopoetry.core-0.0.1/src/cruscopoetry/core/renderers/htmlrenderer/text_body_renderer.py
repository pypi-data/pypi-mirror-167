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
from ...jsonparser import JsonText, JsonTranslations, JsonTranslation, JsonStanza, JsonLine, JsonColon
from ..abstractrenderer import TranslationArrangement
from .utils import *
	

class ColonRenderer:

	def __init__(self, jcolon: JsonColon):
		self.jcolon = jcolon

	def render(self) -> str:
		node = TextNode(self.jcolon.transcription)
		return node


class LineRenderer:

	def __init__(self, jline: JsonLine, total_lines: int):
		self.jline = jline
		
		#for being able to format well the line, we need to know how many decimal digits total_lines is composed of:
		digits = 1
		base = 10
		power = base ** digits
		while total_lines // power > 0:
			digits += 1
			power = base ** digits
		#now that in digits is stored the quantity of digits of the maximum verse number, we can create a formatting string for it:
		self.number_after_format = "%%%ds "%digits
		self.cola = tuple(ColonRenderer(colon) for colon in jline.iter_cola())

	def _start_line(self, number_after: int) -> HtmlElement:
		"""This node will contain the line number if line.number % number_after == 0, else no text."""
		start_line = HtmlNode("td", {"id": "line_%d"%self.jline.number, "class": "number"})
		if number_after != None:
			if self.jline.number % number_after == 0:
				start_line.append(str(self.jline.number))
			else:
				start_line.append(" ")
		else:
			start_line.append(" ")
		return start_line
		
	@property
	def blank_colon(self):
		return HtmlNode("td", {}, " ")
	
	@property
	def colon_separator(self):
		return TextNode(" · ")

	def render_source(self: str = None, number_after: int = None) -> str:
		line = HtmlNode("tr", {"class": "line source"})
		line.append(self._start_line(number_after))
		cola = [colon.render() for colon in self.cola]
		cola = self.colon_separator.join(cola)
		line_cell = HtmlNode("td", {}, cola)
		line.append(line_cell)
		return line

	def render_translation(self, translation_id: str, number_after: int = None) -> str:
		line = HtmlNode("tr", {"class": "line translation"})
		translation = self.jline.get_translation_by_id(translation_id)
		if translation != None:
			line.append(self._start_line(number_after))
			#we insert the text translation in a td node who colspans all the colon columns in the table:
			line.append(HtmlNode("td", {}, translation))
		else:
			return line.append(NullNode())
		return line

	def render(self, translation_id = None, number_after: int = None) -> str:

		#first we get the source:
		source = self.render_source(number_after)
		#start line is the first child of source. We set rowspan in it to 2:
		source[0].attribs["rowspan"] = "2"

		#now we get translation. We need only the second item from here:
		translation = self.render_translation(translation_id, number_after)[1]
							
		return (source, translation)


class StanzaRenderer:

	def __init__(self, jstanza: JsonStanza, total_lines: int):
		self.lines = tuple(LineRenderer(line, total_lines) for line in jstanza.iter_lines())

	@property
	def blank_row(self):
		blank = HtmlNode("tr", {"class": "stanza_sep"})
		blank.append(HtmlNode("td", {}, ' '))
		return blank
	
	def render_source(self, number_after: int = None) -> str:
		stanza = HtmlNode("div", {"class": "stanza"})
		source = HtmlNode("div", {"class": "source"})
		for line in self.lines:
			source.append(line.render_source(number_after))
		stanza.append(source)
		return stanza
		
	def render_translation(self, translation_id: str, number_after: int = None) -> str:
		stanza = HtmlNode("div", {"class": "stanza"})
		translation = HtmlNode("div", {"class": "translation"})
		for line in self.lines:
			translation.append(line.render_translation(translation_id, number_after))
		stanza.append(translation)
		return stanza
	
	def render(self, translation_id = None, number_after: int = None) -> str:
		"""Renders the source text of the stanza and its translation, if found in the json file."""

		stanza = HtmlNode("div", {"class": "stanza"})

		source = self.render_source(number_after)[0]#we extract only the div with source class
		translation = self.render_translation(translation_id, number_after)[0]#we extract only the div with translation class
		stanza.append(source)
		stanza.append(self.blank_row)
		stanza.append(translation)
		return stanza
		

class TextBodyRenderer:
	
	def __init__(self, body: JsonText):
		self.body = body
		
		#for a proper formatting, we also need to know the total number of lines in the poem
		total_lines = 0
		for stanza in body.iter_stanzas():
			total_lines += len(stanza.jdict["lines"])
		
		self.stanzas = tuple(StanzaRenderer(stanza, total_lines) for stanza in body.iter_stanzas())

	@property
	def blank_row(self):
		blank = HtmlNode("tr", {"class": "stanza_sep"})
		blank.append(HtmlNode("td", {}, ' '))
		return blank
		
	def iter_lines(self):
		for stanza in self.stanzas:
			yield from stanza.lines
		
	def render_source(self, number_after: int = None) -> str:
		return self.blank_row.join([stanza.render_source(number_after) for stanza in self.stanzas])
		
	def render_translation(self, translation_id: str, number_after: int = None) -> str:
		return self.blank_row.join([stanza.render_translation(translation_id, number_after) for stanza in self.stanzas])
		

	def render(self, translation_id: str, translation_arrangement: int, number_after: int = None) -> str:
		"""Organizes the metadata in a string as tabular format.
		
		Returns
			view (str): the view of the text as string.
		"""
		node = HtmlNode("div", {"id": "text_section"})
		node.append(HtmlNode("h1", {"id": "text_title"}, "Text"))
		lines_table = HtmlNode("table", {"id": "text_table"})
		node.append(lines_table)

		if translation_arrangement == TranslationArrangement.NO_TRANSLATION:
			lines_table.extend(self.render_source(number_after))

		elif translation_arrangement == TranslationArrangement.AFTER_TEXT:
			lines_table.extend(self.render_source(number_after))
			lines_table.extend([self.blank_row]*2)
			lines_table.extend(self.render_translation(translation_id, number_after))

		elif translation_arrangement == TranslationArrangement.EACH_STANZA:
			stanza_renderings = [stanza.render(translation_id, number_after) for stanza in self.stanzas]
			joiner = HtmlNode("div", {}, [self.blank_row, self.blank_row])
			stanza_renderings = joiner.join(stanza_renderings)
			lines_table.extend(stanza_renderings)
		elif translation_arrangement == TranslationArrangement.EACH_LINE:

			#line.render will return a tuple of two nodes: source and translation.
			line_renderings = tuple(line.render(translation_id, number_after) for line in self.iter_lines())
			for line_rendering in line_renderings:
				lines_table.extend(line_rendering)
				lines_table.append(self.blank_row)

		return node
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
