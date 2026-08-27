class User:
#hidden variable or private variable
    __password = 'Hello1234'

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username


    def getPassword(self):
        return self.__password

    def setPassword(self):
        old_password = input('Enter the old password')
        if old_password == self.__password:
            new_password = input('please enter your new password')
            self.__password = new_password 
        else:
            print('please enter the correct password')

#creating objects
aarin = User('david', 'hello.world@gmail.com', 'Aarin67')
print(aarin.name,'\n', aarin.username)
print(aarin.email)

#print(aarin.__password)it will show an error because its a private variable
#to acces the private variable
print(aarin.getPassword())
aarin.setPassword()
