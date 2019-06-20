import subprocess as sp
import os

x = 0

# Create "InstalledPackages.txt" in the current working directory
os.mknod("InstalledPackages.txt")

# Store the output of equery list "*" (piped into tr to replace trailing line breaks with spaces)
# into "InstalledPackages.txt"
installedPackages = sp.getoutput('equery list "*" | tr \"\n\" \" \" > InstalledPackages.txt')

# "R"ead "InstalledPackages.txt" into the variable installedPkg
installedPkg = open("InstalledPackages.txt", "r")

# Parse the variable installedPkg by spaces into the variable installedPkgArray
installedPkgArray = installedPkg.read().split(' ')

# Create "SortedFlags.txt" in the current working directory to store the matched packages/flags
os.mknod("SortedFlags.txt")

# Loop through the array of packages while adding the associated flags
with open("SortedFlags.txt", "a") as sf:
     for x in range(len(installedPkgArray)):
         newLine = sp.getoutput('equery uses ' + installedPkgArray[x] + ' | tr \"\n\" \" \"')
         sf.write(installedPkgArray[x] + newLine + "\n")
     
installedPkg.close()
sf.close()
print ("Done!")
