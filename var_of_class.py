# class inherit from built in class
class ContactList(list):
    'contactlist object that items are [name,nphone]'
    def search(self,name):
        name_list = []
        for item in self:
            if name in item.name:
                name_list.append(item.name)
            else:
                pass
        return name_list


#diffrence between var of class and var of instance(var can be mutable or immutable)   
class Contact():
    contact_list = ContactList()
    contact_num = 0

    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.contact_list.append(self)
        self.contact_num += 1
    
    def add(self,num):
        self.contact_num += num


if __name__=='__main__':
    s1 = Contact('john smith','01')
    s2 = Contact('john green','02')
    s3 = Contact('will smith','03')
    s1.add(2)
    s2.add(2)
    s3.add(3)
    print(id(Contact.contact_list),Contact.contact_list)
    print(id(s1.contact_list),s1.contact_list)
    print(id(s2.contact_list),s2.contact_list)
    print(id(s3.contact_list),s3.contact_list)
    print(id(Contact.contact_num),Contact.contact_num)
    print(id(s1.contact_num),s1.contact_num)
    print(id(s2.contact_num),s2.contact_num)
    print(id(s3.contact_num),s3.contact_num)
