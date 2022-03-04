"""Exercise 19 (part 1): Remove Control Flag"""

# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file

num_bytes = 16
with open('foobar.file', 'rb') as fp:
    while True:
        chunk = fp.read(num_bytes)
        if chunk == '':  # end of file, stop running.
            break
        print(chunk)
        # process(chunk)
