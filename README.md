![artificial-intelligence-new-technology-science-futuristic-abstract-human-brain-ai-technology-cpu-central-processor-unit-chipset-big-data-machine-learning-cyber-mind-domination-generative-ai-scaled-1-1500x1000](https://github.com/user-attachments/assets/a49ff94a-d171-44e7-be2c-dc225dea9cb3)
# Cybersecurity Job Scraper

This repository contains a Python-based tool for scraping cybersecurity-related job listings using the JSearch API. The tool searches for jobs based on predefined keywords related to cybersecurity and saves the results into a CSV file. It is designed to help users find jobs based on specific search criteria, such as location, required skills, and experience level.

## Features

- **Keyword-based Job Search**: Searches for jobs using predefined cybersecurity-related keywords.
- **API Integration**: Utilizes the [JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) to retrieve job data.
- **CSV Export**: Saves the job results into a CSV file for easy data manipulation and sharing.
- **Random Delays**: Implements random delays between API requests to avoid potential rate-limiting or blocking.
- **Experience Filtering**: Filters jobs based on the required experience level (e.g., jobs requiring less than or equal to 24 months of experience).

## Predefined Keywords

The tool searches for jobs using the following keywords:

- Network Security
- Penetration Testing
- Incident Response
- Threat Intelligence
- Vulnerability Assessment
- Malware Analysis
- Risk Management
- Security Operations
- Encryption
- Identity and Access Management
- Security Information and Event Management (SIEM)
- Firewall Management
- Cybersecurity Compliance
- Cloud Security
- Data Loss Prevention

## Requirements

- Python 3.x
- [fake_useragent](https://pypi.org/project/fake-useragent/) (to rotate user-agent strings)
- [http.client](https://docs.python.org/3/library/http.client.html) (for making HTTP requests)
- [json](https://docs.python.org/3/library/json.html) (to handle JSON responses)
- [csv](https://docs.python.org/3/library/csv.html) (to write job data to CSV files)
- [time](https://docs.python.org/3/library/time.html) (to handle random delays)
- [random](https://docs.python.org/3/library/random.html) (to generate random delay intervals)

To install the required dependencies, run:

```bash
pip install fake_useragent

