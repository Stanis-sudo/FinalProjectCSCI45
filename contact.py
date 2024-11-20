class Contact:
    def __init__(self, firstName: str, phoneNumber: str, middleName: str = None, lastName: str = None, emailAddress: str = None):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        if (not middleName and not lastName):
            self.fullName = firstName
        elif (not middleName):
            self.fullName = firstName + " " + lastName
        elif (not lastName):
            self.fullName = firstName + " " + middleName
        else:
            self.fullName = firstName + " " + middleName + " " + lastName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

    def __str__(self):
        contactInfo = "First Name: " + self.firstName + "\n"
        if self.middleName:
            contactInfo += "Middle Name: " + self.middleName + "\n"
        if self.lastName:
            contactInfo += "Last Name: " + self.lastName + "\n"
        contactInfo += "Phone Number: " + self.phoneNumber + "\n"
        if self.emailAddress:
            contactInfo += "Email: " + self.emailAddress + "\n"
        return contactInfo