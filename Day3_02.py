from abc import ABC, abstractmethod

class MediaItem(ABC):
    """
    Abstract base class for all media items.
    """
    def __init__(self, title, creator, item_id):
        self.title = title
        self.creator = creator
        self.item_id = item_id
        self.available = True 

    @abstractmethod
    def get_availability(self):
        """
        Abstract method to get availability status.
        """
        pass

    def check_out(self):
        """
        Checks out a media item.
        """
        if self.available:
            self.available = False
            print(f"{self.title} checked out.")
        else:
            print(f"{self.title} is not available.")

    def check_in(self):
        """
        Checks in a media item.
        """
        self.available = True
        print(f"{self.title} checked in.")

class PhysicalItem(MediaItem):
    """
    Class for physical media items.
    """
    def __init__(self, title, creator, item_id, location, condition):
        super().__init__(title, creator, item_id)
        self.location = location
        self.condition = condition

    def get_availability(self):
        """
        Returns availability status of a physical item.
        """
        return self.available

class DigitalItem(MediaItem):
    """
    Class for digital media items.
    """
    def __init__(self, title, creator, item_id, file_format, download_limit):
        super().__init__(title, creator, item_id)
        self.file_format = file_format
        self.download_limit = download_limit
        self.downloads_remaining = download_limit

    def get_availability(self):
        """
        Returns availability status of a digital item.
        """
        return self.downloads_remaining > 0

    def download(self):
        """
        Downloads a digital item.
        """
        if self.downloads_remaining > 0:
            self.downloads_remaining -= 1
            print(f"{self.title} downloaded successfully.")
        else:
            print(f"Download limit reached for {self.title}.")

class Book(PhysicalItem):
    """
    Class for physical books.
    """
    def __init__(self, title, author, item_id, location, condition, genre):
        super().__init__(title, author, item_id, location, condition)
        self.genre = genre

class EBook(DigitalItem):
    """
    Class for electronic books.
    """
    def __init__(self, title, author, item_id, file_format, download_limit, access_restrictions):
        super().__init__(title, author, item_id, file_format, download_limit)
        self.access_restrictions = access_restrictions

class AudioBook(DigitalItem):
    """
    Class for audiobooks.
    """
    def __init__(self, title, narrator, item_id, file_format, download_limit, duration):
        super().__init__(title, narrator, item_id, file_format, download_limit)
        self.duration = duration

class DVD(PhysicalItem):
    """
    Class for DVDs.
    """
    def __init__(self, title, director, item_id, location, condition, rating):
        super().__init__(title, director, item_id, location, condition)
        self.rating = rating

# Example Usage
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "B001", "Shelf A1", "Good", "Fantasy")
ebook1 = EBook("Pride and Prejudice", "Jane Austen", "E001", "EPUB", 3, "Faculty Only")
audiobook1 = AudioBook("The Hobbit", "Rob Inglis", "A001", "MP3", 1, "12 hours")
dvd1 = DVD("The Shawshank Redemption", "Frank Darabont", "D001", "Shelf B2", "Excellent", "R")

book1.check_out()
ebook1.download() 
audiobook1.check_out() 
dvd1.check_in()

print(book1.get_availability())
print(ebook1.get_availability()) 

