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

from typing import Tuple, List
import sys
from cruscopoetry.syllabifiers.abstract import AbstractTokenizer, AbstractPhoneme, AbstractConsonant, AbstractVowel, Markers, exceptions
import re


class Phoneme(AbstractPhoneme):

	def __init__(self, string: str):
		super().__init__(string)

	@property
	def string(self):
		return super().string

	@property
	def is_vowel(self):
		return None
		
	def __repr__(self):
		return "%s(%s)"%(self.__class__.__name__, self.string)

	@property		
	def json_dict(self):
		return {"string": self.string, "base": self._base, "is_vowel": self.is_vowel}

		
class NullPhoneme(Phoneme):
	
	def __init__(self):
		super().__init__("")

	@property		
	def json_dict(self):
		return {}
		


class Vowel(AbstractVowel, Phoneme):

	def __init__(self, string: str):
		AbstractVowel.__init__(self, string)

	@property
	def is_vowel(self):
		return True

	@property
	def string(self):
		return super().string
		
	def __repr__(self):
		return "%s(%s, %d)"%(self.__class__.__name__, self.string, self.stress)

	@property		
	def json_dict(self):
		jdict = super().json_dict
		return jdict


class Consonant(AbstractConsonant, Phoneme):

	FERATURES_REGEX = re.compile("(?P<prenasalized>(m(?=b)|n(?=[dgjyz])))?(?P<base>([^\\Waeiou]h?)|ng')(?P<aspirated>')?(?P<palatalized>y)?(?P<labialized>w)?")
	def __init__(self, string: str):

		match = self.__class__.FERATURES_REGEX.match(string)
		prenasalized, base, aspirated, palatalized, labialized =  match.group("prenasalized"), match.group("base"), match.group("aspirated"), match.group("palatalized"), match.group("labialized")
		
		#in situations such as 'my', m

		self.is_prenasalized = prenasalized != None
		self.is_aspirated = aspirated != None
		self.is_palatalized = palatalized != None
		self.is_labialized = labialized != None
		super(AbstractConsonant, self).__init__(base)

	@property
	def is_vowel(self):
		return False

	@property		
	def json_dict(self):
		jdict = super().json_dict
		jdict.update({
			"is_prenasalized": self.is_prenasalized,
			"is_aspirated": self.is_aspirated,
			"is_palatalized": self.is_palatalized,
			"is_labialized": self.is_labialized,
		})
		return jdict

	@property
	def string(self):
		ret_str = ''
		if self.is_prenasalized:
			if self._base == 'b':
				ret_str += 'm'
			else:
				ret_str += 'n'
		ret_str += self._base
		
		if self.is_aspirated:
			ret_str += "'"
		
		if self.is_palatalized:
			ret_str += "y"

		if self.is_labialized:
			ret_str += "w"
		return ret_str			
		
		
class Ambiguous(Phoneme):

	def __init__(self, string: str):
		super().__init__(string)

	@property
	def is_vowel(self):
		return None


