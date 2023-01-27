from time import time

start = time()

new_word = "Pneumonoultramicroscopicsilicovolcanoconiosis Hippopotomonstrosesquippedaliophobia "
text = new_word.split()
a = " "

for i in text:
    a = a + str(i[0]). upper()

print(a)

end = time()
execution_time = end - start
print("Execution Time:", execution_time)
