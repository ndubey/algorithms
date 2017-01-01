#Trie insert and search

class TrieNode:
    def __init__(self, character):
        self.val = character
        self.li = []

class Trie:
    def __init__(self):
        self.root = []

    def pInsert(self, word, li):
        if li == []:
            if len(word) != 0:
                t = TrieNode(word[0])
                li.append(t)
                self.pInsert(word[1:],t.li)
            else:
                li.append('$')
        else:
            #search in li
            if len(word) != 0:
                for t in li:
                    if t != '$' and t.val == word[0]:
                        return self.pInsert(word[1:],t.li)
                t = TrieNode(word[0])
                li.append(t)
                self.pInsert(word[1:], t.li)
            else:
                li.append('$')


    def insert(self, word):
        if self.root == []:
            t = TrieNode(word[0])
            self.root.append(t)
            self.pInsert(word[1:], t.li)
        else:
            self.pInsert(word, self.root)

    def allBelow(self, li, ret, actual):
        if li == []:
            print("problem")
            return ret
        for t in li:
            if t=='$':
                print("found exact match? ")
                ret.append(actual)
        return ret

    def pSearch(self, word, li, actual):
        if li == []:
            return []
        else:
            if len(word) == 0:
                ret = []
                return self.allBelow(li, ret, actual)
            for t in li:
                if t.val == word[0]:
                    print("found char: "+word[0])
                    return self.pSearch(word[1:], t.li, actual)
                else:
                    return []

    def search(self, word):
        if self.root == []:
            return []
        else:
            return self.pSearch(word,self.root, word)

print(" Enter some words to insert in trie. Note type 'Done' to finish:")

word = input()
counter = 6
t = Trie()
#print(word != 'Done')
#print(word != "")
while word != 'Done' and word != "":
    counter -= 1
    if counter == 0:
        print("If you want to finish just enter 'Done'")
        counter = 6
    print("Inserting word: "+word)
    t.insert(word)
    word = input()
    #print(word != 'Done')
    #print(word != "")

#Now do search recommandation based on constructed Trie
print("enter something to get recommandation:")
word = input()
li = t.search(word)
print(li)



