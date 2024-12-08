import requests as r
class Fetcher:
    def __init__(self):
        L = r.get("https://cdn.ituring.ir/ex/users.json")
        self.student = r
        sum_score = 0
    def nurds(self):
        for i in self.students:
            if i["score"] > 18.5:
                return {i["name"], i["last_name"]}
    def mean(self):
        for i in self.students:
            sum_score += i["score"] 
        return(sum_score/ len(self.students))
    def get_student(self):
     	for i in self.students:
 	        if i["city","state","location"]==0:
 	            return [{i["nsme"],i["last_name"]}]
    def sultans(self):
        for i in self.students:                   
 	           max_score==max (i ["score"])
        return tuple((i["name"],i["last_name"]))
 	