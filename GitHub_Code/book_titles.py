old_file=open("finaloutput_known_booktitles.csv","r")
book_titles=open("book titles.txt","r")

newoutput_file=open("finalreviews.csv","w")
book_dict={}

for line in book_titles:
    line=line.strip().split()
    bookID=line[0]
    book_name=line[1:]
    book_name=" ".join(book_name)
    book_dict[bookID]=book_name



for line in old_file:
    original_line=line
    line=line.strip().split(',')

    userID=line[0]
    bookID=line[1]
    rating=line[2]
    book_title=book_dict[bookID]

    new_book_title=book_title.replace(","," ")


    newline=userID+","+new_book_title+","+rating+"\n"
    newoutput_file.write(newline)
old_file.close()
book_titles.close()
newoutput_file.close()