import time
from datetime import datetime

class Quest:

    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.finish_time = None
        
    def __str__(self):
        return f"Название: {self.name}\nОписание: {self.description}\nЦель: {self.goal}"
    
    def accept_quest(self):
        if self.finish_time != None :
            print("С этим испытанием вы уже справились!")
            return
        self.start_time = datetime.now()
        print(f"Начало квеста \"{self.name}\" положено")

    def pass_quest(self):
        if self.start_time == None :
            print("Нельзя закончить то, что не начато!")
            return
        self.finish_time = datetime.now()
        completion_time = self.finish_time - self.start_time
        print(f"Квест завершён.\nВремя выполнения: {completion_time}")



new_quest = Quest( "Сокровища на Острове", \
                  "Нам была передена информация о наличии клада пиратов на осторове, находящийся по следующим координатам: *********", \
                    "Отыскать клад" )
print(new_quest)
new_quest.accept_quest()
time.sleep(5)
new_quest.pass_quest()