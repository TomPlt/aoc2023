def main():
    with open("data.txt", 'r') as f:
        input_lines = [line.strip() for line in f.readlines()]

    total_sum = 0
    dict_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in input_lines:
        first_digit = None
        last_digit = None
        i = 0
        
        while i < len(line):
            found = False
            # Check for each number word in the line
            for word, num in dict_num.items():
                if line[i:i+len(word)] == word:
                    if first_digit is None:
                        first_digit = num
                    last_digit = num
                    i += len(word)  # Skip ahead by the length of the word
                    found = True
                    break
            
            # Check for digits
            if not found and line[i].isdigit():
                digit = int(line[i])
                if first_digit is None:
                    first_digit = digit
                last_digit = digit
                i += 1
            elif not found:
                i += 1

        if first_digit is not None and last_digit is not None:
            line_sum = first_digit * 10 + last_digit
            total_sum += line_sum

    print("Total Sum:", total_sum)

if __name__ == '__main__':
    main()
