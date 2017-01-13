# resume-customizer

They say to write sample projects that solve a problem the coder has.  My 
problem is that I'm looking for something more stable than freelancing.  So 
I've uploaded my resume, as well as the script I use to customize it for each 
employer. 

The first three arguments are the 
 - listed position
 - name of the company
 - the location of the position/company

Sample usage:
./resume_customizer.py "software engineer" Google "Kirkland, WA"

The fourth, optional argument is a list of terms to be added invisibly in the  
footer so any automated resume scanner will pass it on to a human HR with 
better decision making abilities

Sample usage:
./resume_customizer.py "software engineer" Google "Kirkland, WA" "html java css"

