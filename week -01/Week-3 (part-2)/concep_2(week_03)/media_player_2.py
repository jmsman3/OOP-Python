from abc import ABC , abstractmethod 
class Description:
    def __init__(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
class Media(ABC):
    def __init__(self, title , duration):
        self.title = title
        self.duration = duration
    
    @abstractmethod
    def play(self):
        pass 

class Music(Media , Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title , duration)
        Description.__init__(self,description)
    
    def play(self):
        print(f"Playing Music : {self.title}")
    
    def info(self):
        print(f"Titel: {self.title} Duration: {self.duration} Description:{self.get_description()}")
class Video(Media , Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title , duration)
        Description.__init__(self,description)
    
    def play(self):
        print(f"Playing Video : {self.title}")
    
    def info(self):
        print(f"Titel: {self.title} Duration: {self.duration} Description:{self.get_description()}")
class AudioBook(Media , Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title , duration)
        Description.__init__(self, description)
    
    def play(self):
        print(f"Playing AudioBook : {self.title}")
    
    def info(self):
        print(f"Titel: {self.title} Duration: {self.duration} Description:{self.get_description()}")

class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}
        self.__genre = ""

    def get_media_items(self):
        return self.__media_items
    def get_media_by_genre(self):
        return self.__media_by_genre
    
    def add_media(self, media):
        if isinstance(media , Music):
            self.__genre = "Music"
        if isinstance(media , Video):
            self.__genre = "Video"
        if isinstance(media , AudioBook):
            self.__genre = "AudioBook"
        
        self.__media_items.append(media)

        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)
        else :
            self.__media_by_genre[self.__genre] = [media, ]

class User(ABC):
    def __init__(self, name):
        self.name = name 
    
    @abstractmethod 
    def play_media(self):
        pass 
class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)

    def play_media(self, library):
        for media in library.get_media_items():
            media.play()

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre= ""
    
    def set_favourite_genre(self, genre): #ekta genre user er kach theke nelam r ki
        self.__favourite_genre = genre
    
    def get_favourite_gener(self):
        return self.__favourite_genre
    
    def play_media(self, library):
        if self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.play()
        else:
            print("Invalid Genre Selected")
        
        print(library.get_media_by_genre())


library = Library()
music1 = Music("Music1","3.33" , "Autor: Phitron")
music2 = Music("Music1","3.33" , "Autor: Phitron")
video = Video("Video track 1" , "45.44" , "Artist: Omuk-tomuk")
audio1 = AudioBook("AduioBook1" , "34.22" , "Author: Programming-Hero")

library.add_media(music1)
library.add_media(music2)
library.add_media(video)
library.add_media(audio1)

free_user = FreeUser("Mahmud")
premium_user = PremiumUser("Sakib")
premium_user.set_favourite_genre("Video")

# free_user.play_media(library)
premium_user.play_media(library)
# print(isinstance(video , Video))
