import pandas as pd

def show_cat():
    cat = r'''
 /\_/\  
( o.o ) 
 > ^ < 
'''
    return cat

def generate_cv():
    # Personal info
    full_name = "Aksels Skuburs"
    email = "aksels.skuburs@outlook.com"
    phone = "0629157367"
    address = "Amsterdam"
    linkedin = "https://www.linkedin.com/mwlite/in/aksels-skuburs-1a1abb1a0"

    # Summary
    summary = "Fueled by a relentless pursuit of knowledge, I embrace challenges with an unyielding spirit, transforming obstacles into opportunities for growth and learning. My journey has been a tapestry of diverse experiences, weaving together moments of triumph, resilience, and self-discovery. Currently looking for a flexible position (24h) that can be combined with Msc Information Studies (Information Systems) from September."

    # Education
    education_current = [
        {
            "Degree": "MSc in Information Studies",
            "Track": "Information Systems",
            "University": "University of Amsterdam",
            "Location": "Amsterdam",
            "Year of Graduation": "exp. 2024"
        }
    ]

    education_done = [
        {
            "Degree": "BA in Media and Information",
            "University": "University of Amsterdam",
            "Location": "Amsterdam",
            "Year of Graduation": "2019"
        }
    ]

    # Work Experience
    work_experience = [
        {
            "Position": "Customer Success Manager",
            "Company": "AppXite",
            "Location": "Riga, Latvia",
            "Duration": "4 months",
            "Description": "Maintained and optimized external communication channels, learned basic project tracking and development skills in DevOps, collaborated with cross-functional teams to deliver streamlined, achievable project timelines internal & external. Azure fundamentals, level az-900."
        },
        {
            "Position": "Junior AML",
            "Company": "SEB",
            "Location": "Riga, Latvia",
            "Duration": "6 months",
            "Description": "Assisted in developing and testing scenarios for alerts using Excel and Neo4j, participated in alert reviews, and contributed to team projects."
        },
        {
            "Position": "Screening Operations",
            "Company": "Adyen",
            "Location": "Amsterdam",
            "Duration": "6 months",
            "Description": "Handled CDD and KYC operations to ensure compliance."
        }
    ]

    # Skills
    skills = ["Basic Python", "Git Basics", "Azure (az-900)", "HTML & CSS (read)", "Writing clear documentation of functionality, writing engaging manuals for end users"]

    # Creating DataFrames using pandas
    education_current_df = pd.DataFrame(education_current)
    education_done_df = pd.DataFrame(education_done)
    work_experience_df = pd.DataFrame(work_experience)

    # Generating the CV
    cv = f"""
    {full_name}
    {email} | {phone} | {address}
    LinkedIn: {linkedin}

    Summary:
    {summary}

    Current Education:
    {education_current_df.to_string(index=False)}
    
    Finished Education:
    {education_done_df.to_string(index=False)}

    Work Experience:
    {work_experience_df.to_string(index=False)}
    
    Skills:
    {", ".join(skills)}
    """

    return cv

def main():
    print("Hello, reader! This is the first edition of my Python CV. In the moments of freedom, I'm learning how to upgrade this CV. For now, press (p) to proceed")
    user_input = input()

    if user_input.lower() == 'p':
        cv = generate_cv()
        print(cv)
    else:
        cat = show_cat()
        print("You didn't press 'p'. Here's an ASCII cat for you:")
        print(cat)

if __name__ == "__main__":
    main()
