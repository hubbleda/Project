old_file=open("new_finaloutput.csv","r")
book_titles=open("book titles.txt","r")

newoutput_file=open("finaloutput_known_booktitles.csv","w")
book_dict={}

for line in book_titles:
    line=line.strip().split()
    bookID=line[0]
    book_name=line[1:]
    book_name=" ".join(book_name)
    book_dict[bookID]=book_name

unknown=0
unknown_books={}
#print (book_dict['B00KF0URBM'])
for line in old_file:
    original_line=line
    line=line.strip().split(',')
    poss_bookID=line[1]
    if poss_bookID in book_dict:
        newoutput_file.write(original_line)
    else:
        if poss_bookID not in unknown_books:
            #print(poss_bookID)
            unknown_books[poss_bookID]=""
            unknown+=1
print(unknown)
old_file.close()
book_titles.close()
newoutput_file.close()