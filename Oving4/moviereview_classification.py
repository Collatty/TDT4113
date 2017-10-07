from Plab.Oving4 import moviereview_reader
import math
import os
import time

start_time = time.time()

class Classification():

    def __init__(self, directory):
        self.directory = directory
        self.total_documents = len(os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/"+directory+"/train/pos"))*2
        print (" total documents time - time elapsed: {:.2f}s".format(time.time() - start_time))
        self.reader = moviereview_reader.Reader()
        self.positive_reviews = []
        self.negative_reviews = []
        self.positive_words, self.negative_words = self.reader.information_value(directory + "/train/pos/", directory + "/train/neg/")
        print (" training time - time elapsed: {:.2f}s".format(time.time() - start_time))
        self.positive_words = dict(self.positive_words)
        self.negative_words = dict(self.negative_words)

        print ("inititating time - time elapsed: {:.2f}s".format(time.time() - start_time))

    def classify(self, filename):
        unique_words = self.reader.read_single_from_file(filename)
        positivity = 0
        negativity = 0
        for i in range(len(unique_words)):
            if unique_words[i] in self.positive_words.keys():
                positivity += math.log(self.positive_words[unique_words[i]])
                negativity += math.log(0.01)
            if unique_words[i] in self.negative_words.keys():
                negativity += math.log(self.negative_words[unique_words[i]])
                positivity += math.log(0.01)
        if positivity > negativity:
            self.positive_reviews.append(filename.split("/")[3])
        elif positivity < negativity:
            self.negative_reviews.append(filename.split("/")[3])
        else:
            print("VAnskelig å si om denne er positiv eller negativ")

    def multiple_classify(self, sub_directory):
        names = os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/" + self.directory + sub_directory)
        for file in names:
            self.classify(self.directory+sub_directory+file)
        print ("time elapsed: {:.2f}s".format(time.time() - start_time))

    def percentage_of_correctness(self):
        correct = 0
        for name in self.positive_reviews:
            if name in os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/"+self.directory+"/test/pos/"):
                correct+=1
        print ("percentage pos - time elapsed: {:.2f}s".format(time.time() - start_time))
        for name in self.negative_reviews:
            if name in os.listdir("/Users/macbookpro/Documents/Skole/Proglab2/Plab/Oving4/data/"+self.directory+"/test/neg/"):
                correct +=1
        return correct/self.total_documents



def main():
    print ("Start time  - time elapsed: {:.2f}s".format(time.time() - start_time))
    classifier = Classification("alle")
    classifier.multiple_classify("/test/pos/")
    print ("classifing time pos - time elapsed: {:.2f}s".format(time.time() - start_time))
    classifier.multiple_classify("/test/neg/")
    print ("classifying time neg -time elapsed: {:.2f}s".format(time.time() - start_time))
    print(classifier.percentage_of_correctness())
    print ("total time elapsed: {:.2f}s".format(time.time() - start_time))
main()
