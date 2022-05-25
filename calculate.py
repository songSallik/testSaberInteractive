import re


regex = "[a-zA-Zа-яА-ЯёЁ!@#$%^&()}{';\\|><~_=]"
errMsg = "Please enter an equation containing only numbers and operators without letters, emojis, double symbols, brackets, etc."

def calculate(expression):
    return eval(expression)

def check(sentence):
    operations = re.findall(regex, sentence)
    if len(operations)>0:
        return errMsg
    else:
         return "ok"

def runCalculate(sentence):
    try:
        checkStatus = check(sentence)
        if checkStatus=="ok":
            return calculate(sentence)
        else:
            return checkStatus
    except (ZeroDivisionError, ValueError)as er:
        return er
    
