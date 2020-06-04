#!/usr/bin/env python
# coding: utf-8
Logger in python
----------------------
Logger :It is process of stroing /recording the complete information flow and exception into a file(log file)

Loggers in Python can be handled using Logging module
Basic level Loggers
----------------------
INFO,DEBUG,ERROR

1. INFO logger is used to store some important information like the control flow of program.
# In[ ]:


#ex-1
def func():
	try:
		print('func() is called')
		print('Connection 2 is established')
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except ZeroDivisionError:
		print('Please enter the non-zero Denominator')
	else:
		print(result)
	finally:
		print('Connection 2 is terminated')
		print('func() is terminated')

if __name__ == '__main__':
	print('main() is called')
	print('Connection 1 is established')
	func()
	print('Connection 1 is terminated')
	print('main() is terminated')
# o/p:
# ----
# main() is called
# Connection 1 is established
# func() is called
# Connection 2 is established
# Enter the Numerator:	10
# Enter the Denominator:	2
# 5.0
# Connection 2 is terminated
# func() is terminated
# Connection 1 is terminated
# main() is terminated

# NOTE:
# -----
# --> in the above example the control flow information is been displayed for the end user , this is not the 
# good programming approach , so we have to use INFO level logger to record the control flow information as shown below


# In[2]:


#practise
def funk():
    try:
        print("fun() is called")
        print("Connection2 is established")
        num1=int(input("Enter the num1:"))
        num2=int(input("Enter the num2:"))
        result=num1/num2
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        print("fun() is terminated")
        print("Connection2 is terminated")
if __name__=="__main__":
    print("Main() is called")
    print("connection1 is established")
    funk()
    print("Connection1 is terminated")


# In[3]:


#practise
import logging

logging.basicConfig(filename='one.txt',level=logging.INFO,filemode='w')

def funk():
    try:
        logging.info("fun() is called")
        logging.info("Connection2 is established")
        num1=int(input("Enter the num1:"))
        num2=int(input("Enter the num2:"))
        result=num1/num2
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        logging.info("fun() is terminated")
        logging.info("Connection2 is terminated")
if __name__=="__main__":
    logging.info("Main() is called")
    logging.info("connection1 is established")
    funk()
    logging.info("Connection1 is terminated")


# In[4]:


#ex-2
#python program to store the control flow information using INFO level logger
import logging

logging.basicConfig(filename='infolog2.txt',level=logging.INFO,filemode='w')
def func():
	try:
		logging.info('func() is called')
		logging.info('Connection 2 is established')
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except ZeroDivisionError:
		print('Please enter the non-zero Denominator')
	else:
		print(result)
	finally:
		logging.info('Connection 2 is terminated')
		logging.info('func() is terminated')

if __name__ == '__main__':
	logging.info('main() is called')
	logging.info('Connection 1 is established')
	func()
	logging.info('Connection 1 is terminated')
	logging.info('main() is terminated')

# o/p:
# -----
# Enter the Numerator:	10
# Enter the Denominator:	2
# 5.0


INFO:root:main() is called
INFO:root:Connection 1 is established
INFO:root:func() is called
INFO:root:Connection 2 is established
INFO:root:Connection 2 is terminated
INFO:root:func() is terminated
INFO:root:Connection 1 is terminated
INFO:root:main() is terminated

# In[5]:


#DEBUG LEVEL
# --->DEBUG level logger is used to store the information about input data enterd by the user.
# These things will for debuimport logging
logging.basicConfig(filename='errorlog7.txt',level=logging.ERROR)
def func():
	try:
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except Exception as e:
		print('Some program occurred')
		logging.exception(f'The cause of the Exception: {e}')
	else:
		print(result)
		
if __name__ == '__main__':
	
	func()

