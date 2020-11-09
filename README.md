# Economic_Algo_Matala3

מטרת האלגוריתם היא לבדוק האם אפשרות מסויימת היא יעילה פארטו. ישנם כמה שחקנים הצריכים
לבחור באפשרות אחת מתוך כמה אפשרויות. כל שחקן מייחס ערך מסויים לכל אחת מהאפשרויות, לפי
המחלקה הבאה:
class Agent:
value(option:int)->float:
"""
 INPUT: the index of an option.
 OUTPUT: the value of the option to the agent.
"""
- 2 -

א. כיתבו אלגוריתם המקבל מערך של שחקנים ושתי אפשרויות )כל אפשרות מיוצגת ע"י מספר שלם(,
ובודק האם אפשרות 1 היא שיפור פארטו של אפשרות 2:
def isParetoImprovement(agents:List[Agent], option1:int,
option2:int)->bool:
ב. כיתבו אלגוריתם המקבל מערך של שחקנים, אפשרות, ומערך של כל האפשרויות, ובודק האם
האפשרות הנתונה יעילה פארטו:
def isParetoOptimal(agents:List[Agent], option:int,
allOptions:List[int])->bool:
