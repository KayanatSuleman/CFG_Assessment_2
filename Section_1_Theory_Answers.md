# <p style="text-align: center;">Foundation Assessment Theory</p>


### **1.1 What does SDLC stand for? [1 mark]**
>
> SDLC stands for Software Development Life Cycle 
>

### **1.2 What exception is thrown when you divide a number by 0? [1 mark]**
>
> Traceback (most recent call last):
  File "script.py", line 4, in <module>
    result = numerator / denominator
ZeroDivisionError: division by zero
>

### **1.3 What is the git command that moves code from the local repository to the remote repository? [1 mark]**
>
> The git command 'git push' transfers the code changes you made in the local repo to the remote repo on the git server. In this case it would be GitHub.
>

### **1.4 What does NULL represent in a database? [1 mark]**
>
> NULL represents = absense of a value, in a database.
>

### **1.5 Name two responsibilities of the Scrum Master? [2 mark]**
>
>a. One responsibility of the scrum master would to ensure that the Scrum Framework is adhered to and implemented correctly. The Scrum master is tasked to facilitate the the mandatory scrum events i.e. sprint - is completed within the given guidelines and time frames. 
>

>
>b. The scrum master is also responsible to ensure that all task impediments are removed, to allow a seamless working environment for the Scrum team to achieve the necessary tasks within the given time frame. This would mean working with the team to identity and resolve impedeiments. 
>

### **1.6 Name two debugging methods, and when you would use them? [4 mark]**
>
> Two debugging methods of Python
>

+ Print Statements: is a quick and effective way to help me identify if the code is working, especially when trying to see if a function does what you intend it to do. You can test a function by passing in hypothetical arguments to understand better how the code is operating. An example may be to use “print(can_pay(20.00, "50”))” at the end of your code to test your function.

+ Another way to debug within python would be to use the inbuilt debugging features within the IDE. This can be particularly useful when trying to understand any issues within the code. 

>
> Two debugging methods for SQL
>

+ We can print to get immediate results, to do this you would use the SELECT statement to display the results. An example of using this method could be  SELECT * FROM <_table name >. This would bring up all the table details within the database for ease of understanding what amount of information you are dealing with. This could be particularly useful when having to compare more than one table at a time. 

+ Another way to debug in SQL would be to use multiple joins or subqueries to pull information out of your database. This would be useful if there was a larger amount of information to deal with. This would be most useful when there are lots of tables, you could use multiple joins to combine information for it to be more meaningful and accurate. 

### **1.7 Looking at the following code, describe a case where this function would throw an error when called? [5 mark]**
>
>Please refer to the Section_1_Answer.py. file
>

### **1.8 What is git branching? Explain how it is used in Git [6 mark]**
>
>Git branching is a feature of Github that helps with version control, it lets developers work simultaneously within the same project. This process allows collaboration. The branching system also allows for develops to troubleshoot for bug fixes, without tempering with the main branch of the code. To use the branching system in Git you:
>

>
>a. Create a new branch within a repository. This is done by using the terminal, and the command  “git branch <branch_name>’ allows you to create a new branch. This creates an additional space of work within the same commit which is usually on you the main branch. 
>

>
>b. To then switch to and use the new branch that you’ve made; you use the terminal again and the command ‘git checkout <branch_name>. This allows you to switch your space of work onto the new branch as specified. “Git HEAD” allows an indication that you are working on that branch.
>

>
>c. To then make a change or a new commit you can then stage the code and commit the changes using the command in the terminal “git add” and then “git commit”. This allows you to apply the changes you were coding on, that specific branch, leaving the main branch unaffected.
>

>
>d. To merge changes after review, you can do that by first switching to back to the main branch using “git checkout main” and merge the changes from your branch using “git merge <bracnh_name>. This combines the changes that you made in the unique branch to the main branch. 
>

>
>e. You may need to delete a branch that has already been merged but is not needed anymore. To do this you use the command “git delete -d <branch_name>. This also can be done to keep the repo clean and organised 
>

>
>f. Finally to add the changes of your work to the remote repo, you use “git push”. This merges the changes of the code and updates your repo.
>

### **1.9 Design a restaurant ordering system [10 mark]**
>
>In the anticipation of designing a restaurant ordering system, these are the things that should be considered.
>

>
> a.  Key requirements: 
>
+ How the users would interact with the ordering system. The demographic of users would be staff and customers. So how would the system be easy to understand and use.

+ The next requirement would be how to update, upload, delete menu items, prices and descriptions onto the system for easy of understanding for both users, but primarily the staff who may be using the editing the system for menu changes and seasonal items. 

+ Then you would consider how the customer orders their food, what changes they might make to their order, in terms of add on and dietary requirements. The staff should also be able to make any changes easily to ensure good customer service and speed of transaction. 

+ the next requirement would be a costing system, how will the staff take the payment form the customer for the service. The system may need to be adaptable to new changes to technology i.e. Apple Pay, and versatile to accept different modes of payment.  

>
> b. Main considerations and problems:
>

+ Since this is an ordering system for a restaurant, the main aim of the business would be to satisfy their customers. The ordering system needs to be fast, and reliable. Offering easy of use to both the customers and staff members. 

+ The ordering system must also be able to handle multiple inputs from various end points, as there is likely going to be more than one staff member having an interaction with a customer about Their food, payment or dietary requirement. This needs to be managed by the ordering system with efficiency, easy and accurately. 

+ The ordering system would not be very useful if it can’t be changed to suit the restaurant. The need it to be customisable, and adaptable is mandatory. 

+ The orderings system must also be a safe way to hold, and process customer data, so the the ordering system does not cause any conflict with the law and meets all industry standards. 

>
> c. Components/tools:
>

+ To create this ordering systems front end, the use of HTML, CSS and Javascript would be useful. A way to create a user interface could be achieved with a framework like React 

+ The back-end development could be coded in Python, Ruby or Java with a framework like Django. 

+ To manage the database, mySQL could be used for data storage, and providing a way to retrieve the data.

+ We will need a way to process payments : s you could use Paypal to achieve this. 

+ We can integrate API to help with automation of certain tasks

+ And finally to create a secure environment and ensure secure login and data encryption we could use a tool such as OAuth.

done