# o/p:
# -----
# Enter the Numerator:	10
# Enter the Denominator:	0
# Some program occurred
# -------------------------------------
# Enter the Numerator:	10
# Enter the Denominator:	sandesh
# Some program occurred
# -------------------------------------------------
# errorlog7.txt
# --------------
# ERROR:root:The cause of the Exception: division by zero
# Traceback (most recent call last):
#   File "ex7.py", line 9, in func
#     result=num1/num2
# ZeroDivisionError: division by zero
# ERROR:root:The cause of the Exception: invalid literal for int() with base 10: 'sandesh'
# Traceback (most recent call last):
#   File "ex7.py", line 7, in func
#     num2=int(input('Enter the Denominator:\t'))
# ValueError: invalid literal for int() with base 10: 'sandesh'


# In[6]:


#ex-3
def func():
	try:
		
		num1=int(input('Enter the Numerator:\t'))
		print('The value stored within the variable num1: ',num1)
		num2=int(input('Enter the Denominator:\t'))
		print('The value stored within the variable num2: ',num2)

		result=num1/num2

	except ZeroDivisionError:
		print('Please enter the non-zero Denominator')
	else:
		print(result)
		print('The value stored within the variable result: ',result)

if __name__ == '__main__':
	
	func()

# o/p:
# ------
# Enter the Numerator:	10
# The value stored within the variable num1:  10
# Enter the Denominator:	2
# The value stored within the variable num2:  2
# 5.0
# The value stored within the variable result:  5.0

# NOTE:
# -----
# -->In the above example the input entered by the user is displayed on the console , so inorder
# to overcome this disadvantage we have to use DEBUG level logger


# In[7]:


#ex-4
# python program using DEBUG level logger:
import logging

logging.basicConfig(filename='debuglog4.txt',level=logging.DEBUG,filemode='w')
def func():
	try:
		
		num1=int(input('Enter the Numerator:\t'))
		logging.debug(f'The value stored within the variable num1: {num1} ')
		num2=int(input('Enter the Denominator:\t'))
		logging.debug(f'The value stored within the variable num2: {num2} ')

		result=num1/num2

	except ZeroDivisionError:
		print('Please enter the non-zero Denominator')
	else:
		print(result)
		logging.debug(f'The value stored within the variable result: {result} ')

if __name__ == '__main__':
	
	func()

# o/p:
# ----
# Enter the Numerator:	10
# Enter the Denominator:	2
# 5.0
# ----------------------------------------------------------------------
# debuglog4.txt
# -------------
# DEBUG:root:The value stored within the variable num1: 10 
# DEBUG:root:The value stored within the variable num2: 2 
# DEBUG:root:The value stored within the variable result: 5.0 


# In[8]:


#ex-4
# python program using DEBUG level logger:
import logging

logging.basicConfig(filename='debuglog4.txt',level=logging.DEBUG,filemode='w')
def func():
	try:
		
		num1=int(input('Enter the Numerator:\t'))
		logging.debug(f'The value stored within the variable num1: {num1} ')
		num2=int(input('Enter the Denominator:\t'))
		logging.debug(f'The value stored within the variable num2: {num2} ')

		result=num1/num2

	except ZeroDivisionError:
		print('Please enter the non-zero Denominator')
	else:
		print(result)
		logging.debug(f'The value stored within the variable result: {result} ')

if __name__ == '__main__':
	
	func()

# o/p:
# ----
# Enter the Numerator:	10
# Enter the Denominator:	2
# 5.0
# ----------------------------------------------------------------------
# debuglog4.txt
# -------------
# DEBUG:root:The value stored within the variable num1: 10 
# DEBUG:root:The value stored within the variable num2: 2 
# DEBUG:root:The value stored within the variable result: 5.0 


# In[9]:


#ex-5
def func():
	try:
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except Exception as e:
		print('The cause of the Exception: ',e)
	else:
		print(result)
		
if __name__ == '__main__':
	
	func()

# o/p:
# ------
# Enter the Numerator:	10
# Enter the Denominator:	0
# The cause of the Exception:  division by zero
# --------------------------------------------------------------
# Enter the Numerator:	10
# Enter the Denominator:	sandesh
# The cause of the Exception:  invalid literal for int() with base 10: 'sandesh'
# ------------------------------------------------------------------------------

