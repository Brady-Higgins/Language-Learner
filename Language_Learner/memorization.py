import os
import random as r
import math as m
class Memorize:
    def __init__(self):
        i = 0
        value_dict = {}
        temp_list = []
        with open('C:/Users/Brady/PycharmProjects/Misc.Projects/chinese_characters.txt', 'r', encoding='utf-8') as f:
            for line in f:
                i += 1
                for letter in line:
                    if letter != "\n":
                        temp_list.append(letter)
                value_dict[i] = "".join(temp_list)
                temp_list = []
        f.close()
        self.random_num = r.randint(0, i)
        self.total = i
        self.value_dict = value_dict
    def add_word(self,word):
        if word == "q":
            exit()
        self.value_dict[self.total + 1] = word
        i = 1
        with open('C:/Users/Brady/PycharmProjects/Misc.Projects/chinese_characters.txt', 'w', encoding='utf-8') as f:
            for val in self.value_dict:
                word = self.value_dict[i]
                if i != 1 or self.total + 1:
                    word = word + "\n"
                f.writelines(word)
                i += 1
        f.close()
    def random_word(self):
        self.random_num = r.randint(1, self.total)
        return self.value_dict[self.random_num]
    def random_all(self):
        rand_list = []
        for key in self.value_dict:
            rand_list.append(self.value_dict[key])
        r.shuffle(rand_list)
        rows = self.total / 2
        rows = m.ceil(rows)
        i = 0
        chinese_list = []
        pinyin_list = []
        first_pass = False
        for a in rand_list:
            if first_pass:

                val1 = "".join(temp1)
                val2 = "".join(temp2)
                pinyin_list.append(val2)
                chinese_list.append(val1)
            space = False
            temp1 = []
            temp2 = []
            first_pass = True
            for letter in a:
                if space:
                    temp1.append(letter)
                else:
                    temp2.append(letter)
                if letter == " ":
                    space = True

        for val in pinyin_list:
            if i == 6:
                print("")
                i = 0
            print(val,end=" ")
            i += 1
        print("\n")
        ready = input("Show Chinese? ")
        i = 0
        for val in chinese_list:
            if i == 6:
                print("")
                i = 0
            print(val,end="  ")
            i += 1
        print("\n")
    def __str__(self):
        for key in self.value_dict:
            print(self.value_dict[key], end=" ")
        print("\n")



def main():
    m = Memorize()
    print("""Menu: 
    add character = a         quit = q         print all random = rr
    print random = r          print all = p
    """)
    choice = "dummy_input"
    while choice != "q":
        choice = input("Select: ")
        if choice == "a":
            word_choice = input("Word to add: ")

            m.add_word(word_choice)
            m.__str__()
            m.__init__()
        elif choice == "r":
            print(m.random_word())
        elif choice == "p":
            m.__str__()
        elif choice == "rr":
            m.random_all()


if __name__ =="__main__":
    main()