#=====================Block - 1 ======================
from sys import *
import os


#Empty list of tokens
tokens = []
num_stack = []
symbols = {}	#Dictionary
#=====================End Block - 1 =================


#=====================Block - 2 =====================

#Definition of open_file function
def open_file(filename):
	data = open(filename,"r").read()
	data += "<EOF>"
	return data

#=====================End Block - 2=====================

#=====================Block - 3=========================

#Definition of lex function
def lex(filecontents):
	filecontents = list(filecontents)
	''' We are printing the file as list ... 
		It breaks every thing in the file into 
		a single character...
	'''
	#print(filecontents)
	tok = ""
	state = 0
	isexpr = 0
	varstarted = 0
	string = ""
	expr = ""
	var = ""
	n = ""
	for char in filecontents:
		tok += char

		if tok == " ":
			if varstarted == 1:
				tokens.append("VAR:" + var)
				var = ""
				varstarted = 0
			if state == 0:
				tok = ""
			else:
				tok = " "
		
		elif tok == "\n" or tok == "<EOF>":
			if expr != "" and isexpr == 1:
				"""
					Checking here is it expression or number.... and in the next elif also same is checking....
				"""
				tokens.append("EXPR:" + expr)
				#print(expr + "EXPR")
				expr = ""
				#ad
				isexpr = 0
			elif expr != "" and isexpr == 0:
				tokens.append("NUM:" + expr)
				#print(expr + "NUM")
				expr = ""
			elif var != "":
				tokens.append("VAR:" + var)
				var = ""
				varstarted = 0 
			tok = ""

		#LESSTHAN
		elif (tok == "<<" or tok == "LESSTHAN" or tok == "lessthan") and state == 0:
			if expr != "" and isexpr == 0:
				tokens.append("NUM:" + expr)
				expr = ""
			elif expr != "" and isexpr == 1:
				tokens.append("EXPR:" + expr)
				expr = ""
				isexpr = 0
			if var != "":
				tokens.append("VAR:" + var)
				var = ""
				varstarted = 0
			
			tokens.append("LESSTHAN")
			tok = "" 
		
		#GREATER THAN	
		elif (tok == ">>" or tok == "GREATERTHAN" or tok == "greaterthan") and state == 0:
			if expr != "" and isexpr == 0:
				tokens.append("NUM:" + expr)
				expr = ""
			elif expr != "" and isexpr == 1:
				tokens.append("EXPR:" + expr)
				expr = ""
				isexpr = 0
			if var != "":
				tokens.append("VAR:" + var)
				var = ""
				varstarted = 0
			
			tokens.append("GREATERTHAN")
			tok = "" 

		elif tok == "=" and state == 0:
			if expr != "" and isexpr == 0:
				tokens.append("NUM:" + expr)
				expr = ""
			if var != "":
				tokens.append("VAR:" + var)
				var = ""
				varstarted = 0 
			if tokens[-1] == "EQUALS":
				tokens[-1] = "EQEQ"
			else:
				tokens.append("EQUALS")
			tok = ""
		
		elif (tok == "STORE" or tok == "store") and state == 0:
			tokens.append("STORE")
			tok = ""

		elif tok == "$" and state == 0:
			varstarted = 1
			var += tok
			tok = ""
		
		elif varstarted == 1:
			
			if tok == "<" or tok == ">":
				
				if var != "":
					tokens.append("VAR:" + var)
					var = ""
					varstarted = 0
			
			var += tok
			tok = ""

		elif tok == "INPUT":# or tok == "input":	#Checking for INPUT statement
			tokens.append("INPUT")
			tok = ""
		
		elif (tok == "in") and state == 0:
			
				if expr != "" and isexpr == 0:
					tokens.append("NUM:" + expr)
					expr = ""
				tokens.append("IN")
				tok = ""
			

		elif tok == "PRINT" or tok == "print":	#Checking for PRINT statement
			tokens.append("PRINT")
			tok = ""
		
		elif tok == "ENDIF" or tok == "endif":	#Checking for ENDIF statement
			tokens.append("ENDIF")
			tok = ""

		elif tok == "ENDREPEAT" or tok == "endrepeat": #CHECKING FOR ENDREPEAT
			tokens.append("ENDREPEAT")
			tok = ""

		elif tok == "REPEAT" or tok == "repeat": #Checking for REPEAT
			tokens.append("REPEAT")
			tok = ""
		elif tok == "IF" or tok == "if":	#Checking for PRINT statement
			tokens.append("IF")
			tok = ""
		
		elif tok == "THEN" or tok == "then":	#Checking for PRINT statement
			if expr != "" and isexpr == 0:
				tokens.append("NUM:" + expr)
				expr = ""
			tokens.append("THEN")
			tok = ""
		

		elif tok == "0" or tok == "1" or  tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
			expr += tok
			tok = ""
		
		elif tok == "+" or tok == "-" or tok == "*" or tok == "/" or tok == "(" or tok == ")":
			isexpr = 1
			expr += tok
			tok = ""

		elif tok == "\t":
			tok = ""

		elif tok == "\"" or tok == " \"":
			if state == 0:
				state = 1
			elif state == 1:
				tokens.append("STRING:" + string + "\"")
				string = ""
				state = 0  
				tok = ""
		
		elif state == 1:
			string += tok
			tok = ""
	"""
		We can print all the tokens from this...
		print command
	"""
	#print(expr)
	#print(tokens)	
	#return ''
	return tokens	

