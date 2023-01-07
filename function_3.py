item_deatils = {
    # Id : [name,price,author,is_available]
    '1':["Life's amazing secret",179,"Gaur Golap Das",'english',True],
    '2':["Ikigai",332,"Hector Garcia",'english',True],
    '3':["Wings of Fire",173,"APJ Abdul Kalam",'englisg',True],
    '4':["Godan",200,"Munshi Prem Chand",'hindi',True],
    '5':["Mrinalini",109,"Bankimchandra Chatterjee",'hindi',True],
    '6':["Nirmala",178,"Munshi Prem Chand",'hindi',False],
    '7':["Divya",125,"Yashpal",'hindi',False],
    '8':["1984",300,"George Orwell",'marathi',False],
    '9':["Gathod",250,"P.L Deshpande",'marathi',False],
    '10':["Kosla",304,"V.S Khandekar",'marathi',False]
}

# get all book names
def get_book_names():
    print("Total Books : ",len(item_deatils))
    for i,book in enumerate(item_deatils.values()):
        print(i+1,"",book[0])


# Write a function to get details of a book
def is_book_available(bookId):
    if item_deatils[bookId][-1]:
        return True
    return False


def get_book_details(bookId):
    if is_book_available(bookId):
        print("====Book Details====")
        print("Id\t:",bookId)
        print("Name\t:",item_deatils[bookId][0])
        print("Author\t:",item_deatils[bookId][1])
        print("Price\t:",item_deatils[bookId][2])
    else:
        print("Sorry 😥, This Book is not available")
        print("Please check again later ")



# get_book_details(1)
# book_id =input("Enter book id :")
# details = get_book_details(book_id)
get_book_names()