# NOTE:
# ------
# -->In the above example the complete exception information is displayed for the user , this is not the good 
# programming approach , so inorder to record the exception information we should make use of ERROR level
# loggers


# In[10]:


#ex-6
# python program using ERROR level logger:

import logging
logging.basicConfig(filename='errorlog6.txt',level=logging.ERROR)
def func():
	try:
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except Exception as e:
		print('Some program occurred')
		logging.error(f'The cause of the Exception: {e}')
	else:
		print(result)
		
if __name__ == '__main__':
	
	func()

# o/p:
# ------
# Enter the Numerator:	10
# Enter the Denominator:	0
# Some program occurred
# ---------------------------------------------
# Enter the Numerator:	10
# Enter the Denominator:	sandesh
# Some program occurred
# ---------------------------------------------
# errorlog6.txt
# -------------
# ERROR:root:The cause of the Exception: division by zero
# ERROR:root:The cause of the Exception: invalid literal for int() with base 10: 'sandesh'

# NOTE:
# -----
# -->In the above example using error() only we can fetch the cause of the exception, if
# we want to fetch the complete Exception history along with the cause then we should make use 
# of exception() as shown below


# In[11]:


#ex-7
import logging
logging.basicConfig(filename='errorlog7.txt',level=logging.ERROR)
def func():
	try:
		num1=int(input('Enter the Numerator:\t'))
		num2=int(input('Enter the Denominator:\t'))

		result=num1/num2

	except Exception as e:
		print('Some program occurred')
		logging.exception(f'The cause of the Exception: {e}')
	else:
		print(result)
		
if __name__ == '__main__':
	
	func()

# o/p:
# -----
# Enter the Numerator:	10
# Enter the Denominator:	0
# Some program occurred
# -------------------------------------
# Enter the Numerator:	10
# Enter the Denominator:	sandesh
# Some program occurred
# -------------------------------------------------
# errorlog7.txt
# --------------
# ERROR:root:The cause of the Exception: division by zero
# Traceback (most recent call last):
#   File "ex7.py", line 9, in func
#     result=num1/num2
# ZeroDivisionError: division by zero
# ERROR:root:The cause of the Exception: invalid literal for int() with base 10: 'sandesh'
# Traceback (most recent call last):
#   File "ex7.py", line 7, in func
#     num2=int(input('Enter the Denominator:\t'))
# ValueError: invalid literal for int() with base 10: 'sandesh'


# In[12]:


def exc():
    try:
        print("Entering to the exc()")
        print("Connection2 started")
        num1=int(input("Enter data1:"))
        num2=int(input("Entering the data2:"))
        result=num1/num2
        print(result)
    except Exception as e:
        print(e)
    finally:
        print("Connection2 terminated")
if __name__=='__main__':
    print("Entering to the main fun()")
    print("Connection1 started")
    exc()
    print('Connection1 terminated')
        


# In[13]:


import logging
logging.basicConfig(filename='two.txt',level=logging.ERROR)
def exc():
    try:
       
        num1=int(input("Enter data1:"))
        num2=int(input("Entering the data2:"))
        result=num1/num2
        print(result)
    except Exception as e:
        print("some problem occured")
        logging.error(e)
    
    
if __name__=='__main__':
    exc()
    


# # Differnent level of logger
# # ===============================

# In[14]:


from IPython.display import Image
Image("C:\\Users\\rock\\Desktop\\2\\level.PNG")


# In[15]:


#INFO
import logging
logging.basicConfig(filename="level.txt",level=logging.INFO)

    
    
if __name__=='__main__':
    print("Entering main()")
    logging.info("info Information ")
    logging.debug("debug information")
    logging.error("Error information")
    
    logging.exception("Exception information")
    logging.critical("Critical Information")
    logging.warning("warning Information")
    print("Existing main()")
 
# 0/p:level.txt