#=====================End Block - 3======================

#================Block - 6================
def evalExpression(expr):
	"""
		This is another logic we are basically going
		to use the inbuilt function eval()
	expr = "," + expr
	i = len(expr) - 1
	num = ""

	while i>=0:
		if expr[i] == "+" or expr[i] == "-" or expr[i] == "*" or expr[i] == "/":
			num = num[::-1]
			num_stack.append(num)
			num_stack.append(expr[i])
			num = ""
		elif expr[i] == ",":
			num = num[::-1]
			num_stack.append(num)
			num = ""
		else:
			num += expr[i]
		i -= 1
	print(num_stack) 
	"""
	#We are using this inbuilt method to evaluate 
	#our expression
	return eval(expr)
#================End Block - 6 ================



#=====================Block - 5 ==================

def doPRINT(toPRINT):
	if toPRINT[0:6] == "STRING":
		toPRINT = toPRINT[8:]
		toPRINT = toPRINT[:-1]
	elif toPRINT[0:3] == "NUM":
		toPRINT = toPRINT[4:]
	elif toPRINT[0:4] == "EXPR":
		toPRINT = evalExpression(toPRINT[5:])
	print(toPRINT)

#====================End Block - 5 ==================


#======================Block - 7======================

def doASSIGN(varname,varvalue):
	"""
		This function takes two values 
		first is the : name of the variable
		and second is the value of the variable
		to be assigned
	"""
	symbols[varname[4:]] = varvalue

#======================End Block - 7==================

#=======================Block - 8 ===================
def getVARIABLE(varname):
	varname = varname[4:]
	if varname in symbols:
		#print("TRUE")
		return symbols[varname]
	else:
		return "VARIABLE ERROR: Undefined Variable"
		exit()

#=======================End Block - 8================

#======================Block - 9=====================
def getINPUT(string,varname):
	i = input(string[1:-1] + " ")
	symbols[varname] =  "STRING:\"" + i + "\""



#======================End Block - 9=====================

#NewAdd
def getVals(varname):
	if varname[0:6] == "STRING":
		varname = varname[7:]
		#varname = varname[:]
	elif varname[0:3] == "NUM":
		varname = varname[4:]
	elif varname[0:4] == "EXPR":
		varname = evalExpression(varname[5:])
	return varname

#=====================Block - 4 =====================

