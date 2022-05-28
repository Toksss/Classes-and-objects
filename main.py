class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.change_name = new_name
        print("The Students new name is " , new_name)

    def change_age(self, new_age):
        self.change_age = new_age
        print("The Students new age is " , new_age) 

    def add_track(self, new_track):
        self.change_track = new_track
        print("The Students new track is " , new_track)

    def get_score(self, new_score):
        self.get_score = new_score
        print("The Students new score is " , new_score)
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(34.5)
