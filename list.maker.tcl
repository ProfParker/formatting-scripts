# Creates lists of experimental items following a latin square design
# Makes n balanced lists of experimental items, where n = number of conditions
# 
# Instructions:
# Input must have one sentence per line in the form: 
#	Item # Cond # word word word . . .
#	e.g. 10 1 This is a test sentence.
# 
# execute: wish list.maker.tcl
# Note: Items file must be in the same directory as this script
#
# Original Code by Brian Dillon


#########################   GUI   #########################
frame .f
label .f.l_file -text "Item file:"
label .f.conds -text "Number of conditions:"
entry .f.e_file -width 50 -textvariable ItemFile
entry .f.num_conds -width 10 -textvariable numConds
button .f.b_file -text "Browse" -command {set ItemFile [tk_getOpenFile]}

grid config .f.l_file -column 0 -row 0
grid config .f.e_file -column 1 -row 0
grid config .f.b_file -column 2 -row 0
grid config .f.conds -column 1 -row 2
grid config .f.num_conds -column 2 -row 2
grid columnconfigure .f 2 -minsize 100

button .f.b_ok -text "Start" -width 15 -command {main $ItemFile $numConds}

grid config .f.b_ok -column 0 -row 2

grid config .f -column 0 -row 0 -columnspan 4
############################################################


proc main {ItemFile numConds} {

for {set i 1} {$i <= $numConds} {incr i} {
	set items($i) Items::
	set output($i) [open list_$i.txt "RDWR CREAT"]
	set counter($i) $i
}

if {[file exists $ItemFile]} {
	set inFile [open $ItemFile "r"]						
	set Tabs 1		
		while {[gets $inFile line] != -1} {
			set line [string trim $line]
			if {[string length $line] > 0} {

				if {$Tabs == [expr $numConds+1]} {
					set Tabs 1
					foreach count [array names counter] {
						incr counter($count)
						if {$counter($count) == [expr $numConds+1]} {set counter($count) 1}
					}
				}
				set curCond [lindex $line 1]
				if {$curCond != $Tabs} {puts $output(1) "ERROR-Make sure that conditions are in the correct order in the original file-ERROR"}
				foreach count [array names counter] {
					if {$curCond == $counter($count)} {
						puts $output($count) $line
						flush $output($count)
						incr Tabs
					}
					
				}
			}
		}
}
}
					