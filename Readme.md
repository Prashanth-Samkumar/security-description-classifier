# Project Structure
├── SDC.py # Interactive script to classify incidents
├── SDC_pipeline.pkl # Trained Sentence Transformer + classifier pipeline
├── security_incidents_dataset.csv # Dataset for training/testing
├── training_recipe... # Training notes/documentation
├── requirements.txt # List of dependencies
├── .gitignore # Git ignore rules
└── venv/ # Local virtual environment


# setup

## create the virtual environment
`
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
`

## install dependencies

`
pip install -r requirements.txt
`

## Run the interactive classifier

`
python SDC.py
`