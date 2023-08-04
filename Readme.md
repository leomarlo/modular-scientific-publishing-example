# Modular Structure for the paper "Political Power Networks"

This project contains a modular structure for creating scientific papers, running simulations, and generating presentations. The structure is intended to provide an organized and efficient way to manage different aspects of a scientific project.

## Getting Started

### Prerequisites

- Python3: This project requires Python3 to run. If Python3 is not installed, please install it before proceeding.
- pdflatex: This is required to generate PDF files from LaTeX sources.
- bibtex: This is used for bibliography management in LaTeX documents.

### Setup

Run the `setup.sh` script in your terminal (you might have to *chmod u+x setup.sh* before). The script will check if Python3 is installed and will exit if it is not. The script will also set up the necessary virtual environments and dependencies for running simulations, generating papers, and creating presentations.

Use the following command to run the script:

```bash
$ ./setup.sh
```

The script accepts the following optional flags:

- _--clear_: Removes existing virtual environments in the simulation, paper, and presentations folders.
- _--simulation_: Runs a simulation, generates a PDF, and informs you when the PDF has been generated.
- _--paper_: Generates a paper.
- _--presentation_: Prepares for a presentation.


For example, to remove existing virtual environments, run a simulation and create the paper use:

```bash
$ ./setup.sh --clear --simulation --paper
```

## Contributions
Contributions are welcome. Please feel free to send a pull request or create an issue if you have any questions, find bugs, or suggest enhancements.

## License
This project is licensed under a Creative Commons Attribution 4.0 International License.

## Contact
For any inquiries, please email me at leonhard.horstmeyer@gmail.com.