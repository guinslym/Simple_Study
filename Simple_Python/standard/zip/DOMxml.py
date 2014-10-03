__author__ = 'Dog'
from xml.dom import minidom

doc = minidom.Document()
doc.appendChild(doc.createComment("This is a simple xml."))
booklist = doc.createElement("booklist")
doc.appendChild(booklist)


def add_book(newbook):
    book = doc.createElement("book")
    book.setAttribute("id", newbook["id"])

    title = doc.createElement("title")
    title.appendChild(doc.createTextNode(newbook["title"]))
    book.appendChild(title)

    author = doc.createElement("author")
    name = doc.createElement("name")
    firstname = doc.createElement("firstname")
    firstname.appendChild(doc.createTextNode(newbook["firstname"]))
    lastname = doc.createElement("lastname")
    lastname.appendChild(doc.createTextNode(newbook["lastname"]))
    name.appendChild(firstname)
    name.appendChild(lastname)
    author.appendChild(name)
    book.appendChild(author)

    pubdate = doc.createElement("pubdate")
    pubdate.appendChild(doc.createTextNode(newbook["pubdate"]))
    book.appendChild(pubdate)
    booklist.appendChild(book)


add_book({"id": "1001", "title": "An apple", "firstname": "Peter", "lastname": "Zhang", "pubdate": "2014-1-2"})
add_book({"id": "1002", "title": "Love", "firstname": "Mike", "lastname": "Li", "pubdate": "2013-11-2"})
add_book({"id": "1003", "title": "Steve.Jobs", "firstname": "Tom", "lastname": "Wang", "pubdate": "2014-4-2"})
add_book({"id": "1004", "title": "Harry Potter", "firstname": "Peter", "lastname": "Chen", "pubdate": "2013-10-2"})


f = file("book.xml", "w")
doc.writexml(f)
f.close()