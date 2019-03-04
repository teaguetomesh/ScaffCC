#!/bin/sh

# get QX Simulator
if [ ! -e scripts/qx_simulator_linux_x86_64/qx_simulator_1.0.beta_linux_x86_64 ]
then
    wget -nc -P scripts/ http://quantum-studio.net/qx_simulator_linux_x86_64.tar.gz
    tar -xvf scripts/qx_simulator_linux_x86_64.tar.gz -C ../
fi

./scaffold.sh -c $1
./scaffold.sh -s $1
source=${1##*/}
echo ${source%.scaffold}
scripts/qx_simulator_linux_x86_64/qx_simulator_1.0.beta_linux_x86_64 ${source%.scaffold}.qc > ${source%.scaffold}.global_phase.output
python scripts/simulation/remove_global_phase.py ${source%.scaffold}.global_phase.output ${source%.scaffold}.no_global_phase.output
#python remove_global_phase.py ${source%.scaffold}.global_phase.output ${source%.scaffold}.no_global_phase.output

