class Mpesa_Account:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance

	def deposit(self,amount):
		
		self.balance=self.balance + amount
		print("Hi {} You have succesfully deposited {} in your account of phone_number. Your new M_pesa balance is Ksh{}.thank you.".format(self.name,amount,self.phone_number,self.balance));
		




	def withdraw(self,amount):
		if(amount<self.balance):
			self.balance=self.balance - amount
			print("Hi{} Your Withdrawal of cash {} of phone_number{} was sucessful. Your new balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance));

		else:
			print("You have insufficient funds");
		

		





	def check_balance(self):
		print("Hi {} Your current balance is {}. Thank you for using Mpesa.".format(self.name,self.balance));





