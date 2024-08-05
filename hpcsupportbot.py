import openai
import argparse

# Set your Azure OpenAI Service endpoint, key, and deployment name
openai.api_type = "azure"
openai.api_base = "https://vinilhackproject.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "10e4b0dd49924450b87d56aab5e4fc58"
deployment_name = "gpt-35-turbo"  # Deployment name

def generate_hpc_utility_response(topic, query):
    prompt = f"Generate utilities for HPC diagnostics on the topic of {topic}:\nQuery: {query}\nResponse:"
    try:
        response = openai.Completion.create(
            engine=deployment_name,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    parser = argparse.ArgumentParser(description='Generate HPC diagnostic utilities using Azure OpenAI Service')
    parser.add_argument('topic', type=str, choices=['Infiniband', 'Nvidia GPU', 'AMD GPU', 'Slurm', 'OpenPBS', 'MPI', 'Job Scripts', 'Logs'],
                        help='The HPC topic to generate utilities for')
    parser.add_argument('query', type=str, help='The query to generate a response for')
    args = parser.parse_args()

    topic = args.topic
    query = args.query
    response = generate_hpc_utility_response(topic, query)
    print(f"Response:\n{response}")

if __name__ == "__main__":
    main()