class SwahiliTokenizer(AbstractTokenizer):

	def __init__(self):
		self.ambiguous = ("m", "n")
		self.simple_consonants = ("b", "ch", "d", "dh", "ḏ", "f", "g", "gh", "h", "j", "k", "l", "ng'", "p", "r", "s", "sh", "t", "ṯ", "th", "v", "w", "y", "z")
		self.aspirated_consonants = ("ch'", "f'", "k'", "p'", "t'", "ṯ'")
		self.palatalized_consonants = ("fy", "py", "vy", "my")
		self.prenasalized_consonants = ("mb", "nd", "ng", "nj", "ny", "nz")
		self.labialized_consonants = (
			"bw", "chw", "dw", "ḏw", "fw", "gw", "jw", "kw", "lw", "mw", "nw", "ng'w", "pw", "rw", "sw", "shw", "tw", "ṯw", "vw", "yw", "zw", "mbw", "ndw", "ngw", "njw", "nzw"
		)
		
		consonants = self.simple_consonants + self.aspirated_consonants + self.palatalized_consonants + self.prenasalized_consonants + self.labialized_consonants + self.ambiguous
		self.non_ambiguous_vowels = ("a", "e", "i", "o", "u", "ə")
		vowels = self.non_ambiguous_vowels + self.ambiguous
		super().__init__(consonants, vowels)
	
	@property
	def non_ambiguous_consonants(self):
		return self.simple_consonants + self.aspirated_consonants + self.palatalized_consonants + self.prenasalized_consonants + self.labialized_consonants
		
	def _make_phoneme(self, string: str) -> Phoneme:
		"""Builds an instance of Vowel, Consonant or Ambiguous phonemes from a token string"""
		if string in self.non_ambiguous_consonants:
			return Consonant(string)
		
		#all the tokens starting by a number should be considered as vowels, so we check also this:
		elif string[0].isdigit():
			return Vowel(string)
		
		#now we check for numberless vowels, and pass what remains to Ambiguous:
		elif string in self.non_ambiguous_vowels:
			return Vowel(string)
		else:
			return Ambiguous(string)
			
	def _disambiguate(self, phonemes: List[Phoneme]) -> List[Phoneme]:
		"""Traverse all the items of a list of Phoneme instances, individuates the Ambiguous ones and transform them in Consonant instances if there is a Vowel instance after them, else in Vowel 
		instances."""
		#we will traverse the list from the end to the beginning. In this way, when we find a cluster of Ambiguous instances (such in mmoja, nne), we will be able to give 
		#immediately a role to the last one, and therefore we will be able to procede also with the others.
		for i in range(len(phonemes)-1,-1,-1):	#we don't have to worry for the last item because it will be certainly a vowel (and if it wasn't, we have already inserted it)
			if phonemes[i].__class__ == Ambiguous:
				if phonemes[i+1].is_vowel:
					phonemes[i] = Consonant(phonemes[i].string)
				else:
					phonemes[i] = Vowel(phonemes[i].string)
	
	def tokenize(self, string: str, separate_prenasalized = True) -> Tuple[str]:
		
		tokens = list(super().tokenize(string))
		
		#in Swahili there is no vowel crasis or diphthongation, so we raise an UnknownChar warning for those idiots that have put it in:
		if Markers.CRASIS in tokens:
			e = exceptions.UnknownChar(Markers.CRASIS)
			if __name__ == "__main__":#this is just for debugging
				e.line_number = 0
			raise e
		
		#here we can already handle an exceptional case. Words such as 'mbwa' and 'nge' here would be tokenized as ("mbw", "a"), ("ng", "e"), but so they would result as monosyllabic; thus we need to 
		#separate here the nasal component from the occlusive one.
		#we however do this olny if the parametre separate prenasalized is true, otherwise it could have unexpected consequences in manual syllabification:
		if separate_prenasalized:
			if len(tokens) == 2:											#just a consonant and a vowel
				if tokens[0][:2] in self.prenasalized_consonants: 			#the first two characters correspond to a prenasalized consonant:
					tokens = [tokens[0][:1], tokens[0][1:], tokens[1]]
		
		#consonant clusers must be separated, especially in poetry. Therefore, if we have two consonants next to each other and the first is not "m" or "n" (which could be also vowels), we insert a
		#'ə' vowel between them:
		for i in range(len(tokens)-1):
			if ((tokens[i] in self.non_ambiguous_consonants) and (tokens[i+1] in self.non_ambiguous_consonants)):
				tokens.insert(i+1, 'ə')
		
		#we check also the end:
		if tokens[-1] in self.non_ambiguous_consonants:
			tokens.append('ə')
			
		phonemes =  [self._make_phoneme(token) for token in tokens]
		return phonemes

	def auto_tokenize(self, string: str) -> Tuple[str]:
		"""Tokenizes a word that must be syllabified automatically."""
		phonemes = self.tokenize(string, separate_prenasalized = True)
		self._disambiguate(phonemes)
		return tuple(phonemes)
		
	def manually_tokenize(self, string: str) -> Tuple[str]:
		"""Used for tokenizing a syllable of a manually syllabified word"""
		tokens = self.tokenize(string, separate_prenasalized = False)

		#now we disambiguate the Ambiguous instances, making them Vowel if they are alone, Consonants if not
		if tokens[0].__class__ == Ambiguous:
			if len(tokens) == 1:
				tokens[0] = Vowel(tokens[0].string)
			else:
				tokens[0] = Consonant(tokens[0].string)
		return tuple(tokens)