# INFO:root:info Information 
# ERROR:root:Error information
# ERROR:root:Exception information
# NoneType: None
# CRITICAL:root:Critical Information
# WARNING:root:warning Information


# In[16]:


import logging
logging.basicConfig(filename="lev.txt",level=logging.DEBUG)
if __name__=="__main__":
    print("Entring to the main()")
    
    logging.info("Info Information")
    logging.debug("Debig Information")
    logging.error("Error Information")
    logging.exception("Exception Information")
    logging.critical("Critical Information")
    logging.warning("Warning Information")
    print("Existing to the main()")


#   o/p:DEBUG
#   ===========
# INFO:root:Info Information
# DEBUG:root:Debig Information
# ERROR:root:Error Information
# ERROR:root:Exception Information
# NoneType: None
# CRITICAL:root:Critical Information
# WARNING:root:Warning Information


# In[17]:


import logging
logging.basicConfig(filename="level2.txt",level=logging.ERROR,filemode='w')

if __name__=="__main__":
	print("Entering to the main()")
	logging.info("Info Information ")
	logging.debug("DEBUG Information")
	logging.error("Error Information")
	logging.exception("Exception Information")
	logging.critical("Critical INformation")
	logging.warning("warning Information")
	print("Quiting from main")

#o/p:Error
#==============

# ERROR:root:Error Information
# ERROR:root:Exception Information
# NoneType: None
# CRITICAL:root:Critical INformation


# In[18]:


# Default logging level
# ============================
import logging
logging.basicConfig(filename='log3.txt',filemode='w')

if __name__=='__main__':
	print("info information")
	logging.info("info inforamtion")
	logging.debug("debug information")
	logging.error("error information")
	logging.exception("Exception information")
	logging.critical("critical information")
	logging.warning("warning information")
	
	print("exiting from main")

# 0/p
# ========
# ERROR:root:error information
# ERROR:root:Exception information
# NoneType: None
# CRITICAL:root:critical information
# WARNING:root:warning information

#Note
#---------------
#-->using DEBUG level we can store all the information
#-->default logging mode is append(a)
#-->default logging leval is Warning


# In[19]:


#===============
import logging
logging.basicConfig()

if __name__ == '__main__':
	
	print("Entring the main()")
	logging.info("ingo inforamtion")
	logging.debug("debug information")	
	logging.error("error information")
	logging.exception("exception information")
	logging.warning("warning ingoramtion")
	logging.critical("critical information")
	
	print("existing from main()")

# O/p
# =============
# Entring the main()
# ERROR:root:error information
# ERROR:root:exception information
# NoneType: None
# WARNING:root:warning ingoramtion
# existing from main()
# CRITICAL:root:critical information
# [Finished in 0.3s]

#NOTE
#------
#-->If we are not specifying file name then the messages will be printed
	# to the console.


# In[20]:


import logging
logging.basicConfig(filename="lev.txt",level=logging.DEBUG)
if __name__=="__main__":
    print("Entring to the main()")
    
    logging.info("Info Information")
    logging.debug("Debig Information")
    logging.error("Error Information")
    logging.exception("Exception Information")
    logging.critical("Critical Information")
    logging.warning("Warning Information")
    print("Existing to the main()")


# In[21]:


import logging
logging.basicConfig(filename='log11.txt',filemode='w',format='%(asctime)s %(levelname)s:%(message)s:%(funcName)s:',datefmt='%d%m%Y %I-%M-%S-%p')

if __name__=='__main__':
	print("Enteing the main()")
	logging.error("error information")
	logging.warning("Warning information")
	logging.critical("critical information")
	print("existing from main()")

#Formatting of log messages:
--------------------------------------------
By using format keyword argument,we can format messages.

1. To display only level name:
--------------------------------------
syntax:
-------------
	logging.basicConfig(format="%(levelname)s")

2>To display levelname and message:
--------------------------------------------------

syntax:
-------------
 	logging.basicConfig(format="%(levelname)s:%(message)s")

