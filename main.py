from db_manager import create_connection, create_table, add_book, search_books

def main():
    database = "bookstore.db"
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

    # Example usage:
    add_book(conn, "The Catcher in the Rye", "J.D. Salinger", 1951)
    add_book(conn, "To Kill a Mockingbird", "Harper Lee", 1960)

    books = search_books(conn, "The Catcher in the Rye")
    for book in books:
        print(book)

if __name__ == '__main__':
    main()
