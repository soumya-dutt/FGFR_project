# This script is for calculation of NAMD Energy between ligand and individual protein residues in the binding site.

# Wrapping the whole complex 
pbc wrap -centersel "protein or resname WCJ" -center com -compound residue -all


# Alinging the frames
puts -nonewline " Aligning frames \n"

# Align all frames to the first frame
set numFrames [molinfo top get numframes]
set selFirstFrame [atomselect top "protein or resname WCJ" frame 0]
for {set i 1} {$i < $numFrames} {incr i} {
    set selCurrentFrame [atomselect top "protein or resname WCJ" frame $i]
    set transformation [measure fit $selCurrentFrame $selFirstFrame]
    $selCurrentFrame move $transformation
    puts " $i frame aligned"
    $selCurrentFrame delete
}
$selFirstFrame delete
puts -nonewline "Frames are aligned\n"


# Taking in initial atomselection
puts -nonewline "\n \t \t Selection1: "             ;# Make selection1 your ligand
gets stdin selection1
set sele1 [atomselect top $selection1]

puts -nonewline "\n \t \t Selection2: "             ;# Make selection2 your bindingsite 
gets stdin selection2                               ;# For example - same residue as (protein within 5 of resname name_name_of_ligand)
set sele2 [atomselect top $selection2]

# Listing all the unique residues 
set list1 [lsort -unique [$sele1 get resid]] 
puts "list of resids in selection1 : $list1"

set list2 [lsort -unique [$sele2 get resid]] 
puts " list of resid in selection2 : $list2"

# Getting NAMDEnergy
package require namdenergy

set parameter1 /home/sdutta46/Desktop/toppar/par_all36m_prot.prm
set parameter2 /home/sdutta46/Desktop/toppar/par_all36_carb.prm 
set parameter3 /home/sdutta46/Desktop/toppar/par_all36_lipid.prm 
set parameter4 /home/sdutta46/Desktop/toppar/par_all36_cgenff.prm 
set parameter5 /home/sdutta46/Desktop/toppar/par_all36_na.prm 
set parameter6 /home/sdutta46/Desktop/toppar/par_interface.prm 
set parameter7 /home/sdutta46/Desktop/toppar/toppar_water_ions_namd.str
set parameter8 wcj.prm                                                        ;# Don't forget to give the parameter for the ligand

foreach num1 $list1 {
    set res1 [atomselect top "resid $num1 and not water"]
       
    foreach num2 $list2 {
        
        set res2 [atomselect top "resid $num2 and not water"]
        namdenergy -vdw -elec -nonb -sel $res1 $res2 -par $parameter1 -par $parameter2 -par $parameter3 -par $parameter4 -par $parameter5 -par $parameter6 -par $parameter7 -par $parameter8 -ofile namdenergy_residue_${num1}_${num2}.dat -tempname temp_namdenergy

        
    }
  
}

puts "################################################## Finished ##################################################"











