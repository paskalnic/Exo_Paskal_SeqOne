# Project Name

This project is a script for analyzing genetic data.

## Features

- `exo paskal.py`: This script extracts reads from a BAM file based on certain criteria and counts :
● The number of variants present in the patient
● The average VAF of the patient's heterozygous variants. 
● The number of deletions in the file 
## Requirements

- Docker

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/paskalnic/Exo_Paskal_SeqOne.git
   ```

2. Docker build the project

   docker build -t {image_name} .

3. Docker run to run project

   docker run {image_name}
