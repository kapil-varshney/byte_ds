

class CreditCard:

	def __init__(self, card_number):
  		self.card_number = card_number
  		self.card_type = self.determine_card_type()
  		self.valid = self.validate()

	
#Create and add your method called `determine_card_type` to the CreditCard class here:
	def determine_card_type(self):
		
		# Dictionary with keys as tuples of starting digits and values as the card types
		card_brand = {
			(4,) : 'VISA',
			(51, 52, 53, 54, 55): 'MASTERCARD',
			(34, 37) : 'AMEX',
			(6011,) : 'DISCOVER'
		}

		if (True in [int(self.card_number[0]) in k for k in card_brand]):
			card_type = ([card_brand[k] for k in card_brand if int(self.card_number[0]) in k])

		elif (True in [int(self.card_number[0:2]) in k for k in card_brand]):
			card_type = ([card_brand[k] for k in card_brand if int(self.card_number[0:2]) in k])

		elif (True in [int(self.card_number[0:4]) in k for k in card_brand]):
			card_type = ([card_brand[k] for k in card_brand if int(self.card_number[0:4]) in k])

		else:
			card_type = ['INVALID']

		return (card_type[0])


#Create and add your method called `check_length` to the CreditCard class here:
	def check_length(self):
		
		valid_length = {
			'VISA' : 16,
			'MASTERCARD' : 16,
			'DISCOVER' : 16,
			'AMEX' : 15
		}

		if (len(self.card_number) in (valid_length[k] for k in valid_length if k == self.card_type)):
			return (True)
		else:
			return (False)


#Create and add your method called 'validate' to the CreditCard class here:
	def validate(self):
		
		if (not self.check_length()):
			self.card_type = "INVALID"
			return False

		def digits_of(num):
			return [int(i) for i in str(num)]

		digits = digits_of(self.card_number)
		odd_digits= digits[-1::-2]
		even_digits = digits[-2::-2]
		total = sum(odd_digits)
		for digits in even_digits:
			total += sum(digits_of(digits*2))

		if ((total%10) == 0) :
			return True
		else :
			self.card_type = "INVALID"
			return False



#do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"

