from nltk.tokenize import WhitespaceTokenizer

class MarkovChain(object):

	def __init__ (self, order):
		self.dictionary = {}
		self.max_word_count = None
		self.max_sentence_count = None
		self.setOrder(order)

	def setOrder(self, order ):
		self.order = order

	def buildDictionary(self, input_files):

		for file in input_files:
			data = open(file, 'r')
			lines = [self._processLine(line) for line in data.readlines()]
			self._processText(lines)

	def _processLine(self, line):

		return line.split('.')

	def _processText(self, lines):

		for line in lines:
			tokens = WhitespaceTokenizer().tokenize(line[0])
			sentence_key = str(tokens[0:self.order])
			self.dictionary.setdefault('BEGIN',[]).append(sentence_key)

			temp_map = {}

			for token in tokens[self.order:]:

				if token not in temp_map:
					temp_map[token] = 1

				else:
					temp_map[token] += 1

			if sentence_key not in self.dictionary:

				self.dictionary[sentence_key] = [(word, count) for word, count in temp_map.items()]

			else:

				words = self.dictionary[sentence_key]

				for index in range(len(words)):
					pairing = words[index]
					word, count = pairing

					if word in temp_map:
						count += temp_map[word]

					self.dictionary[sentence_key][index] = (word, count)
