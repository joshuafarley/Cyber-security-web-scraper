import http.client
import json
import time
import random
import csv
from fake_useragent import UserAgent

# New list with the provided combined keyword strings
cybersecurity_keywords = [
    "Network Security",
    "Penetration Testing",
    "Incident Response",
    "Threat Intelligence",
    "Vulnerability Assessment",
    "Malware Analysis",
    "Risk Management",
    "Security Operations",
    "Encryption",
    "Identity and Access Management",
    "Security Information and Event Management (SIEM)",
    "Firewall Management",
    "Cybersecurity Compliance",
    "Cloud Security",
    "Data Loss Prevention"
]

# Function to search for jobs using the JSearch API
def search_jobs(query, location, page=1, num_pages=1, date_posted='all'):
    # Set up the connection and request
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")

    # Replace these values with your own RapidAPI credentials
    headers = {
        'x-rapidapi-key': "Enter your own key",  # Enter your own RapidAPI key here
        'x-rapidapi-host': "jsearch.p.rapidapi.com"
    }

    # Construct the URL with query parameters
    request_url = f"/search?query={query.replace(' ', '%20')}&location={location}&page={page}&num_pages={num_pages}&date_posted={date_posted}"

    # Make the GET request
    conn.request("GET", request_url, headers=headers)

    # Get the response
    res = conn.getresponse()
    data = res.read()

    # Decode the response
    decoded_data = data.decode("utf-8")

    # Parse the JSON response
    job_results = json.loads(decoded_data)

    return job_results

# Function to scrape jobs using the combined keyword strings and save results to a CSV file
def scrape_jobs_to_csv(keywords_list, location="USA", extra_info=None, page=1, num_pages=1, csv_filename="cybersecurity_jobs.csv"):
    # Rotate user-agents to avoid getting blocked
    ua = UserAgent()

    # Open CSV file for writing
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Job Title', 'Company', 'Location', 'Posted Date', 'Apply Link', 'Skills Required', 'Responsibilities', 'Experience', 'Salary']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Iterate through the combined keyword strings and search for jobs
        for keywords in keywords_list:
            # Call the search_jobs function with the combined keyword query
            job_listings = search_jobs(query=keywords, location=location, page=page, num_pages=num_pages)

            # Check if job results exist
            if job_listings.get('data'):
                for job in job_listings['data']:
                    experience_info = job.get('job_required_experience', {})

                    # Handle missing or None values
                    required_experience_months = experience_info.get('required_experience_in_months', None)
                    if required_experience_months is not None:
                        required_experience_months = int(required_experience_months)
                    else:
                        required_experience_months = 0

                    # Extract salary information from the job listing
                    salary_min = job.get('job_min_salary', 'N/A')
                    salary_max = job.get('job_max_salary', 'N/A')
                    salary = f" {salary_min} - {salary_max}" if salary_min != 'N/A' and salary_max != 'N/A' else 'N/A'

                    # Extract job location details
                    job_city = job.get('job_city', 'N/A')
                    job_state = job.get('job_state', 'N/A')
                    job_country = job.get('job_country', 'N/A')

                    # Create a formatted location string
                    location_str = f"{job_city}, {job_state}, {job_country}"

                    # Filter jobs based on experience (less than or equal to 24 months)
                    if required_experience_months <= 24:
                        experience_required = experience_info.get('experience_mentioned', 'Not specified')

                        job_info = {
                            'Job Title': job.get('job_title', 'N/A'),
                            'Company': job.get('employer_name', 'N/A'),
                            'Location': location_str,
                            'Posted Date': job.get('job_posted_at_datetime_utc', 'N/A'),
                            'Apply Link': job.get('job_apply_link', 'N/A'),
                            'Skills Required': ', '.join(job.get('job_highlights', {}).get('Qualifications', ['Not specified'])),
                            'Responsibilities': ', '.join(job.get('job_highlights', {}).get('Responsibilities', ['Not specified'])),
                            'Experience': f"{required_experience_months} Not Specified" if experience_required == "true" else "Experience not mentioned",
                            'Salary': salary
                        }

                        # Write the job info to the CSV file
                        writer.writerow(job_info)

            # Introduce a random delay to mimic human browsing but suppress the message
            browse_delay = random.uniform(5, 15)
            time.sleep(browse_delay)

    print(f"Job data has been saved to {csv_filename}")


# Example usage
if __name__ == "__main__":
    # Iterate through the list of combined keyword strings and export data to CSV
    scrape_jobs_to_csv(cybersecurity_keywords, extra_info=["location"], page=1, num_pages=1)



