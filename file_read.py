# Normal method
f = open('demo.txt', 'r')

print(f.name)
print(f.mode)

f.close()

# Context manager - read
with open('demo.txt', 'r') as f:

    for line in f:
        print(line, end='')
    f_content = f.readlines()
    f_content = f.read(100)
    print(f_content, end='')

    size_read = 10
    f_content = f.read(size_read)
    print(f_content, end='*')

    f.seek(0)

    f_content = f.read(size_read)
    print(f_content)

    
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size_read) 


# Context manager - Write
with open('demo.txt', 'r') as rf:
    f.write('Test')
    f.seek(0)
    f.write('R')
    # --------------------
    with open('demo_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            # -----------------
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)