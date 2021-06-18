class Terran:
    def __init__(self):
        print("생성자")
    
    def __del__(self):
        print("소멸자")
        
    def __str__(self):    
        return "babo"
            
print(Terran())