import os
import operator



__author__ = "Collatty"

class Reader:

    unwanted_chars = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~;!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~;"

    def __init__(self):
        self.name = "Reader"

    def read_single_from_file(self, filename, n_gram=None):
        if n_gram is None:
            unique_words = set()
            for line in open("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/" + filename, encoding='utf-8'):
                words = line.split()
            for i in range(len(words)):
                for chars in self.unwanted_chars:
                    words[i] = words[i].strip(chars)
                unique_words.add(words[i].lower())
            return list(unique_words)
        else:
            underscore = "_"
            unique_words = set()
            for line in open("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/" + filename, encoding='utf-8'):
                words = line.split()
            for i in range(len(words)):
                for chars in self.unwanted_chars:
                    words[i] = words[i].strip(chars)
                unique_words.add(words[i].lower())
            for i in range(len(words)-n_gram+1):
                unique_words.add(underscore.join(words[i:i+n_gram]).lower())
            return list(unique_words)


    def read_multiple_from_file(self, directory):
        #pos = os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/" + filename)
        names = os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/" + directory)
        #words_in_positive = []
        words_in_files = []
        #for file in pos:
            #words_in_positive.append(self.read_single_from_file("pos/"+file))
        for file in names:
            words_in_files.append(self.read_single_from_file(directory + file,3))
        print("read multiple ferdig")
        return words_in_files #,words_in_positive

    def find_most_frequent(self, matrix_of_words):
        list_of_words = []
        for words in matrix_of_words:
            for word in words:
                list_of_words.append(word)
        dictionary_counted = {}
        for word in list_of_words:
            if word in dictionary_counted.keys():
                dictionary_counted[word] += 1
            else:
                dictionary_counted.update({word: 1})
        sorted_dict_counted = sorted(dictionary_counted.items(), key=operator.itemgetter(1))
        sorted_dict_counted = self.remove_stop_words(sorted_dict_counted)
        return sorted_dict_counted

    def remove_stop_words(self, sorted_dict_count):
        stop_words = [word.rstrip() for word in open("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/stop_words.txt")]
        sorted_list = []
        for i in range(len(sorted_dict_count)-1, 0, -1):
            if sorted_dict_count[i][0] not in stop_words and sorted_dict_count[i][0] != '':
                sorted_list.append(sorted_dict_count[i])
        return sorted_list

    def top_25(self, sorted_list):
        print(sorted_list[len(sorted_list)-1:len(sorted_list)-26:-1])

    def information_value(self, directory_pos, directory_neg):
        pos = self.read_multiple_from_file(directory_pos)
        neg = self.read_multiple_from_file(directory_neg)
        total_documents = len(pos)+ len(neg)
        pos = dict(self.find_most_frequent(pos))
        neg = dict(self.find_most_frequent(neg))
        total_word_count= {}
        total_word_count.update(pos)
        for key in neg.keys():
            if key in total_word_count.keys():
                total_word_count[key] += neg[key]
            else:
                total_word_count.update({key: neg[key]})
        pruned_total_word_count = self.pruning(total_word_count,total_documents)
        positive_information_value = {}
        negative_information_value = {}
        for key in total_word_count.keys():
            if key in pos.keys():
                positive_information_value.update({key: (pos[key]/pruned_total_word_count[key])})
            if key in neg.keys():
                negative_information_value.update({key: (neg[key]/pruned_total_word_count[key])})
        pos_sorted_information_value = sorted(positive_information_value.items(), key=operator.itemgetter(1))
        neg_sorted_information_value = sorted(negative_information_value.items(), key=operator.itemgetter(1))
        #self.top_25(pos_sorted_information_value)
        #self.top_25(neg_sorted_information_value)
        return pos_sorted_information_value, neg_sorted_information_value

    def pruning(self,total_word_count,document_count):
        delete_keys = []
        for key in total_word_count.keys():
            if total_word_count[key]/document_count < 0.02:
                delete_keys.append(key)
        for key in delete_keys:
            del total_word_count[key]
        return total_word_count



