# First Option
my_list = ["apple", "banana", "cherry", "apple", "orange", "banana"]

class UniqueList:
    
    def __init__(self, my_list):
        self.my_list = my_list
        self.unique_list = []
        
    def get_unique_list(self):
        for x in self.my_list:
            if x not in self.unique_list:
                self.unique_list.append(x)
        return self.unique_list




# Second Option
my_list = ["apple", "banana", "cherry", "apple", "orange", "banana"]

unique_list = list(set(my_list))

print(unique_list)
