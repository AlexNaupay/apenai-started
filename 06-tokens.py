# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
import tiktoken

file = open('boletin_sabancaya_202427.txt', "r")
bulletinText = file.read()
file.close()

# The first time this runs, it will require an internet connection to download. Later runs won't need an internet
# connection.
tiktoken.get_encoding("cl100k_base")

# Use tiktoken.encoding_for_model() to automatically load the correct encoding for a given model name.
# gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-4, and gpt-3.5-turbo
encoding = tiktoken.encoding_for_model('gpt-4o-mini')

tokens = encoding.encode(bulletinText)

print("Tokens = %s" % len(tokens))
