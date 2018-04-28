
'''
input_file=open("finaloutput.csv","r")
outfile=open("new_finaloutput.csv","w")
i=0
for line in input_file:
	if i==0:
		pass
	if i%2==1:
		outfile.write(line)
	i+=1
	
input_file.close()
outfile.close()
'''

rating_file=open("new_finaloutput.csv","r")
book_dict={}

for line in rating_file:
	line=line.strip().split(",")
	bookID=line[1]
	if bookID not in book_dict:
		book_dict[bookID]=""
		#print(bookID)
print(len(book_dict))
#print(line)
metadata=open("metadata.json","r")
def parse(file):
    for line in file:
        yield eval(line)

i=0
'''
titlefile=open("book titles.txt","w")
for line in parse(metadata):
	json_book_id = line['asin']
	if 'title' in line:
		book_title=line['title']

		if json_book_id in book_dict:
			titlefile.write(json_book_id+" "+book_title+"\n")

	i+=1
	if i%10000==0:
		
		print("looked at "+str(i)+" items")
print("Done")
'''
#titlefile.close()
metadata.close()
rating_file.close()