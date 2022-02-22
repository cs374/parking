# parking
Team 4: Parking Helpers
Members: Cate Baker, Jacquelyn Hendricks, Grace Bailey, Alex Tran

This is how to set up the project step by step:

1) Clone the repository with this command:

```git clone git@github.com:cs374/parking.git```

2) Now if you run the command ```l```, you should see everything in your directory. If the first step went right, you should see "parking" in there.

3) Now type: 

```cd parking```

-> Cool! Now you're in our repository! You should see all of our files there when you type ```l```

4) Now you will run the createtables.sql script using this command:

```psql -h data.cs.jmu.edu parking < createtables.sql```

5) The tables are now created. You can view them in pgadmin, too. However, there's no data yet, but that's what the copy script is for. 
First, make the copy.sh file executable with this command:

```chmod 755 copy.sh```
```ls -l copy.sh```

Now, run the copy.sh file with this command:

```./copy.sh```


