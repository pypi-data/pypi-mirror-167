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
from .joiners import Joiners
	

class ColonRenderer:

	def __init__(self, jcolon: JsonColon):
		self.jcolon = jcolon

	def render(self) -> str:
		return self.jcolon.transcription


class LineRenderer:

	def __init__(self, jline: JsonLine, total_lines: int):
		self.jline = jline
		self.number_in_poem = 0
		
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

	def _start_line(self, indent, number_after):
		if indent == None:
			indent = "  "
		start_line = indent
		if number_after != None:
			if self.number_in_poem % number_after == 0:
				start_line += self.number_after_format%self.number_in_poem
			else:
				start_line += self.number_after_format%''
		return start_line

	def render_source(self, indent: str = None, number_after: int = None) -> str:
		line = self._start_line(indent, number_after)
		line += Joiners.COLON.join(tuple(colon.render() for colon in self.cola))
		return line

	def render_translation(self, translation_id: str, indent: str = None, number_after: int = None) -> str:
		translation = self.jline.get_translation_by_id(translation_id)
		if translation != None:
			line = self._start_line(indent, number_after)
			line += translation
			return line
		return ''

	def render(self, translation_id = None, indent: str = None, number_after: int = None) -> str:
		source = self.render_source(indent, number_after)
		#since this will be a each-line rendering, we don't need to print the line number also for translation. So we give number_after a bigger value than the total lines number, so that
		# self.jline.number % number_after be always different from 0:
		translation = self.render_translation(translation_id, indent, 10**(len(self.number_after_format)+1))
		return source + Joiners.LINE + translation


class StanzaRenderer:

	def __init__(self, jstanza: JsonStanza, total_lines: int):
		self.lines = tuple(LineRenderer(line, total_lines) for line in jstanza.iter_lines())
	
	def render_source(self, indent: str = None, number_after: int = None) -> str:
		return Joiners.LINE.join(tuple(line.render_source(indent, number_after) for line in self.lines))
		
	def render_translation(self, translation_id: str, indent: str = None, number_after: int = None) -> str:
		return Joiners.LINE.join(tuple(line.render_translation(translation_id, indent, number_after) for line in self.lines))
	
	def render(self, translation_id = None, indent: str = None, number_after: int = None) -> str:
		"""Renders the source text of the stanza and its translation, if found in the json file."""
		source = self.render_source(indent, number_after)
		translation = self.render_translation(translation_id, indent, number_after)
		return source + Joiners.STANZA + translation
		
		


class TextBodyRenderer:
	
	def __init__(self, body: JsonText):
		self.body = body
		
		#for a proper formatting, we also need to know the total number of lines in the poem
		total_lines = 0
		for stanza in body.iter_stanzas():
			total_lines += len(stanza.jdict["lines"])
			
		self.stanzas = tuple(StanzaRenderer(stanza, total_lines) for stanza in body.iter_stanzas())
		#now we iterate over the lines and set their attribute number_in_poem to a progressive integer starting by 1:
		for i, line in enumerate(self.iter_lines()):
			line.number_in_poem = i+1
		
	def iter_lines(self):
		for stanza in self.stanzas:
			yield from stanza.lines
		
	def render_source(self, indent: str = None, number_after: int = None) -> str:
		return Joiners.STANZA.join(tuple(stanza.render_source(indent, number_after) for stanza in self.stanzas))
		
	def render_translation(self, translation_id: str, indent: str = None, number_after: int = None) -> str:
		return Joiners.STANZA.join(tuple(stanza.render_translation(translation_id, indent, number_after) for stanza in self.stanzas))
		

	def render(self, translation_id: str, translation_arrangement: int, indent: str = None, number_after: int = None) -> str:
		"""Organizes the metadata in a string as tabular format.
		
		Returns
			view (str): the view of the text as string.
		"""
		ret_str=""
		if translation_arrangement == TranslationArrangement.NO_TRANSLATION:
			ret_str += self.render_source(indent, number_after)
		elif translation_arrangement == TranslationArrangement.AFTER_TEXT:
			ret_str += self.render_source(indent, number_after)
			ret_str += Joiners.LINE*2
			ret_str += self.render_translation(translation_id, indent, number_after)
		elif translation_arrangement == TranslationArrangement.EACH_STANZA:
			stanza_renderings = tuple(stanza.render(translation_id, indent, number_after) for stanza in self.stanzas)
			ret_str += (Joiners.STANZA + Joiners.LINE).join(stanza_renderings)
		elif translation_arrangement == TranslationArrangement.EACH_LINE:
			line_renderings = tuple(line.render(translation_id, indent, number_after) for line in self.iter_lines())
			ret_str += (Joiners.STANZA).join(line_renderings)
		return ret_str
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
