
public class BookManagementSystem {

    // Book class
    public class Book {

        public String bookName;
        public String author;
        public Integer price;

        // Constructor
        public Book(String bookName, String author, Integer price) {

            this.bookName = bookName;
            this.author = author;
            this.price = price;
        }
    }

    // Method to display books
    public static void displayBooks() {

        // Create list of books
        List<Book> books = new List<Book>();

        // Add books
        books.add(new Book(
         
        
        
        
        
         'Python Basics', 'Rohit Sharma', 500));
        books.add(new Book(
         
        
        
        
        
         'Data Structures', 'Amit Verma', 650));
        books.add(new Book(
         
        
        
        
        
         'AI Fundamentals', 'Neha Patel', 700));

        // Display book details
        for (Book b : books) {

            System.debug( 
             'Book Name: ' + b.bookName
            );
            System.debug(
            'Author: ' + b.author
            );
            System.debug(
            'Price: ' + b.price
            );
            System.debug(


    
        


        


        


        


    '----------------------');
        }
    }
}
