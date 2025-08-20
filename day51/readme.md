# Seek() and tell() functions

In Python seek() and tell() functions are used to work with file objects and their position within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file like objects such as files, pipes and in- memory buffers.

# Seek()
-> The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position.

# tell()
-> The tell() function returns the current position within the file in bytes. This can be useful for keeping track of your location within the file or seeking  to a specific position relative to the current position.

# truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you  specify the mode as 'w' or 'a' the file is opened in write mode and you can write to the file. However if you want to truncate the file to a specific size, you can use the truncate function.