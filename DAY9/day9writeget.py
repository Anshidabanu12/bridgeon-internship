class HTTPerror(exception):
    def __init__(self, status_code):
        self.staus_code = self.staus_code
        super().__init__(f"HTTP error {self.staus_code}")


    def get_or_400(collection, id):
        if id in collection:
            return  collection[id]
        raise HTTPerror(404)
    

    #test
users ={
     1: {"name": "alice"},
     2: {"name": "jerry"},
     3:{"name": "zam"}
}

#test valid
try:
    user = get_or_404(users,2)
    print("found": user)
except HTTPerror as e:
    print(e)

try:
    user = get_or_404(users,2)
    print("found:"user)
except HTTPerror as e:
print(e)