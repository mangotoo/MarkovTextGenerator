import argparse
from markov import MarkovChain

def main(arguments):

	markov_chain = MarkovChain(arguments['order'])

	dictionary = markov_chain.buildDictionary(arguments['input'])

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description = "Simple script used to generate text using a Markov Model")

	parser.add_argument('-n', '--order' , nargs = '?', help = 'The order of the Markov Chain', type = int, default = 2)

	parser.add_argument('-i', '--input', nargs = '+', help = 'The name of the input file(s)', type = str)

	parser.add_argument('-o', '--output', nargs = '+', help = 'The name of the output dictionary', type = str)

	arguments = vars(parser.parse_args())

	main(arguments)
