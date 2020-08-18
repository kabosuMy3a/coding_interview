from dataclasses import dataclass

@dataclass
class Interviewee :
	name : str
	sex : int 
	answer : str

	def __init__(self, name: str, sex: int, answer: str):
		self.name = name
		self.sex = sex
		self.answer = answer

	def to_string(self) -> str :
		return self.name+str(self.sex)+self.answer


sungyu = Interviewee("sungyu", 0, "Hi")
print(sungyu.to_string())