3.To display Timestamp in the log message:
------------------------------------------------------------
syntax:
--------------
 	logging.basicConfig(format="%(asctime)s":%(levelname)s:%(message)s')

4>To display functioname:%(funcName)s
5>To display filename: %(filename)s

WAP to store the information w.r.t WARNING level and store the data within a log
file by providing the data mtime,levelname,message, and functionname

import logging
logging.basicConfig(filename='log.txt',filemode='w',format='%(asctime)s %(levelname)s
:%(message)s:%(funcName)s:',datefmt='%d%m%Y %I-%M-%S-%p')

if __name__=='__main__':
	print("Enteing the main()")
	logging.error("error information")
	logging.warning("Warning information")
	logging.critical("critical information")
	print("existing from main()")

NOTE:
-------------
-->using datefmt() we can display the things a/c to user requirement
suntax:
------------
	datefmt="%d%m%Y %H:%M;%S"

%H-->24 hours time scale
%I-->12 hours time scale
%p-->PM or AM
%d-->date
%m-->month
%Y-->Year
%M-->minute
%S-->seconds

===========================
WAP to record the control flow information,user input data ,and exception logs/message into a log file.
1. To display only level name:
--------------------------------------
syntax:
-------------
	logging.basicConfig(format="%(levelname)s")
# In[22]:


import logging
logging.basicConfig(filename="san.txt",filemode='w',format="%(levelname)s")

if __name__=="__main__":
    print("Enteing the main()")
    logging.error("error information")
    logging.warning("Warning information")
    logging.critical("critical information")
    print("existing from main()")
    
    
# O/p--san.txt--
# ERROR
# WARNING
# CRITICAL

2>To display levelname and message:
--------------------------------------------------

syntax:
-------------
 	logging.basicConfig(format="%(levelname)s:%(message)s")

# In[23]:


import logging 
logging.basicConfig(filename="san1.txt",filemode="w",format="%(levelname)s :::: %(message)s")

if __name__=="__main__":
    print("Entering to the main()")
    logging.error("Error Information")
    logging.warning("Warning Information")
    logging.critical("Critical Information")
    logging.debug("Debug Information")
    logging.warning("Warning Information")
    print("Existing from main()")
    
# O/p  san1.txt
# ERROR :::: Error Information
# WARNING :::: Warning Information
# CRITICAL :::: Critical Information
# WARNING :::: Warning Information

3.To display Timestamp in the log message:
------------------------------------------------------------
syntax:
--------------
 	logging.basicConfig(format="%(asctime)s":%(levelname)s:%(message)s')

# In[24]:


import logging
logging.basicConfig(filename="san11.txt",filemode='w',format="%(asctime)s")

if __name__=="__main__":
    print("Entrering to the main()")
    logging.error("Error information")
    logging.debug("Debug information")
    logging.warning("warning Information")
    print("Existing to the main")


# O/p---san11.txt
# ==========
# 2020-06-04 12:49:49,357
# 2020-06-04 12:49:49,358

4>To display functioname:%(funcName)s


# In[25]:


import logging 
logging.basicConfig(filename="san1.txt",filemode="w",format="'The File present in' %(funcName)s")

if __name__=="__main__":
    print("Entering to the main()")
    logging.error("Error Information")
    logging.warning("Warning Information")
    logging.critical("Critical Information")
    logging.debug("Debug Information")
    logging.warning("Warning Information")
    print("Existing from main()")

5>To display filename: %(filename)s
# In[26]:


import logging 
logging.basicConfig(filename="san1.txt",filemode="w",format="'The File present in' %(filename)s datefmt='%d%m%Y %I-%M-%S-%p'")

if __name__=="__main__":
    print("Entering to the main()")
    logging.error("Error Information")
    logging.warning("Warning Information")
    logging.critical("Critical Information")
    logging.debug("Debug Information")
    logging.warning("Warning Information")
    print("Existing from main()")


# In[ ]:




