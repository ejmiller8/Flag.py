# Flag.py
Python script for listing all installed packages and their related use flags on a Gentoo system. This script is intended to be developed into a use flag manager.

This script uses "equery list *" to list all the packages a user has installed on their Gentoo system. Then, it parses the list into an array and loops through that array while using "equery uses" to associate each set of use flags with the package they correspond to. Then, all the matching packages and use flags are output to a text file.
