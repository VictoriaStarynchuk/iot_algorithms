class WChain:
    def __init__(self, file):
        self.file = file

    def _read_data(self):
        words = []
        with open(self.file, "r") as file:
            amount_of_words = int(file.readline())
            for line in range(amount_of_words):
                words.append(file.readline().strip())
        return words

    def count_of_chains(self):
        words = sorted(self._read_data(), key=len)
        chain_of_words = {word: 1 for word in words}
        chains_of_word_list = {word: [word] for word in words}
        for word in chain_of_words.keys():
            if len(word) == 1:
                continue
            for iterator in range(len(word)):
                word_to_check = word.replace(word[iterator], '', 1)
                if word_to_check in chain_of_words:
                    if chain_of_words[word_to_check] + 1 > chain_of_words[word]:
                        chain_of_words[word] = chain_of_words[word_to_check] + 1
                        chains_of_word_list[word] += chains_of_word_list[word_to_check]

        result_chain_of_word = max(chain_of_words.values())
        result_word_chain_list = list(chain_of_words.keys())[list(chain_of_words.values()).index(result_chain_of_word)]
        print(chains_of_word_list[result_word_chain_list])
        WChain._write_data(result_chain_of_word)
        return result_chain_of_word

    def _write_data(answer):
        with open("wchain.out", "w") as file:
            file.write(str(answer))


if __name__ == '__main__':
    w = WChain("wchain.in")
    w.count_of_chains()
