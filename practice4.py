import array as arr

numbers = arr.array("i", [1, 2, 3, 4, 5, 12, 13, 14, 15, ])
print(numbers)
print(numbers[7])
print(numbers.index(12))
import re

# The first regex pattern, "blast\w*", makes use of the \w special character,
# which will match alphanumeric characters and underscores.
# Adding the * quantifier directly after it will match zero or more characters of
REGEX_REPLACEMENTS = [
    (r"blast\w*", "😤"),
    (r" [-T:+\d]{25}", ""),
    (r"\[support\w*\]", "Agent "),
    (r"\[johndoe\]", "Client"),
]
# For the time stamp, you use an extended character
# set of [-T:+\d] to match all the possible characters that you might find in the time stamp.
# Paired with the quantifier {25}, this will match any possible time stamp, at least until the year 10,000.
# The special character, \d, matches any digit character
# The third regex pattern is used to select any user string that starts with the keyword "support".
# Note that you escape (\) the square bracket ([) because otherwise the keyword
# would be interpreted as a character set.

# Finally, the last regex pattern selects the client username string and replaces it with "Client".
transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""
# Another vital part of the first pattern is that the re.
# IGNORECASE flag makes it a case-insensitive pattern. So now,
# any substring containing blast, regardless of capitalization, will be matched and replaced.
for old, new in REGEX_REPLACEMENTS:
    transcript = re.sub(old, new, transcript, flags=re.IGNORECASE)

print(transcript)
#nb There are more quantifiers, though. If you used [abc]{10},
# it would match exactly ten characters of a, b or c in any order and any combination.
# Also note that repeating characters is redundant, so [aa] is equivalent to [a].


# Now your transcript has been completely sanitized, with all noise removed!

