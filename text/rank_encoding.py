import numpy as np
from random import sample
import time
import sys
from termcolor import colored

if __name__ == "__main__":
	text = str(input("Enter a sentence:"))
	memory = int(input("How many letters to remember:"))
	print(f"Text: {text}")
	sleep_time = 0.1

def get_n_grams(text, memory):
	text_length = len(text)
	n_grams = [["".join([text[i+j] for j in range(k+1)]) for i in range(text_length-k)] for k in range(memory+1)]
	return n_grams

def get_ranks(text, memory):
	n_grams = get_n_grams(text, memory)
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
	all_ranks = get_ranks(text, memory)
	code = ""
	for index, letter in enumerate(text):
		if index < memory:
			code += str(all_ranks[index][text[0:index+1]])
		else:
			code += str(all_ranks[memory][text[index-memory:index+1]])
	return int(code)

def get_frequency(all_ranks, k=1, memory=3):
	freq_ = 0
	for key, value in all_ranks[memory].items():
		if value == k:
			freq_ += 1
	k_freq = freq_ / len(all_ranks[memory])
	return k_freq

def get_entropies():
	entropies = []
	for i in range(memory):
		all_ranks = get_ranks(text, i)
		unique_freq = set(value for value in all_ranks[i].values())
		entropy = 0
		for k in unique_freq:
			k_freq = get_frequency(all_ranks, k, i)
			entropy += k_freq * np.log2(1/k_freq)
		entropies.append(entropy)
	return entropies

# Printed version
def print_rank_encode(text, memory):
	all_ranks = get_ranks(text, memory)
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
	print
entropies = get_entropies()
for i in range(memory):
	print_rank_encode(text, memory=i)
	print(f" - Entropy: {entropies[i]}")