from random import sample
import time
import sys
from termcolor import colored

if __name__ == "__main__":
	string = str(input("Enter a sentence:"))
	memory = int(input("Enter many letters to remember:"))
	text = list(string)
	text_length = len(text)
	print(f"Text:")
	print(string)


n_grams = [[[text[i+j] for j in range(k+1)] for i in range(text_length-k)] for k in range(memory+1)]

print(n_grams[memory])



#print(three_grams)

def encode(sleep_time=0.5):
	code = ""
	print("Code:")
	for i in range(text_length):
		time.sleep(sleep_time)
		sampled_index = sample(range(text_length-i), 1)[0]
		sampled_character = text[sampled_index]
		tries = 1
		sys.stdout.write(u"\u001b[1000D" + colored(str(code), "blue") + colored(str(sampled_character), "red") + str(string[i+1:]) + " - " + colored(str(tries), "red"))
		sys.stdout.flush()
		while sampled_character != string[i]:
			time.sleep(sleep_time)
			tries += 1
			sampled_index = sample(range(text_length-i), 1)[0]
			sampled_character = text[sampled_index]
			sys.stdout.write(u"\u001b[1000D" + colored(str(code), "blue") + colored(str(sampled_character), "red") + str(string[i+1:]) + " - " + colored(str(tries), "red"))
			sys.stdout.flush()
		time.sleep(sleep_time*2)
		code += str(tries)
		del text[sampled_index]
		time.sleep(sleep_time)
		sys.stdout.write(u"\u001b[1000D" + colored(str(code), "blue"))
		sys.stdout.flush()
	print("\n")
	print
encode()