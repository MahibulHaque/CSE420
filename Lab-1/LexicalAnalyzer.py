# Get the list of keywords
keywords = ["abstract", "continue", "for", "new", "switch", "assert", "default",
            "goto", "package", "synchronized", "boolean", "do", "if", "private",
            "this", "break", "double", "implements", "protected", "throw",
            "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while", "else if"]
math = ["+", "-", "*", "/", "=", "%", "++", "--", "+=", "-=", "*=", "/=", "%="]
logical = ["<", ">", "<=", ">=", "==", "!", "&&", "||"]
others = [",", ";", "(", ")", "{", "}", "[", "]"]


validKeywords = set()
validIdentifiers = set()
validMath = set()
validLogicalOperators = set()
validNumbers = set()
validOthers = set()
invalidIdentifier = set()



def lexical_analyzer(code, check, store):

    for i in check:  # taking all the values of the check list
        if i in code:
            
            store.add(i)
            code = code.replace(i, " ")
    return code

                

   
        

        
    # return code


# Making an array which I will use later for identifiers and number
output_file = open("output.txt", 'w')


def print_valid_tokens(token_type, assigned_set, separator):
    print(token_type, end="")
    print(separator.join(sorted(assigned_set)))
    output_file.write(f"{token_type} {separator.join(sorted(assigned_set))}\n")



if __name__ == "__main__":
    # read the contents of input.txt
    f = open("input.txt", "r")
    code = f.readlines()
    # remove the newline character from each line
    code = [x.strip() for x in code]
    code_array = []
    
    for i in code:

        if i.startswith("//"):  # Comment
            code = code.replace(i, "")
        else:
            code = lexical_analyzer(i, keywords, validKeywords)
            code = lexical_analyzer(code, logical, validLogicalOperators
        )
            code = lexical_analyzer(code, math, validMath)
            code = lexical_analyzer(code, others, validOthers)
        # if the code is not empty, then it is an identifier or a number.
        # So, I will add it to the code_array for later use out of this loop.
        code_arr = code.split()
        code_array.append(code_arr)

    for i in code_array:
        for j in i:
            if j.isalpha():

                validIdentifiers.add(j)
            else:
                try:
                    if (float(j).is_integer()):
                        validNumbers.add(j)
                except:
                    invalidIdentifier.add(j)
    print_valid_tokens("Keywords: ", validKeywords, ", ")
    print_valid_tokens("Identifiers: ", validIdentifiers, ", ")
    print_valid_tokens("Math: ", validMath, ", ")
    print_valid_tokens("Logical: ", validLogicalOperators
, ", ")
    print_valid_tokens("Number: ", validNumbers, ", ")
    print_valid_tokens("Others: ", validOthers, " ")