def parse(toks):
	"""	
		We can print the toks list from here
	""" 
	#print(toks)	
	i = 0
	while i<len(toks):
		if toks[i] == "ENDIF":
			#print("FOUND AN ENDIF")
			i+=1
		elif toks[i] == "ENDREPEAT":
			if toks[i-5][0:3] == "VAR" and toks[i-3][0:3] == "NUM":
				f = int(getVals(getVARIABLE(toks[i-5])))
				if f < int(toks[i-3][4:]):
					f += 1
					doASSIGN(toks[i-5],"NUM:"+str(f))
					i -= 6
				else:
					i+=1
			elif toks[i-5][0:3] == "VAR" and toks[i-3][0:3] == "VAR":
				f = int(getVals(getVARIABLE(toks[i-5])))
				if f < int(getVals(getVARIABLE(toks[i-3]))):
					f += 1
					doASSIGN(toks[i-5],"NUM:"+str(f))
					i -= 6
				else:
					i+=1
			

		elif toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR" or toks[i] + " " + toks[i+1][0:3] == "PRINT VAR":
			if toks[i+1][0:6] == "STRING":
				doPRINT(toks[i+1])
			elif toks[i+1][0:3] == "NUM":
				doPRINT(toks[i+1])
			elif toks[i+1][0:4] == "EXPR":
				doPRINT(toks[i+1])
			elif toks[i+1][0:3] == "VAR":
				doPRINT(getVARIABLE(toks[i+1]))
			i += 2

		


		elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM"  or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR"  or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
			#print(toks[i+2])
			"""
				Passing toks[i] : Variable name 
				toks[i+2] : Variable value to be 
				assigned...
			"""
			if toks[i+2][0:6] == "STRING":
				doASSIGN(toks[i],toks[i+2])
			elif toks[i+2][0:3] == "NUM":
				doASSIGN(toks[i],toks[i+2])
			elif toks[i+2][0:4] == "EXPR":
				doASSIGN(toks[i],"NUM:" + str(evalExpression(toks[i+2][5:])))
			#Used  for variable assignment
			elif toks[i+2][0:3] == "VAR":
				doASSIGN(toks[i],getVARIABLE(toks[i+2]))
			i += 3 
		#STORE
		elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "STORE NUM IN VAR" or toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:3] == "STORE STRING IN VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "STORE VAR IN VAR":
			if toks[i+1][0:6] == "STRING":#xppp
				doASSIGN(toks[i+3],toks[i+1])
			elif toks[i+1][0:3] == "NUM":
				doASSIGN(toks[i+3],toks[i+1])
			elif toks[i+1][0:4] == "EXPR":
				doASSIGN(toks[i+3],"NUM:" + str(evalExpression(toks[i+1][5:])))
			#Used  for variable assignment
			elif toks[i+1][0:3] == "VAR":
				doASSIGN(toks[i+3],getVARIABLE(toks[i+1]))
			i += 4

		elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "INPUT STRING VAR":
		# INPUT STRING:"" VAR:$VARIABLE
			getINPUT(toks[i+1][7:],toks[i+2][4:])
			i+=3

		elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM EQEQ NUM THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR EQEQ NUM THEN"  or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM EQEQ VAR THEN"  or  toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:6] + " " + toks[i+4]  == "IF STRING EQEQ STRING THEN"  or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:6] + " " + toks[i+4]  == "IF VAR EQEQ STRING THEN"  or  toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF STRING EQEQ VAR THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR EQEQ VAR THEN":
			#For NUM == NUM   (Both Needs to be NUMBER ot BOTH Needs to be string)
			if(toks[i+1][0:3] == "NUM" and toks[i+3][0:3] == "NUM") or (toks[i+1][0:6] == "STRING" and toks[i+3][0:6] == "STRING"):	
				if toks[i+1][7:] == toks[i+3][7:]:
					#print("TRUE")
					i+=5
				else:
					#print("FALSE")
					i+=7
				#i+=5 

			#FOR VAR == NUM    (Both Needs to be NUMBER)
			elif toks[i+1][0:3] == "VAR" and toks[i+3][0:3] == "NUM":	
				if getVals(getVARIABLE(toks[i+1])) == toks[i+3][4:]:
					i+=5
				else:
					i+=7

			#FOR VAR == STRING    (Both Needs to be STRING)
			elif toks[i+1][0:3] == "VAR" and toks[i+3][0:6] == "STRING":	
				if getVals(getVARIABLE(toks[i+1])) == toks[i+3][7:]:
					i+=5
				else:
					i+=7

			#FOR NUM == VAR    (Both Needs to be NUMBER)
			elif toks[i+1][0:3] == "NUM" and toks[i+3][0:3] == "VAR":
				if toks[i+1][4:] == getVals(getVARIABLE(toks[i+3])):
					i+=5
				else:
					i+=7

			#FOR STRING == VAR    (Both Needs to be STRING)
			elif toks[i+1][0:6] == "STRING" and toks[i+3][0:3] == "VAR":
				if toks[i+1][7:] == getVals(getVARIABLE(toks[i+3])):
					i+=5
				else:
					i+=7

			#FOR VAR == VAR 	  (BOTH NEEDS TO BE STRING AND VAR TOO OF SAME TYPE)
			elif toks[i+1][0:3] == "VAR" and toks[i+3][0:3] == "VAR":
				if getVals(getVARIABLE(toks[i+1])) == getVals(getVARIABLE(toks[i+3])):
					i+=5
				else:
					i+=7

		#Here Checking for Less than conditions : 
		elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM LESSTHAN NUM THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM GREATERTHAN NUM THEN"  or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR LESSTHAN NUM THEN"  or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM LESSTHAN VAR THEN"  or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR GREATERTHAN NUM THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF NUM GREATERTHAN VAR THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR GREATERTHAN VAR THEN" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4]  == "IF VAR LESSTHAN VAR THEN":
			#NUM LESS THAN NUM
			if toks[i+1][0:3] == "NUM" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "NUM":
				if int(toks[i+1][4:]) < int(toks[i+3][4:]):
					i+=5
				else:
					i+=7
			#NUM GREATER THAN NUM
			elif toks[i+1][0:3] == "NUM" and toks[i+2] == "GREATERTHAN" and toks[i+3][0:3] == "NUM":
				if int(toks[i+1][4:]) > int(toks[i+3][4:]):
					i+=5
				else:
					i+=7
			#VAR LESS THAN NUM
			elif toks[i+1][0:3] == "VAR" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "NUM":
				if int(getVals(getVARIABLE(toks[i+1]))) < int(toks[i+3][4:]):
					i+=5
				else:
					i+=7

			elif toks[i+1][0:3] == "VAR" and toks[i+2] == "GREATERTHAN" and toks[i+3][0:3] == "NUM":
				if int(getVals(getVARIABLE(toks[i+1]))) > int(toks[i+3][4:]):
					i+=5
				else:
					i+=7

			elif toks[i+1][0:3] == "NUM" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "VAR":
				if int(toks[i+1][4:]) < int(getVals(getVARIABLE(toks[i+3]))):
					i+=5
				else:
					i+=7
			
			elif toks[i+1][0:3] == "NUM" and toks[i+2] == "GREATERTHAN" and toks[i+3][0:3] == "VAR":
				if int(toks[i+1][4:]) > int(getVals(getVARIABLE(toks[i+3]))):
					i+=5
				else:
					i+=7

			elif toks[i+1][0:3] == "VAR" and toks[i+2] == "GREATERTHAN" and toks[i+3][0:3] == "VAR":
				if int(getVals(getVARIABLE(toks[i+1]))) > int(getVals(getVARIABLE(toks[i+3]))):
					i+=5
				else:
					i+=7

			elif toks[i+1][0:3] == "VAR" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "VAR":
				if int(getVals(getVARIABLE(toks[i+1]))) < int(getVals(getVARIABLE(toks[i+3]))):
					i+=5
				else:
					i+=7

		#repeat parser
		elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3]  == "REPEAT VAR LESSTHAN NUM" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3]  == "REPEAT NUM LESSTHAN NUM" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3]  == "REPEAT VAR LESSTHAN VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3]  == "REPEAT NUM LESSTHAN VAR":
			if toks[i+1][0:3] == "VAR" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "NUM":
				j = int(getVals(getVARIABLE(toks[i+1])))#xp1
				if j < int(toks[i+3][4:]):
					i+=4
				else:
					i+=6
			elif toks[i+1][0:3] == "VAR" and toks[i+2] == "LESSTHAN" and toks[i+3][0:3] == "VAR":
				j = int(getVals(getVARIABLE(toks[i+1])))#xp1
				if j < int(getVals(getVARIABLE(toks[i+3]))):
					i+=4
				else:
					i+=6
			


	#print(symbols)

