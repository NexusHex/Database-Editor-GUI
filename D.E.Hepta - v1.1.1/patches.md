This sub-iteration of the Database Editor is a bugfix patch for an issue concerning the auto-updating Text widget that would show the contents of the database and the Scrollbar widget that allowed the user to scroll along the contents of the database.

**The auto-update feature has unfortuntely been removed** and has been replaced with a button, which allows the user to manually update the file. I apologize for the removal of this feature, since it made the life of the user a bit easier, but **Tkinter and SQLite3 seem to have issues with running a database and refreshing a Text/Scrollbar widget at the same time.**

I have also added some minor changes to the program in accordance with the removal of auto-update as well as other changes that came to mind:

Date created: 8/28/2023

Database Editor HeptaFunction comes with the following additions and changes:
>**Auto-update for the data_show Text widget has been removed and replaced with a Button widget** due to issues between modules for use of the Scrollbar. **Updating the Text widget will now be manual.**
>
>The title of the program is now in the same Frame widget as the version Label widget
>
>Special messageboxes will appear whenever data from the database is **added, deleted or cleared**. They will inform the user that they have to press the Button widget with *Update Database* on it for the changes to show in the Text box.
>
>When the program starts, any data from past executions of the program will remain - as they have in version 1.1 - but will now show *<UPDATE_FOR_NUM>*, since the OID (original ID) number is not available to SQLite3 until the database is updated within the main program. Simply follow what the text says, and press the Button saying *Update Databse*, and the number of the item will appear in suit.