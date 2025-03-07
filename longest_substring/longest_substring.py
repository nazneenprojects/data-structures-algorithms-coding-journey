"""
Longest Substring

"""

def longest_substring(s: str) -> int:
    """

    :return:
    """
    maxLen = 1
    if s == '':
        return 0

    for i in range(len(s)):
        substring = s[i]
        print("substring:",substring)
        for j in range(i+1, len(s)):
            if s[j] not in substring:
                print(s[j])
                substring = substring + s[j]
                print("substring:",substring)
                maxLen = max(maxLen, len(substring))
                print("maxLen:", maxLen)
            else:
                print("break loop")
                break

    return maxLen



def longest_substring_2(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): Input string
    Returns:
        int: Length of the longest substring without repeating characters
    """
    if not s:
        return 0

    # Dictionary to store the last position of each character
    char_position = {}

    # Variables to track the current and maximum length
    max_length = 0
    start = 0

    for current_pos, char in enumerate(s):
        # If we've seen this character before and its position is >= start
        if char in char_position and char_position[char] >= start:
            # Move the start pointer to the position after the last occurrence
            start = char_position[char] + 1
        else:
            # Update max_length if current window is longer
            current_length = current_pos - start + 1
            max_length = max(max_length, current_length)

        # Update the last position of current character
        char_position[char] = current_pos

    return max_length


# Function to return the actual substring
def get_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.

    Args:
        s (str): Input string
    Returns:
        str: Longest substring without repeating characters
    """
    if not s:
        return ""

    char_position = {}
    max_length = 0
    start = 0
    max_start = 0
    max_end = 0

    for current_pos, char in enumerate(s):
        if char in char_position and char_position[char] >= start:
            start = char_position[char] + 1
        else:
            current_length = current_pos - start + 1
            if current_length > max_length:
                max_length = current_length
                max_start = start
                max_end = current_pos + 1

        char_position[char] = current_pos

    return s[max_start:max_end]



if __name__ == "__main__":
    input = "abcabcbb"
    # output : 3
    output = longest_substring(input)
    print(output)
    output1 = longest_substring_2(input)
    print(output1)
