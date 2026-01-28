import streamlit as st
import matplotlib.pyplot as plt
st.title("تشغيل نظام نتاج لإدارة الأهداف والنتائج الرئيسية")
st.write("تساعد هذه الداشبورد في تتبع أداء الأهداف عبر المؤسسات.")
class Organization:
    def __init__(self, id, name, sector):
        self.id = id
        self.name = name
        self.sector = sector
        self.objectives_list = []

    def add_objective(self, objective):
        self.objectives_list.append(objective)

    def organization_achievement_rate(self):
        if len(self.objectives_list) == 0:
            return 0
        total = 0
        for objective in self.objectives_list:
            total += objective.objective_achievement_rate()
        return total / len(self.objectives_list)
class Objective:
    def __init__(self, name):
        self.name = name
        self.key_results = []

    def add_key_result(self, key_result):
        self.key_results.append(key_result)
    def objective_achievement_rate(self):
        if len(self.key_results) == 0:
            return 0
        weighted_total = 0
        total_weights = 0
        for kr in self.key_results:
            weighted_total += kr.percentage_achieving_result() * kr.weighte
            total_weights += kr.weighte
        if total_weights == 0:
            return 0
        return weighted_total / total_weights
class Key_Result:
    def __init__(self, name, target_value, current_value, weighte):
        self.name = name
        self.target_value = target_value
        self.current_value = current_value
        self.weighte = weighte

    def percentage_achieving_result(self):
        if self.target_value == 0:
            return 0
        return (self.current_value / self.target_value) * 100


class Control_panel:
    def data_preparation(self, organization):
        names = []
        rates = []
        for obj in organization.objectives_list:
            names.append(obj.name)
            rates.append(obj.objective_achievement_rate())
        return names, rates

    def display_indicators(self, organization):
        names, rates = self.data_preparation(organization)
        fig, ax = plt.subplots()
        ax.bar(names, rates)
        ax.set_xlabel("الأهداف")
        ax.set_ylabel("نسبة التحقيق %")
        ax.set_title("نسب تحقيق الأهداف")
        st.pyplot(fig)
org1 = Organization(1, "البنك العربي الافريقي", "بنوك")
org2 = Organization(2, "البنك الاسلامي", "بنوك")
org3 = Organization(3, "بنك القاهرة", "بنوك")

obj1 = Objective("زيادة الأرباح")
obj1.add_key_result(Key_Result("KR1", 100, 70, 1))

obj2 = Objective("تحسين خدمة العملاء")
obj2.add_key_result(Key_Result("KR2", 100, 40, 1))

org1.add_objective(obj1)
org1.add_objective(obj2)

organizations = [org1, org2, org3]
selected_org = st.selectbox(
    "اختار المؤسسة",
    organizations,
    format_func=lambda org: org.name
)

st.write("المؤسسة المختارة:", selected_org.name)
if st.button("عرض الأداء"):
    panel = Control_panel()
    panel.display_indicators(selected_org)
