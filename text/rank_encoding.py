from random import sample
import time
import sys
from termcolor import colored

if __name__ == "__main__":
	text = str(input("Enter a sentence:"))
	#memory = int(input("How many letters to remember:"))
	print(f"Text: {text}")
	sleep_time = 0.1

def get_n_grams(text, memory):
	text_length = len(text)
	n_grams = [["".join([text[i+j] for j in range(k+1)]) for i in range(text_length-k)] for k in range(memory+1)]
	return n_grams

def get_ranks(n_grams):
	all_ranks = []
	for i in range(len(n_grams)):
		freq = dict()
		for item in n_grams[i]:
			if item in freq:
				freq[item] += 1
			else:
				freq[item] = 1
		freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
		ranks = dict()
		value_ = 0
		rank_ = 0
		for key, value in freq.items():
			if value == value_:
				ranks[key] = rank_
			else:
				rank_ += 1
				ranks[key] = rank_
			value_ = value
		ranks = dict((key, value) for key, value in ranks.items())
		all_ranks.append(ranks)
	return all_ranks

def rank_encode(text, memory):
	n_grams = get_n_grams(text, memory)
	all_ranks = get_ranks(n_grams)
	code = ""
	for index, letter in enumerate(text):
		if index < memory:
			code += str(all_ranks[index][text[0:index+1]])
		else:
			code += str(all_ranks[memory][text[index-memory:index+1]])
	return int(code)

# Printed version
def print_rank_encode(text, memory):
	n_grams = get_n_grams(text, memory)
	all_ranks = get_ranks(n_grams)
	code = ""
	print(f"{memory} memory code:")
	for index, letter in enumerate(text):
		if index < memory:
			sys.stdout.write(u"\u001b[1000D" + colored(code, "blue") + colored(text[index], "red") + text[index+1:])
			sys.stdout.flush()
			time.sleep(sleep_time)
			code += str(all_ranks[index][text[0:index+1]])			
		else:
			sys.stdout.write(u"\u001b[1000D" + colored(code, "blue") + colored(text[index], "red") + text[index+1:])
			sys.stdout.flush()
			time.sleep(sleep_time)
			code += str(all_ranks[memory][text[index-memory:index+1]]) 
	sys.stdout.write(u"\u001b[1000D" + colored(str(code), "blue"))
	sys.stdout.flush()
	print("\n")
	print

for i in range(10):
	print_rank_encode(text, memory=i)


