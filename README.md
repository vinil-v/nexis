# Nexis – Revolutionizing the Command Line with Smart AI Assistance

<img src="https://github.com/vinil-v/nexis/blob/main/images/nexis_updated_logo.png" >

## Description
Introducing **Nexis**: a fusion of "next" and "axis," representing the future of intelligent coding solutions. Nexis transforms the way developers and engineers interact with their systems through the command line interface. This advanced command-line interface (CLI) tool seamlessly integrates AI capabilities into the traditional CLI environment, revolutionizing troubleshooting, coding, and information retrieval for a smarter, more interactive, and efficient workflow.

### Challenges Faced by Engineers and Developers:

**Maintaining Focus:**
- Traditional web searches require opening multiple tabs and navigating through numerous documents, which is time-consuming and exhausting. This process leads to frustration and focus issues for engineers and developers.
- With Nexis, you don't have to leave the CLI. You can create scripts, search for information, or debug without switching interfaces, increasing focus and saving time.

**Information Overload:**
- When searching for topics, errors, or solutions, developers encounter an overwhelming amount of documents on the web. Finding the right information is crucial and should be readily accessible.
- Nexis addresses this by providing relevant information directly within the CLI, ensuring developers have immediate access to what they need.

**Efficient Information Retrieval:**
- In today's data-rich environment, extracting specific and relevant information can be extremely challenging.
- Nexis quickly delivers concise and pertinent information, streamlining the search process for engineers and developers.

**AI-Powered Troubleshooting, Search, and Coding:**
- Nexis, powered by Azure OpenAI GPT-4, acts as an assistant within your CLI. You can ask questions, search for information, debug issues, and write code without leaving the command line.
- Traditionally, the CLI was limited to basic bash completion and utilities, but Nexis revolutionizes it by integrating advanced AI capabilities directly into the CLI environment.

<img src="https://github.com/vinil-v/nexis/blob/main/images/nexis_demo.gif" >

## Pre-requisites
1. Python 3.8 or higher
2. Valid Azure Subscription
3. Azure OpenAI subscription
4. Tested on Ubuntu 20.04, Ubuntu 22.04 & AlmaLinux 8.7

## Setup Instructions

