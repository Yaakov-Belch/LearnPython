# What's the difference between Pandas groupby vs. SQL group by?

Let's take one step back and discuss the differences between Pandas and SQL.
Let'd take another step back and discuss the different goals of Pandas vs. SQL.

SQL is a *query* language: We have a data base and we just want
to get the answer to a question.  
Pandas is a programming language (an extension library of a 
programming language): We have data and want to process it.

Thus, what would be *one* complex SQL query is a combination of several simple
steps in Pandas.  In SQL, we cannot access the intermedate processing results.
In Pandas, we get them just like our final result --- ready to be used in other
computations (or to be discarded).  In Pandas, the intermediate results and the
final result is a data frame just like the input data.  By contrast, in SQL, the
input data is a data base tables --- and the output is just information outside 
of the data base.  In Pandas, data is referenced through python variables (with
python scoping rules) --- in SQL data bases, tables are stored like global 
variables.

Thus, in SQL, you would understand the `group by` feature as part of a larger
query.  In Pandas, it is an operation on its own.


