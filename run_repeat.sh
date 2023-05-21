#!bin/bash

DIRNAMES=("obj_berry_2" "obj_cactus_2" "obj_broccoli_2" "obj_pear_2" "obj_cat_1" "obj_frog_1" "obj_croissant_1" "obj_mushroom_2" "obj_extinguisher_1" "obj_owl_1")

for i in {0..9}
do
    bash run.sh 3 ${DIRNAMES[i]}
done