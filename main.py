class Student:
         #constructor or init method
    def __init__(self,name, age,track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    #more methods
    def change_name(self, new_name):
        self.name = new_name
        print("The new name is ", new_name)
    def change_age(self, new_age):
        self.age = new_age
        print("The new age is ", new_age)
    def add_track(self, new_track):
        self.track = new_track
        print("The new track is ", new_track)
    def get_score(self, new_score):
        self.score = new_score
        print("The new score is ", new_score)

        #instantiation
Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

#Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(22)

