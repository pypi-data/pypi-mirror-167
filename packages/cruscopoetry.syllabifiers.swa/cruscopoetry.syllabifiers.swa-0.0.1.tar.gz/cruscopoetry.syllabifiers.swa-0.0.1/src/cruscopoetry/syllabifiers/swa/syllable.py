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
from cruscopoetry.syllabifiers.abstract import AbstractSyllable
from .tokenizer import Phoneme, NullPhoneme


class SwahiliSyllable(AbstractSyllable):

	def __init__(self, phonemes: tuple):
		if len(phonemes) == 1:
			phonemes.insert(0, NullPhoneme())
		self.onset, self.nucleum = phonemes

	def iter_phonemes(self):
		if self.onset.__class__ != NullPhoneme:
			yield self.onset
		yield self.nucleum

	@property
	def stress(self):
		return self.nucleum.stress
	
	@stress.setter
	def stress(self, value: int):
		self.nucleum.stress = value % 8

	def set_phonetic_stress(self, value: bool):
		if value:
			if not self.has_phonetic_stress:
				self.stress += 1
		else:
			if self.has_phonetic_stress:
				self.stress -= 1

	@property
	def string(self):
		return ''.join(phoneme.string for phoneme in self.iter_phonemes())
	
	@property
	def json_dict(self) -> dict:
		ret_dict = super().json_dict
		return ret_dict
