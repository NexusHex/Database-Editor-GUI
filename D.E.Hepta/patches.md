This iteration of the Database Editor is a replica of the terminal-based Database Editor DecaFunction (https://github.com/NexusHex/Database-Editor-Series/tree/main/Editors/1.6.6%20-%20DecaFunction). Some functions have been cut off, since they involved saving the database in a list within the program, which doesnt happen anymore, so the function count has decreased to 7.

Date created: 8/27/2023

Database Editor HeptaFunction comes with the following additions and changes:
>The user can **remove specific values from the database file** by using a value's **OID (original ID)** number.
>
>You can now **export the database to a .csv file**, which can be viewed in apps like Excel
>
>The code now uses context managers for making connections to the .db file rather than manually committing and closing the database connection
>
>Frames have been added to most widgets in the program (QoL)
>
>When viewing the items within the database, the item comes with its **OID (original ID)** number to the side, for easy reference when you want to delete a value (QoL)
>
>The GUI of the app has had a visual overhaul to make way for the various widgets that have been added in this update (QoL)