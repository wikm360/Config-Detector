text = ["mmadhello" , "hellommd" , "chtori" , "hello"]
target = "hello"
count = len(text)
count_target = len(target)
list_target = list(target)
for i in range(0,count) :
    finish=0
    list_input = list(text[i])
    count_word = len(list_input)
    if count_word == count_target :
        for j in range(0,count_word) :
            if list_input[j] == list_target[j] :
                finish += 1
            else :
                finish += -1
        if finish == count_target :
            print("index " + str(i) + " is equl")
    else :
        pass

