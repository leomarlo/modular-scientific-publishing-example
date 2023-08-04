#! /bin/bash

# check if python3 is installed. If not issue a warning and exit, otherwise procede

if ! command -v python3 &> /dev/null
then
  echo "python3 could not be found"
  echo "Please install python3 and try again"
  exit
fi

args=("$@")
while (( "$#" )); do
  if [ "$1" == "--clear" ] ; then
    echo ">>> Removing .venv folders"
    rm -rf simulation/.venv
    rm -rf paper/.venv
    rm -rf presentations/.venv
    shift
  else
    shift
  fi
done



# check whether .venv folders exist in simulation folder
if [ -d "simulation/.venv" ] 
then
  echo ">>> Virtual Environment for the Simulation already exists"
    
else
  echo ">>> Virtual Environment for the Simulation does not exist"
  python3 -m venv simulation/.venv
  echo ">>> Virtual Environment for the Simulation has been created"
  source simulation/.venv/bin/activate
  # install dependences
  simulation/.venv/bin/pip3 install -r simulation/requirements.txt
  simulation/.venv/bin/python3 -m pip install --upgrade pip
fi

# check whether .venv folders exist in paper folder
if [ -d "paper/.venv" ] 
then
  echo ">>> Virtual Environment for the Paper already exists"
else
  echo ">>> Virtual Environment for the Paper does not exist"
  python3 -m venv paper/.venv
  echo ">>> Virtual Environment for the Paper has been created"
  source paper/.venv/bin/activate
  # install dependences
  paper/.venv/bin/pip3 install -r paper/requirements.txt
  paper/.venv/bin/python3 -m pip install --upgrade pip
fi

# create virtual environment for the presentation exists
if [ -d "presentations/.venv" ] 
then
  echo ">>> Virtual Environment for the Presentation already exists"
else
  echo ">>> Virtual Environment for the Presentation does not exist"
  python3 -m venv presentations/.venv
  echo ">>> Virtual Environment for the Presentation has been created"
  source presentations/.venv/bin/activate
  # install dependences
  presentations/.venv/bin/pip3 install -r presentations/requirements.txt
  presentations/.venv/bin/python3 -m pip install --upgrade pip
fi




for arg in "${args[@]}"; do
  if [ "$arg" == "--simulation" ]; then
    echo ">>> Running Simulation"
    simulation/.venv/bin/python3 simulation/main.py
  fi
  if [ "$arg" == "--paper" ]; then
    echo ">>> Generating Paper"
    paper/.venv/bin/python3 paper/generateMain.py
    # Generate the pdflatex
    ./scripts/compilePaper.sh
  fi
  if [ "$arg" == "--presentation" ]; then
      echo ">>> Generate Presentation"
      # presentations/.venv/bin/python3 presentations/main.py
  fi     
done

