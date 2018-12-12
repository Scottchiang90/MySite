from niceanot import *


def generate_sentences(seed=None, num = 1):
    if num < 1:
        return ""

    final = reconstituted_model.make_sentence(seed)
    for i in range(num-1):
        final += " " + reconstituted_model.make_sentence()
    return final
