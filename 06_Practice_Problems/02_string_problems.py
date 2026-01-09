"""
String Problems - Practice Exercises
=====================================
Try to solve these problems yourself before looking at the solutions!
"""

print("=" * 60)
print("PROBLEM 1: Reverse a String")
print("=" * 60)
print("Reverse the characters in a string")
print()

# Your code here
# ...

# Solution:
def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

# Alternative solution using loop
def reverse_string_loop(text):
    """Reverse using loop"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Test
print("Solution:")
test_strings = ["hello", "Python", "12345"]
for s in test_strings:
    print(f"'{s}' reversed is '{reverse_string(s)}'")

print("\n" + "=" * 60)
print("PROBLEM 2: Count Vowels")
print("=" * 60)
print("Count the number of vowels in a string")
print()

# Your code here
# ...

# Solution:
def count_vowels(text):
    """Count vowels in text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test
print("Solution:")
test_strings = ["hello", "Python Programming", "aeiou"]
for s in test_strings:
    print(f"'{s}' has {count_vowels(s)} vowels")

print("\n" + "=" * 60)
print("PROBLEM 3: Palindrome Checker")
print("=" * 60)
print("Check if a string is a palindrome (reads same forwards and backwards)")
print()

# Your code here
# ...

# Solution:
def is_palindrome(text):
    """Check if string is palindrome"""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test
print("Solution:")
test_strings = ["racecar", "hello", "level", "A man a plan a canal Panama"]
for s in test_strings:
    result = "is" if is_palindrome(s) else "is not"
    print(f"'{s}' {result} a palindrome")

print("\n" + "=" * 60)
print("PROBLEM 4: Count Words")
print("=" * 60)
print("Count the number of words in a sentence")
print()

# Your code here
# ...

# Solution:
def count_words(text):
    """Count words in text"""
    words = text.split()
    return len(words)

# Test
print("Solution:")
test_strings = [
    "Hello World",
    "Python is awesome",
    "One two three four five"
]
for s in test_strings:
    print(f"'{s}' has {count_words(s)} words")

print("\n" + "=" * 60)
print("PROBLEM 5: Remove Spaces")
print("=" * 60)
print("Remove all spaces from a string")
print()

# Your code here
# ...

# Solution:
def remove_spaces(text):
    """Remove all spaces"""
    return text.replace(" ", "")

# Alternative solution
def remove_spaces_loop(text):
    """Remove spaces using loop"""
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

# Test
print("Solution:")
test_strings = ["hello world", "Python Programming", "a b c d"]
for s in test_strings:
    print(f"'{s}' → '{remove_spaces(s)}'")

print("\n" + "=" * 60)
print("PROBLEM 6: Title Case")
print("=" * 60)
print("Convert string to title case (capitalize first letter of each word)")
print()

# Your code here
# ...

# Solution:
def to_title_case(text):
    """Convert to title case"""
    words = text.split()
    title_words = [word.capitalize() for word in words]
    return " ".join(title_words)

# Test
print("Solution:")
test_strings = ["hello world", "python programming", "the quick brown fox"]
for s in test_strings:
    print(f"'{s}' → '{to_title_case(s)}'")

print("\n" + "=" * 60)
print("PROBLEM 7: Count Character Frequency")
print("=" * 60)
print("Count how many times each character appears in a string")
print()

# Your code here
# ...

# Solution:
def count_characters(text):
    """Count character frequency"""
    freq = {}
    for char in text:
        if char != " ":  # Skip spaces
            freq[char] = freq.get(char, 0) + 1
    return freq

# Test
print("Solution:")
test_string = "hello"
freq = count_characters(test_string)
print(f"Character frequency in '{test_string}':")
for char, count in sorted(freq.items()):
    print(f"  '{char}': {count}")

print("\n" + "=" * 60)
print("PROBLEM 8: First Non-Repeating Character")
print("=" * 60)
print("Find the first character that appears only once")
print()

# Your code here
# ...

# Solution:
def first_non_repeating(text):
    """Find first non-repeating character"""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    for char in text:
        if freq[char] == 1:
            return char
    return None

# Test
print("Solution:")
test_strings = ["hello", "aabbcc", "python", "aabbc"]
for s in test_strings:
    result = first_non_repeating(s)
    if result:
        print(f"'{s}' → First non-repeating: '{result}'")
    else:
        print(f"'{s}' → No non-repeating character")

print("\n" + "=" * 60)
print("PROBLEM 9: Anagram Checker")
print("=" * 60)
print("Check if two strings are anagrams")
print("(contain same characters in different order)")
print()

# Your code here
# ...

# Solution:
def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    # Sort characters and compare
    return sorted(s1) == sorted(s2)

# Test
print("Solution:")
pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("The eyes", "They see"),
    ("python", "java")
]
for str1, str2 in pairs:
    result = "are" if are_anagrams(str1, str2) else "are not"
    print(f"'{str1}' and '{str2}' {result} anagrams")

print("\n" + "=" * 60)
print("PROBLEM 10: Remove Duplicates")
print("=" * 60)
print("Remove duplicate characters from string (keep first occurrence)")
print()

# Your code here
# ...

# Solution:
def remove_duplicates(text):
    """Remove duplicate characters"""
    seen = set()
    result = []
    
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return "".join(result)

# Test
print("Solution:")
test_strings = ["hello", "programming", "aabbcc"]
for s in test_strings:
    print(f"'{s}' → '{remove_duplicates(s)}'")

print("\n" + "=" * 60)
print("BONUS: Longest Word")
print("=" * 60)
print("Find the longest word in a sentence")
print()

# Solution:
def find_longest_word(text):
    """Find longest word"""
    words = text.split()
    if not words:
        return None
    
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Test
print("Solution:")
test_strings = [
    "Python is an awesome programming language",
    "Hello world",
    "The quick brown fox jumps"
]
for s in test_strings:
    longest = find_longest_word(s)
    print(f"Longest word in '{s}':")
    print(f"  → '{longest}' ({len(longest)} characters)")
