# Text summarization using NLP

### Project plan

1 - Build project initialization setup using setuptools, os, and pathlib.

1.1 - Include logging feature.

2 - Build configuration class tools for different stages of deep learning design to have one source of truth.

3 - Build a model by importing data, building a dataset, network, training, evaluation, and prediction pipelines.

4 - Keep track of the project on GitHub and use GitHub action for CD/CI and deployment.

5 - Containerize the project using Docker.

6 - Deploy the model on AWS using S3, EC2, and possibly EKS service.

# Model

Pegasus transformer model from the hugging face project is used.
https://huggingface.co/docs/transformers/model_doc/pegasus

# SentencePiece

SentencePiece from the Hugging Face Transformers library, is an unsupervised text tokenizer and detokenizer mainly used for neural network-based text generation tasks. [sentencepiece] is an optional extra that can be added to the Transformers library for installation.

# rouge_score

The ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metric is a set of metrics used for the automatic evaluation of machine-generated text, especially in the context of text summarization and machine translation. The ROUGE metrics focus on comparing the overlap between the generated text and reference (human-written) text in terms of n-grams, word sequences, and other linguistic units.

Here are some key ROUGE metrics:

1. **ROUGE-N (unigram, bigram, trigram, etc.):**

Measures the overlap of n-grams (contiguous sequences of n words) between the generated text and the reference text.
ROUGE-1 considers unigrams, ROUGE-2 considers bigrams, and so on.

2. **ROUGE-L (Longest Common Subsequence):**

Measures the overlap in terms of the longest common subsequence (LCS) between the generated and reference texts. It considers word sequences that are common to both.

3. **ROUGE-W (Weighted Overlap):**

Similar to ROUGE-N but assigns different weights to different n-grams based on their lengths.

4. **ROUGE-S (Skip-bigram):**

Measures the overlap of skip-bigrams, which are pairs of words that are separated by a certain number of words in between.

5. **ROUGE-SU (Skip-bigram plus Unigram):**

Combines skip-bigram and unigram measures.

# BLEU score from Sacrebleu Library:

The BLEU (Bilingual Evaluation Understudy) score is a metric used to evaluate the quality of machine-generated translations by comparing them to one or more human-generated reference translations. It was proposed as a metric for the automatic evaluation of machine-translation output.

The BLEU score is based on the precision of the n-grams (contiguous sequences of n items, usually words) produced by the machine translation system. Here are the key components and concepts associated with the BLEU score:

1. **Precision of N-grams:**

   - BLEU measures the precision of the n-grams (typically unigrams, bigrams, trigrams, etc.) in the machine-generated translation compared to the reference translations.
   - Precision is calculated as the number of overlapping n-grams in the candidate translation that match the n-grams in the reference translations.

2. **Brevity Penalty:**

   - BLEU includes a brevity penalty to account for the fact that shorter translations tend to receive higher precision scores. Without this penalty, a very short translation could artificially inflate the BLEU score.
   - The brevity penalty penalizes translations that are shorter than the average length of the reference translations.

3. **Cumulative BLEU:**

   - BLEU is often calculated for different values of n (e.g., BLEU-1, BLEU-2, BLEU-3, BLEU-4), representing the precision of different orders of n-grams.
   - Cumulative BLEU scores consider the precision of n-grams up to a certain order, incorporating information from lower-order n-grams.

