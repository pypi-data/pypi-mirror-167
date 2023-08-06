# ManualSorter
A TUI application that reads lines from the clipboard, allows them to be manually reordered and then updates the clipboard.

# How to use
First, copy the text that you would like to reorder, for this example try copying the following list:
Bananas
Apples
Pears
Strawberries

Next, run the mansort.py script.

You will see at the top of the screen that the mode is set to READ and the first item of the list is selected. READ mode allows you to change which item is selected. Use either of the following key pairs to move the selection up/down: K/J or up/down arrow.

Move the selection until your favourite fruit is highlighted, then use any of the following keys to enable MOVE (edit) mode: F, L, right arrow. MOVE mode allows you to move the selected item. Use either of the following key pairs to move the selected item up/down: K/J or up/down arrow. As your favourite fruit is selected you will want to move it to the top.

Use any of the following keys to return to READ mode: D, H, left arrow, and repeat the process until the list is in the desired order.

Every time you change the order of the list your clipboard is updated, try pasting somewhere to confirm that the list is in the new order.

