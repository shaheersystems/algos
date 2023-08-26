


# define class of hash table
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
t = HashTable() # create object of hash table



# store calender in hashtable
t["jan"] = 31
t["feb"] = 28
t["mar"] = 31
t["apr"] = 30
t["may"] = 31
t["jun"] = 30
t["jul"] = 31
t["aug"] = 31
t["sep"] = 30
t["oct"] = 31
t["nov"] = 30   
t["dec"] = 31

val=input("Enter the month: ")
val=val.lower()
val=val[0:3]
print("Number of days in",val,"is",t[val])