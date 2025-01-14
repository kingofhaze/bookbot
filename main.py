def wordcount(file_contents):
    return len(file_contents.split())

def charcount(file_contents):
    charCount = {}
    for char in file_contents.lower():
        if char.isalpha():
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
    
    return sorted(charCount.items(), key=lambda x: x[1], reverse=True)

def main():
    file = 'books/frankenstein.txt'

    with open(file) as f:
        file_contents = f.read()
        wc = wordcount(file_contents)
        charList = charcount(file_contents)

        print(f'--- Begin report of {file} ---')
        print(f'{wc} words found in the document\n')
        for char in charList:
            print(f"The '{char[0]}' character was found {char[1]} times")
        print(f'--- End report ---')

main()