4. **Formula:**

   - The BLEU score is typically computed using the formula:

     ![BLEU Formula](<https://latex.codecogs.com/svg.latex?BLEU%20=%20BP%20\cdot%20\exp(\sum_{n=1}^N%20w_n%20\log(p_n))>)

     - \(BP\) is the brevity penalty.
     - \(N\) is the maximum order of n-grams considered.
     - \(w_n\) is the weight assigned to the precision of n-grams (commonly set to \(\frac{1}{N}\)).
     - \(p_n\) is the precision of n-grams.

5. **Interpretation:**
   - BLEU scores range from 0 to 1, with 1 indicating a perfect match between the machine-generated translation and the reference translations.
   - Higher BLEU scores generally indicate better translation quality, but the interpretation depends on the specific use case and language pair.

It's important to note that BLEU is just one of many metrics used to evaluate machine translation, and it has its limitations, such as sensitivity to word order and inability to capture semantic meaning comprehensively. Researchers often use a combination of metrics and conduct human evaluations for a more comprehensive assessment of translation quality.

# Workflow:

In order, each of these files needs to update when we add a new pipeline (stage):

1- Update config.yaml
2- Update params.yaml
3- Update src/config
4- update the component
5- update the pipeline
6- update main.py
7- update app.py

# Web app and REST API:

To handle concurrent requests, FastAPI alongside uvicorn is used.

- FastAPI is a modern, fast (high-performance), web framework for building APIs that works with python.
- "uvicorn" is used which is an ASGI (Asynchronous Server Gateway Interface) server implementation for Python web applications. ASGI is a specification for asynchronous web servers and frameworks that enables handling more concurrent connections with less resource usage compared to traditional synchronous web servers. To run async apps using uvicorn following command is used: "uvicorn myapp:app --host 0.0.0.0 --port 8080 --reload"

# Containerization process:

1. Build docker image
2. Push the Docker image to AWS ECR
3. Launch an EC2 instance in AWS
4. Pull the docker image from AWS ECR
5. Launch a container instance of the image in the EC2 instance

Setup commands for EC2:
sudo apt-get update
sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
sudo usermod -aG docker ubuntu (run Docker commands without needing to use 'sudo')
newgrp docker (This will create a new shell with the 'docker' group as the effective group for the duration of that shell session)



# CD/CI with GitHub actions:
GitHub actions are used to develop a CD/CI pipeline 

## **1. Event Trigger:**

This workflow is triggered on a push event to the main branch, excluding changes to the README.md file.

## **2. Permissions:**

Specifies GitHub App permissions for this workflow. It grants write access to the ID token and read access to the repository contents.

- **d-token: write permission**, means that the workflow run is allowed to generate and use identity tokens with write access. This is necessary for workflows that interact with GitHub Apps.

## **3. Jobs:**

The workflow contains three jobs: integration, delivery, and deployment.

### **3.1. Integration:**

- **runs-on:** This key specifies the type of runner (execution environment) that the job will use. In this case, it's set to ubuntu-latest, which means the job will run on the latest version of the Ubuntu operating system provided by GitHub Actions.

- **steps:** This is a list of individual tasks or steps that the job will execute sequentially.

- **Step 1 (checkout code):**

  - **uses:** Specifies an action that should be used for this step. In this case, it uses the actions/checkout@v3 action. The checkout action is commonly used to fetch the contents of the repository so that subsequent steps can operate on the code.

- **Step 2 (lint code):**
  Lint, or a linter, is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs. This is a placeholder and will be replaced by actual linting commands.

  - **run:** Defines a shell command that will be executed as part of this step. In this case, it's a simple echo command that outputs the text "Linting repository."

- **Step 3 (run unit tests):**
  - **run:** Defines a shell command for running unit tests. Similar to the previous step, it uses an echo command to output the text "Running unit tests." Again, this is a placeholder and will be replaced by actual commands needed to run unit tests.

Overall, this job checks out the code from the repository and then includes steps for linting the code and running unit tests. Note that the actual linting and testing commands are not provided yet.

### **3.2. Delivery:**

- **needs:** Specifies that this job depends on the completion of another job named "integration"..

- **Step 1 (checkout code):**

  - **uses:** Specifies the actions/checkout@v3 action. This step ensures that the latest code from the repository is available for subsequent actions.

- **Step 2 (install utilities):**

  - **run:** Defines a multi-line shell script. In this case, it updates the package list (apt-get update) and installs the jq and unzip utilities.

- **Step 3 (configure AWS credentials):**

  - **uses:** Specifies the aws-actions/configure-aws-credentials@v1 action, which is used to configure AWS credentials for subsequent AWS-related actions. The credentials are included in the subsequent **with**, extracted from environment variables using secrets.

- **Step 4 (login to Amazon ECR):**

  - **id:** Assigns an identifier to this step. This identifier (ECR-login) can be used later in the workflow to reference the outputs of this step.

- **Step 5 (push image to Amazon ECR):**

  - **env:** Defines environment variables used in this step.
  - **run:** Defines a multi-line shell script. This script builds a Docker image, tags it, and pushes it to Amazon ECR. The environment variables and outputs of the previous steps are used in this process.

Overall, this job is essentially handling the deployment process, building a Docker image, and pushing it to Amazon ECR as part of a continuous delivery workflow.

### **3.3. Deployment:**

- **runs-on:** Indicates that this job will run on a self-hosted runner, unlike the previous jobs that ran on GitHub-hosted runners.

- **Step 1 (configure AWS credentials):**

  - **uses:** Specifies the aws-actions/configure-aws-credentials@v1 action, which configures AWS credentials for subsequent AWS-related actions.

- **Step 2 (login to Amazon ECR):**

  - **id:** Assigns an identifier to this step. This identifier (ECR-login) can be used later in the workflow to reference the outputs of this step.

- **Step 3 (pull latest image):**

  - **run:** Defines a shell script that pulls the latest Docker image from Amazon ECR. The URL and repository name are obtained from the secrets.

- **Step 4 (run Docker image to serve users):**

  - **run:** Defines a shell script that runs a Docker container using the previously pulled image. The container is named "texts," and environment variables for AWS credentials and region are passed to the container.

- **Step 5 (Clean previous images and containers):**
  - **run:** Defines a shell script that cleans up previous Docker images and containers using docker system prune.

Overall, this job is responsible for deploying the Docker image obtained from Amazon ECR by pulling the latest version and running a container. The steps involve configuring AWS credentials, logging in to Amazon ECR, pulling the latest image, running the Docker container, and cleaning up previous Docker artifacts.

# Run Docker on EC2 instance on AWS:

After EC2 instance is running, run the following commands in the instance:

sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


mkdir actions-runner && cd actions-runner

curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

echo "29fc8cf2dab4c195bb147384e7e2c94cfd4d4022c793b346a6175435265aa278  actions-runner-linux-x64-2.311.0.tar.gz" | shasum -a 256 -c

tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

./config.sh --url https://github.com/samyarsworld/text-summarization-NLP --token AZEGQHVJD2B5APCYD3FWTGTFLBP2E

./run.sh