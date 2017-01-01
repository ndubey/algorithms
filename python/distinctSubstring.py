

#A trie node class
class TrieNode:
    def __init__(self, value):
        self.val = value
        self.li = []

#construct a trie class 
class Trie:
    def __init__(self):
        self.root = []

    def _insertEnd(self, li):
        if not '$' in li:
            li.append('$')

    def _insertWord(self,word,li):
        if len(word) < 1:
            #done inserting add $ in li if not already there
            self._insertEnd(li)
            return
        print("inserting: "+word[0])
        if li == []:
            t = TrieNode(word[0])
            li.append(t)
            self._insertWord(word[1:],t.li)
        else:
            #first search the character in li if not present then only insert
            for elem in li:
                if elem != '$' and elem.val == word[0]:
                    return self._insertWord(word[1:],elem.li)
            #not present
            t = TrieNode(word[0])
            li.append(t)
            self._insertWord(word[1:],t.li)

    def insertWord(self, word):
        #error check
        if len(word) < 1:
            return
        self._insertWord(word,self.root)

    def _countNodes(self,li):
        if li == []:
            return 0
        else:
            count = 0
            for elem in li:
                if elem is not '$':
                    count += 1
                    count += self._countNodes(elem.li)
            return count

    def countNodes(self):
        if self.root != []:
            return self._countNodes(self.root)
        else:
            return 0

    def _countWords(self, li):
        if li == []:
            return 0
        count = 0
        for elem in li:
            if elem == '$':
                count += 1
            else:
                count += self._countWords(elem.li)
        return count

    def countWords(self):
        if self.root != []:
            return self._countWords(self.root)
        else:
            return 0
        

print("Enter a string for which all distinct substring has to be found out")

inputStr = input()


#now costruct a trie with all suffixes of str

t = Trie()
for i in range(len(inputStr)):
    t.insertWord(inputStr[i:])

#number of nodes same as result number of unique substring without taking into acount null string
print('Total number of nodes in the Trie:'+ str(t.countNodes()))

#total real number of strings in Trie
print('Total real words in the Trie:'+str(t.countWords()))
