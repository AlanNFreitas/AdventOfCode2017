from adventutils import input_file, read_phrases

passphrase_list = read_phrases(input_file())
count = 0
for passphrase in passphrase_list:
    s = set(passphrase)
    if len(s) == len(passphrase):
        count += 1

print(count)

    
