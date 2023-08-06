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

from typing import Tuple
from cruscopoetry.syllabifiers.abstract import AbstractSyllabifier, Markers
from .tokenizer import SwahiliTokenizer, Phoneme
from .syllable import SwahiliSyllable


class SwahiliSyllabifier(AbstractSyllabifier):

	def __init__(self):
		super().__init__()
	
	def _set_phonetic_stresses(self, syllables: tuple):
		"""Iterates over syllables (a tuple of SwahiliSyllable instances that ideally compose a word), inserting the phonetic stress in the penultimate syllable and eliminating it from the others."""

		#only 'tu' and 'je' are the phonetically stressed monosyllables, the others are not
		if len(syllables) == 1:
			if syllables[0].string in ("je", "tu"):
				syllables[0].set_phonetic_stress(True)
			else:
				syllables[0].set_phonetic_stress(False)

		#if it is a polysyllable, we stress just the penultimate:
		else:
			for i in range(len(syllables)):
				if i != (len(syllables) - 2):
					syllables[i].set_phonetic_stress(False)
				else:
					syllables[i].set_phonetic_stress(True)
	
	def auto_syllabify(self, word: str) -> Tuple[dict]:
		syllables = []
		#if there is a hyphen in the word, we split it and tokenize each section:
		if '-' in word:
			sections = word.split('-')
			while '' in sections:
				sections.remove('-')
			sections = [self.auto_syllabify(section) for section in sections]
			syllables.extend(sections)
		
		#if not, this is the non recurive part of the function:
		tokenizer = SwahiliTokenizer()
		tokens = tokenizer.auto_tokenize(word)
		#now we traverse the list; if we find a Consonant, we group it together with the following Vowel; if we find a Vowel not preceded by a Consonant, we put it as an isolated syllable
		i = 0
		while i < len(tokens):
			new_syllable = []
			if tokens[i].is_vowel == False:
				new_syllable.append(tokens[i])
				new_syllable.append(tokens[i+1])
				i += 1
			else:
				new_syllable.append(tokens[i])
			i += 1
			syllables.append(SwahiliSyllable(new_syllable))

		#we set the phonetic stresses:
		self._set_phonetic_stresses(syllables)

		#finally we return the syllables' json_dict properties:
		return tuple(syllable.json_dict for syllable in syllables)
	
	def manually_syllabify(self, word: str) -> Tuple[dict]:
		
		#first, we remove the brackets:
		word = word[1:-1]
		#then we split on the syllables separator:
		word = word.split(Markers.SYLLABLES_SEP)
		#now we tokenize the phonemes:
		tokenizer = SwahiliTokenizer()
		word = [list(tokenizer.manually_tokenize(syllable)) for syllable in word]

		#now we build our SwahiliSyllable instances and return their json_dict:
		syllables = tuple(SwahiliSyllable(syllable) for syllable in word)
		
		#we set the phonetic stresses:
		self._set_phonetic_stresses(syllables)

		#finally we return the syllables' json_dict properties:
		return tuple(syllable.json_dict for syllable in syllables)

