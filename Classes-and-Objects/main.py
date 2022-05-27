class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name=str,age=int,tracks=str,score=float):
        self.name = name
        self.age=age
        self.tracks = tracks
        self.score = score
    def say_hi(self):
         print('Hello, my name is', self.name,self.age)
   
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob.say_hi()


class Student:
    def __init__(self,change_name=str,change_age=int,add_tracks=str,get_score=float):
        self.change_name = change_name
        self.change_age=change_age
        self.add_tracks =add_tracks
        self.score = get_score
    def change_me(self):
         print('Hello, my new name is', self.change_name )
   
Bob = Student(change_name="Peter", change_age=34, add_tracks=["UI/UX"],get_score=20.90)
Bob.change_me()
# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
