# parking
Team 4: Parking Helpers
Members: Cate Baker, Jacquelyn Hendricks, Grace Bailey, Alex Tran

This is how to set up the project step by step:

1) Clone the repository with this command:

```git clone git@github.com:cs374/parking.git```

2) Now if you run the command 

```l```

You should see everything in your directory. If the first step went right, you should see "parking" in there.

3) Now you can type this command line to get into your repository: 

```cd parking```

-> Cool! Now you're in our repository! You should see all of our files there when you type ```l```

4) Ok, *I think* you will now have to set the environment variables, so that you don't have to type you psql password
everytime you do something with the database. Type the following commands:

```export PGHOST=data.cs.jmu.edu```
```export PGDATABASE=parking```
```export PGUSER=YOUR_JMU_EID```
```export PGPASSWORD=YOUR_PSQL_PASSWORD(SHOULD BE YOUR STUDENT #```

5) Now you will run the createtables.sql script using this command. It will create the tables that you can view in PGADMIN:

```psql parking < createtables.sql```

6) The tables are now created. You can view them in pgadmin, too. However, there's no data yet, but that's what the copy script is for. 
It imports data from the csv files into the tables.
First, make the copy.sh file executable with this command:

```chmod 755 copy.sh```
```ls -l copy.sh```

Now, run the copy.sh file with this command:

```./copy.sh```


