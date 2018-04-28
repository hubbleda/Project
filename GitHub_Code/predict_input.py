old_file=open("finalreviews.csv","r")

user_file=open("users.txt","r")
test_file=open("finalreviews.csv","r")
prototype=open("prototype.txt","w")
user_set=set()

for line in user_file:
    line=line.strip()
    user=line
    user_set.add(user)

total_books=4500
count=0
book_review_dict={}
first=True
for line in test_file:
    orig_line=line
    line = line.strip().split(',')
    user=line[0]
    book=line[1]
    # if its the first entry
    if first==True:
        book_review_dict[book]=[user]
        first=False
        oldbook=book
        prototype.write(orig_line)
    # if its not the first entry and we havent hit a new book
    elif first==False and book in book_review_dict:
        book_review_dict[book].append(user)
        oldbook=book
        prototype.write(orig_line)
    # if we've hit a new book
    # and its not in the dict
    elif first==False and oldbook!=book and book not in book_review_dict:


        users_who_rated= book_review_dict[oldbook]
        users_who_rated=set(users_who_rated)
        unrated_users_for_this_book = user_set.difference(users_who_rated)
        '''
        print("users who didnt rate the prophet" +str(len(unrated_users_for_this_book)))
        print("users= "+str(len(user_set)))
        print("users who rated the prophet= "+str(len(users_who_rated)))
        '''
        total=0
        for unrated_user in unrated_users_for_this_book:
            #print(unrated_user+","+oldbook+","+"0.0")
            new_review=unrated_user+","+oldbook+","+"0.0"+"\n"
            prototype.write(new_review)
            total+=1

        book_review_dict[book]=[user]

        oldbook=book
        prototype.write(orig_line)
        count+=1

        print(str((count/total_books)*100)+ "%")


users_who_rated= book_review_dict[oldbook]
users_who_rated=set(users_who_rated)
unrated_users_for_this_book = user_set.difference(users_who_rated)
prototype.write('\n')
for unrated_user in unrated_users_for_this_book:
    #print(unrated_user+","+oldbook+","+"0.0")
    new_review=unrated_user+","+oldbook+","+"0.0"+"\n"
    prototype.write(new_review)
    total+=1


prototype.close()
test_file.close()
old_file.close()
user_file.close()