# Import re
import re

# Create a string
txt = "The rain in Spain"

# Search for "Spain"
x = re.search("Spain", txt)

# Print the span
print(x.span())