#=====================End Block - 4 =====================



#=====================Block - 5 =======================

#Definition of run Function
def run():
	data = open_file(argv[1])
	'''
		We can Print the data of the file using
		this... 
	'''
	#print(data) 
	"""
		lex() Functions return list of all
		the tokens
	"""
	toks = lex(data)	#Calling lex function
	"""
		Parse function takes the list 'toks'
		returned by the lex function
	"""
	parse(toks)			#Calling parse function

#=====================End Block - 5=======================

def pysic_start_interpreter():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("#############################################################################\n\n")
	print("\t@@@@@@     @@       @@     @@@@@@@@   @@@@@@@@@@     @@@@@@@@    ")
	print("\t@@@@@@@     @@     @@      @@@@@@@      @@@@@@      @@@        ")
	print("\t@@    @@     @@   @@       @@             @@        @@")
	print("\t@@    @@      @@@@         @              @@        @@     ")
	print("\t@@@@@@         @@          @@@@@@@@       @@        @@ ")
	print("\t@@@@@          @@                @@       @@        @@ ")
	print("\t@@             @@               @@@       @@        @@ ")
	print("\t@@             @@           @@@@@@@     @@@@@@      @@@   ")
	print("\t@@             @@          @@@@@@@@   @@@@@@@@@@     @@@@@@@@       ")
	print("\n\t\t\t\t\t\t\t- A new to Code...")
	print("\n\n#############################################################################")



pysic_start_interpreter()

#Function that starts the program
run()
