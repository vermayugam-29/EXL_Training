class Employee():
    def work(self):
        print("Employee work")

class Engineer(Employee):
    def design(self):
        print("Engineer work")

class Manager(Employee):
    def manage(self):
        print("Manager work")

class TechLead(Engineer, Manager):
    def lead(self):
        print("Leading the team")

lead = TechLead()
lead.work()
lead.design()
lead.manage()
lead.lead()