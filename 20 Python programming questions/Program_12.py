#   Longest Common Prefix
#   Write a function to find the longest common prefix string amongst an array of strings.


def longest_common_prefix(strs):
    if not strs:
        return ""  # Return empty string if the list is empty

    # Start with the first string as the longest common prefix
    prefix = strs[0]

    # Compare the prefix with each string in the array
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]  # Reduce the prefix by one character

    return prefix

# Example usage:
strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(result)  # Output: "fl"
