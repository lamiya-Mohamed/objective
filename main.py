import matplotlib.pyplot as plt
class nizamu_ntaj:
    def __init__(self):
        self.list_organizations = []
        self.list_users = []
    def add_organizations(self,organization):
        self.list_organizations.append(organization)
    def add_users(self,user):
        self.list_users.append(user)
    def general_report(self):
        for organization in self.list_organizations:
            print(f"{organization.name}")
            print(f"{organization.organization_achievement_rate()}")
class Organization:
    def __init__(self,id,name,sector):
        self.id = id
        self.name = name
        self.sector = sector
        self.objectives_list =[]

    def add_objective(self,objective):
        self.objectives_list.append(objective)
    def organization_achievement_rate(self):
        if len(self.objectives_list) == 0:
          return 0
        total =0
        for objective in self.objectives_list:
            total+= objective.objective_achievement_rate()
        return total / len(self.objectives_list)
class Objective:
    def __init__(self,name,describation,owner,date_start,date_end,):
        self.name = name
        self.describation = describation
        self.owner = owner
        self.date_start = date_start
        self.date_end = date_end
        self.key_results = []
    def add_key_result(self,key_result):
        self.key_results.append(key_result)
    def objective_achievement_rate(self):
     if len(self.key_results) == 0:
          return  0
     weighted_total = 0
     total_weights = 0
     for key_result in self.key_results:
         weighted_total += key_result.percentage_achieving_result() * key_result.weighte
         total_weights += key_result.weighte
     if total_weights  == 0:
        return  0
     return weighted_total /  total_weights
class Key_Result:
    def __init__(self,name,target_value,current_value,weighte):
        self.name = name
        self.target_value = target_value
        self.current_value = current_value
        self.weighte = weighte
        self.tasks_list = []
    def add_tasks(self,task):
        self.tasks_list.append(task)
    def percentage_achieving_result(self):
      if self.target_value == 0:
          return 0
      return self.current_value / self.target_value * 100
class Task:
    def __init__(self,name,responsible,status,delivery_date):
        self.name = name
        self.responsible = responsible
        self.status = status
        self.delivery_date = delivery_date
    def is_complete(self):
      if self.status.lower() == "Completed":
          return True
      else:
          return False
class Control_panel:
    def data_preparation(self,organization):
        list_name= []
        list_lineages = []
        for objective in organization.objectives_list:
            list_name.append(objective.name)
            list_lineages.append(objective.objective_achievement_rate())
        return list_name ,list_lineages

    def display_indicators(self,organization):
        list_names,list_rates = self.data_preparation(organization)
        plt.bar(list_names,list_rates )
        plt.xlabel("الأهداف")
        plt.ylabel("نسبة التحقيق %")
        plt.title("نسب تحقيق الأهداف")
        plt.pie(list_rates)
        plt.hist(list_rates)
        plt.grid(True)
        plt.show()
class File_Manager:
    def Save_data(self,filename,organization):
        with open(filename,"w") as file:
         for organization in self.list_organizations:
           file.write(f"{organization.id,organization.name,organization.sector}")
         for objective in self.objectives_list:
           file.write(f"{objective.name,objective.describation,objective.owner,objective.date_start,objective.date_end}")
         for key_result in self.key_results:
           file.write(f"{key_result.name,key_result.weighte,key_result.current_value,key_result.target_value}")
         for task in self.tasks_list:
             file.write(f"{task.name,task.responsible,task.status,task.delivery_date}")

org1 = Organization(1, "البنك العربي الافريقي", "بنوك")
org2 = Organization(2, "البنك الاسلامي", "بنوك")
org3 = Organization(3, "بنك القاهرة", "بنوك")

obj1 = Objective("زيادة الأرباح", "زيادة ارباح البنك" ,"abdulrhaman",20/1/2025,30/1/2026)
obj1.add_key_result(Key_Result("KR1", 100, 70, 1))

obj2 = Objective( "تحسين خدمة العملاء" , "تحسين اراء العملاء عن البنك" ,"ahmed",20/1/2025,30/1/2026)
obj2.add_key_result(Key_Result("KR2", 100, 40, 1))
org1.add_objective(obj1)
org1.add_objective(obj2)
