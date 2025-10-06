"""
1. Format commas correctly
Input:
once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched

Output:
once upon a time, in a land far far away lived a princess, whose beauty was yet unmatched

2. Format newlines correctly
Input:
once upon a time, in a land far far away lived a princess, whose beauty was yet unmatched

max_len_text: unmatched (9)
max_len_line: 9*3=27


Output:
once upon a time, in a land
far far away lived a
princess, whose beauty was
yet unmatched

"""

class Format:
    def format_text(self, text: str):
        if not text:
            return ''
        
        if text[-1] == ',':
            text = text[:-1]

        new_text = []
        for i in range(len(text)):
            if text[i] == ',':
                comma = ','
                if new_text[i-1] == ' ':
                    new_text.pop()
                if text[i+1] != ' ':
                    comma = ', '
                new_text.append(comma)
            else:
                new_text.append(text[i])

        joined_new_text = "".join(new_text)
        splitted_new_text = joined_new_text.split()
        max_len = len(max(splitted_new_text, key=lambda x: len(x)))
        result = self.format_line(splitted_new_text, max_len * 3)

        return result
    
    def format_line(self, words: list, line_len: int):
        new_text = []

        count = -1
        for i in words:
            count += len(i) + 1
            if count > line_len:
                new_text.pop()
                new_text.append('\n')
                new_text.append(i)
                new_text.append(' ')
                count = len(i)
            else:
                new_text.append(i)
                new_text.append(' ')

        new_text.pop()
        new_text.append('\n')
        result = "".join(new_text)
        return result.strip()

try:
    text = input()
    f = Format()
    res = f.format_text(text)
    print(res)
except Exception as e:
    print('')

def test_format():
    f = Format()
    test_cases = [
        ("", ""),  # Empty input
        (",,, ,,,", ", , , ,"),  # Only commas
        ("word1,word2,word3", "word1, word2, word3"),  # No spaces after commas
        ("word1word2word3", "word1word2word3"),  # No spaces
        ("a", "a"),  # Single character
        (",", ","),  # Single comma
        ("word1, word2, word3,", "word1, word2, word3,"),  # Ends with a comma
        ("word, " * 10000, "word, " * 10000),  # Large input
        (None, None),  # Non-string input, expected exception
        (12345, None)  # Non-string input, expected exception
    ]
    
    for text, expected in test_cases:
        try:
            res = f.format_text(text)
            assert res == expected, f"Test failed for input: {text}"
        except Exception as e:
            print(f"Exception for input: {text} -> {e}")

# test_format()
