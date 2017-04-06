### Taking a string and changing a letter in the string
def mutate_string(string, position, character):
    ### Convert string to a list
    l = list(string)
    ### At the given position, change to the given character
    l[position] = character
    ### Join the list back into a string
    string = ''.join(l)
    ### Print that shit
    print(string)

### Slice the string, change to the given character at the given postion
### Add the rest of the string after the added character
    string = string[:position] + character + string[position+1:]
    print(string)

mutate_string('Frank Sinatra and the Rat Pack', 14, 's')