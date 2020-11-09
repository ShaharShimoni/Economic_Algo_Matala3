# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Agent:
    wants=[]
    def value(self,option:int):
        return self.wants[option]
def isParetoImprovement(agents:List[Agent], option1:int,option2:int)->bool:
    for x in agents:
        print(x.wants)
        if(x.value(option1)>x.value(option2)):
            return False
    return True

def isParetoOptimal(agents:List[Agent], option:int,allOptions:List[int])->bool:
    for j in allOptions:
        flag=True;
        for x in agents:
            if(x.value(option)>x.value(j)):
                flag=False
        if(flag==True):
            return True
    return flag

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    AgentAmi=Agent()
    AgentTmi =Agent()
    array=[10,10,40,40]
    AgentAmi.wants=array
    array1=[5,5,40,50]
    AgentTmi.wants=array1

    AgentList=[]
    AgentList.insert(0,AgentAmi);
    AgentList.insert(1,AgentTmi);
    print(isParetoImprovement(AgentList, 2, 1))
    #ques1

    # ques2
    AgentAmi = Agent()
    AgentTmi = Agent()
    AgentRmi = Agent()
    array1 = [1,2,3,4,5]
    AgentAmi.wants=array1
    array2 = [3,1,2,5,4]
    AgentTmi.wants=array2
    array3 = [3,5,5,1,1]
    AgentRmi.wants=array3
    AgentList2 = []
    AgentList2.insert(0, AgentAmi);
    AgentList2.insert(1, AgentTmi);
    AgentList2.insert(2, AgentRmi);
    list=[0,1,3,4]
    print(isParetoOptimal(AgentList2, 2, list))


    #print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
