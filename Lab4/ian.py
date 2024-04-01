def find_chooses(regex):
    matches = []
    stack = []
    for i, char in enumerate(regex):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                start_index = stack.pop()
                substring = regex[start_index + 1:i]
                substring = substring.replace("|", ", ")
                matches.append(substring)

    # Remove substrings from the regex
    for match in matches:
        regex = regex.replace("(" + match.replace(", ", "|") + ")", "")

    return matches, regex

regex = "(S|T)(U|V)W*Y+24"
sublists, regex = find_chooses(regex)

def find_operators(regex):
    num = ""
    for i in regex:
        if i.isalnum():
            num += i
        elif i == "*":
            print("inmultirea cu", num)
            num = ""
        elif i == "+":
            print("adunarea cu", num)
            num = ""


find_operators(regex)
print("Matches:", sublists)
print("Remaining regex:", regex)
