# Improper Neutralization of Special Elements used in an SQL Command

This lab shows how to easy gain access to the database. If attacker found this vulnerability he may read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file presented on the DBMS file system and in some cases issue commands to the operating system.

## Core idea
You don't have any account. You have to takeover the flag stored in password column in database.