### 1. Create Azure OpenAI Service
Login to the [Azure Portal](https://portal.azure.com/) and create an Azure OpenAI service. 

<img src="https://github.com/vinil-v/nexis/blob/main/images/AzureOpenAIService.png" width="70%" height="70%">

Obtain the Keys and Endpoint from the resource management section. This information is needed to build Nexis.

<img src="https://github.com/vinil-v/nexis/blob/main/images/enpoints_api.png" width="50%" height="50%">

### 2. Configure `openai_config.json`
Create an `openai_config.json` file in your home directory with the obtained information:
```json
{
    "api_base": "https://nexisproject.openai.azure.com/",
    "api_version": "2023-03-15-preview",
    "api_key": "your-api-key",
    "deployment_name": "gpt-4"
}
```

### 3. Deploy Base Model in Azure AI Studio
Login to [Azure AI Studio](https://ai.azure.com/) and deploy a Base model for Nexis:
- Go to the deployment option.
- Select Deploy model → Select model → Select gpt-35-turbo and confirm.
- Update the deployment name in `openai_config.json` if necessary.

<img src="https://github.com/vinil-v/nexis/blob/main/images/model_deployment.png">


<img src="https://github.com/vinil-v/nexis/blob/main/images/model_deployment_final.png"  width="50%" height="50%">

### 4. Install Nexis
Clone the repository, change the directory, and set up Nexis:
```bash
git clone https://github.com/vinil-v/nexis.git
cd nexis/
sudo chmod +x setup_nexis.py
sudo ./setup_nexis.py
```
Note: In RHEL-based systems like AlmaLinux, ensure the shebang (`#!/usr/bin/env python3.8`) in both `nexis` and `setup_nexis.py` scripts points to Python 3.8. Additionally, run `pip3.8 install --user openai==0.28` if needed.

### 5. Run Nexis
Ensure the `openai_config.json` file is in the home directory. Run Nexis using the following command:
```bash
nexis
```

## Example Usage

### Help Command
```bash
vinil@vinilhackmachine2:~$ nexis -h
------------------------------------------------------------------------------------------------------------------------

WARNING: This response is generated by Nexis, a GPT-4 based model. Please verify the information provided and use it as a guideline. AI-generated responses may not always be fully accurate or complete.

------------------------------------------------------------------------------------------------------------------------

usage: nexis [-h] {ib,gpu,slurm,openpbs,mpi,scripts,logs,vmsku,error,others,linux,ai} query

Generate Nexis response using Azure OpenAI Service

positional arguments:
  {ib,gpu,slurm,openpbs,mpi,scripts,logs,vmsku,error,others,linux,ai}
                        Nexis response
  query                 The query to generate a response for

options:
  -h, --help            show this help message and exit
```

### Generate SLURM Job Script
```bash
vinil@vinilhackmachine2:~$ nexis slurm "create a job script for testing slurm job scheduling in 2 nodes"
------------------------------------------------------------------------------------------------------------------------

WARNING: This response is generated by Nexis, a GPT-4 based model. Please verify the information provided and use it as a guideline. AI-generated responses may not always be fully accurate or complete.

------------------------------------------------------------------------------------------------------------------------

Response:
Sure, here is a basic example of a Slurm job script that will run a job on 2 nodes. This script will execute a simple command, but you can replace it with your own code or script.

```bash
#!/bin/bash

#SBATCH --job-name=test_job      # Job name
#SBATCH --nodes=2               # Request two nodes
#SBATCH --ntasks-per-node=1     # Number of tasks per node
#SBATCH --time=00:05:00         # Expected run time (hh:mm:ss)
#SBATCH --output=test_job.out   # Name of the output file

module load slurm

# Print some information about the job to STDOUT
echo "Starting slurm job on $(hostname)"
echo "Running on $SLURM_NODELIST"

# Replace the following line with your own code
srun hostname
```

You can submit this job to Slurm with the `sbatch` command:

```bash
sbatch test_job.sh
```

This script will request two nodes, run a single task on each node, and limit the job's runtime to five minutes. It will print the hostname of the machine it's running on and the list of nodes allocated for the job. Finally, it will run the `hostname` command on each node using `srun`, which distributes the tasks among the allocated nodes.

```

### Generate Tensorflow MNIST Code

```bash
vinil@vinilhackmachine2:~$ nexis ai "create a mnist code using tensorflow"
------------------------------------------------------------------------------------------------------------------------

WARNING: This response is generated by Nexis, a GPT-4 based model. Please verify the information provided and use it as a guideline. AI-generated responses may not always be fully accurate or complete.

------------------------------------------------------------------------------------------------------------------------

Response:
Sure, here is a simple example of a code to create a MNIST classifier using TensorFlow. This example uses the tf.keras API, which is a high-level API to build and train models in TensorFlow.

```python
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Build the tf.keras.Sequential model by stacking layers
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# Choose an optimizer and loss function for training
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

# Train and evaluate the model
model.fit(train_images, train_labels, epochs=5)
model.evaluate(test_images,  test_labels, verbose=2)
```

This code will train a simple neural network on the MNIST dataset for 5 epochs. The model structure is quite simple, just a flatten layer to transform the 2D 28x28 pixel image to 1D 784 pixel, a dense layer with 128 neurons and 'relu' activation function, a dropout layer for regularization and a final dense layer with 10 neurons (as there are 10 classes in MNIST).

Please note that you may need to adjust the parameters like number of epochs, layers, neurons in the layer, etc. based on your specific use case to achieve the best performance.

### Check NVIDIA GPU Usage
```bash
vinil@vinilhackmachine2:~$ nexis gpu "how to check nvidia gpu usage via command line in linux"
------------------------------------------------------------------------------------------------------------------------

WARNING: This response is generated by Nexis, an GPT-4 based model. Please verify the information provided and use it as a guideline. AI-generated responses may not always be fully accurate or complete.

------------------------------------------------------------------------------------------------------------------------

Response:
You can check NVIDIA GPU usage via command line in Linux using the "nvidia-smi" command. This command provides information about the GPU utilization, memory usage, temperature, and more.

Here's the basic usage:

1. Open a terminal.
2. Type `nvidia-smi` and press Enter.

This will display a table with several columns including GPU name, memory usage, GPU utilization and more.

If you want to monitor your GPU usage in real-time, you can use the `watch` command in combination with `nvidia-smi`:

1. Open a terminal.
2. Type `watch -n 1 nvidia-smi` and press Enter.

This will refresh the `nvidia-smi` output every second, allowing you to monitor your GPU usage in real-time.

Remember, you need to have the NVIDIA drivers and the `nvidia-smi` tool installed on your system to use these commands.
```

Nexis simplifies troubleshooting, coding, and information retrieval by providing intelligent, AI-driven support directly through the command line. It is a valuable tool for HPC and AI engineers, streamlining their workflows and enhancing productivity.
 
