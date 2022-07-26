#!/usr/bin/env python3

import os
import random
import numpy as np

def main():
    # read words in poems
    words = set([])
    poems = []
    for f in os.listdir("."):
        if f.endswith(".poem"):
            poems.append(f)
            poem = [line for line in open(f, "r").readlines()]
            for line in poem:
                line = ''.join([ch for ch in line if (ch.isalpha()) | (ch == ' ')])
                for word in line.split(" "):
                    words.add(word.lower())

    words = list(words)

    primary_transition = np.zeros((len(words), len(words)))
    secondary_transition = np.zeros((len(words), len(words)))

    # construct transition matrices
    for f in poems:
        poem = [line for line in open(f, "r").readlines()]
        sequence = []
        for line in poem:
            line = ''.join([ch for ch in line if (ch.isalpha()) | (ch == ' ')])
            for word in line.split(" "):
                sequence.append(word.lower())

        for i in range(len(sequence) - 2):
            current_state = words.index(sequence[i])
            next_state = words.index(sequence[i+1])
            primary_transition[next_state][current_state] += 1

            secondary_state = words.index(sequence[i+2])
            if secondary_state != -1:
                secondary_transition[secondary_state][current_state] += 1

    generated = []
    for i in range(20):
        if i == 0:
            generated.append(words[np.random.randint(len(words))])
        else:
            stack = []
            for word in words:
                for i in range(int(primary_transition[words.index(word)][words.index(generated[-1])])):
                    stack.append(word.lower())
            random.shuffle(stack)

            new_word = stack[0]

            if i > 1:
                while True:
                    try:
                        confidence = secondary_transition[words.index(new_word)][words.index(generated[-2])] / np.sum(secondary_transition[:][words.index(generated[-2])]) # err
                        if confidence > 0.5:
                            break
                    except Exception as e:
                        pass

                    stack = []
                    for word in words:
                        for i in range(int(primary_transition[words.index(word)][words.index(generated[-1])])):
                            stack.append(word.lower())
                    random.shuffle(stack)
                    new_word = stack[0]

            generated.append(new_word)

        print(generated[-1])

    generated_string = ""
    for word in generated:
        generated_string += word + " ";

    print(generated_string)

if __name__ == "__main__":
    main()
