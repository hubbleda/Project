file=open("output.csv","r")



i=0
user_dict={}
book_dict={}
for line in file:
    line=line.strip().split(',')


    user=line[0]
    book=line[1]
    if user not in user_dict:
        user_dict[user]=1
    else:
        user_dict[user]+=1

    if book not in book_dict:
        book_dict[book]=1
    else:
        book_dict[book]+=1
    i+=1
print(" users= "+str(len(user_dict))+" with 30+ reviews")
print(" books= " + str(len(book_dict)) + " with 200+ reviews")
import operator

sorted_user_dict=sorted(user_dict.items(),key=operator.itemgetter(1),reverse=True)
sorted_user_dict=sorted_user_dict[0:int(len(sorted_user_dict)/16)]
print(len(sorted_user_dict))

count=0
print(sorted_user_dict[len(sorted_user_dict)-5:])

file.close()

sorted_user_dict=dict(sorted_user_dict)
file=open("output.csv","r")

new_book_dict={}
for line in file:
    line = line.strip().split(',')
    user = line[0]
    book = line[1]

    if user in sorted_user_dict:
        if book not in new_book_dict:
            new_book_dict[book] = 1
        else:
            new_book_dict[book] += 1


print(" number of books the top "+str(len(sorted_user_dict))+ " users rated= "+str(len(new_book_dict)))
file.close()

final_file=open("finaloutput.csv","w")
file=open("output.csv","r")


header="userID,bookID,score"+"\n"
final_file.write(header)

for line in file:
    orig_line=line
    line=line.strip().split(",")
    user=line[0]
    book=line[1]

    if user in sorted_user_dict:
        if book in new_book_dict:
            output_str=orig_line #+"\n"
            final_file.write(output_str)

file.close()
final_file.close()
print("done")