## Introduction - QuickSQLConnector

- QuickSQLConnector directly establishes connection between python and mysqlserver. And gives you simple interface to execute mysql commands easily.

How to use?

- Use 'quicksqlconnector' keyword to import

```  from quicksqlconnector import quicksqlconnector```

### Creating instance of module

```DB = quicksqlconnector('host', port, 'username', 'password', 'database-name')```

- 'quicksqlconnector' only have one method which is 'query'

- Pass your 'mysql commnad' as a string in 'query' method to execute query.

 ```
 Some test commands shown below ->
 DB.query('update people set id=90 where id=1') 
 DB.query('delete from people where id=1000') 
 DB.query('delete from people where id=1022') 
 DB.query('insert into people value(26,4,6)') 
 DB.query('select * from people') 
 ```
    
### Bugs & Feedback

Github - https://github.com/Anas-Dew/QuickSQL)

