#python 3.7.1
def show_cat():
    cat = r'''
 /\_/\  
( o.o ) 
 > ^ < 
'''
    return cat

def main():
    print("Hello, reader! This is the first edition of my Python CV, in the moments of freedom I'm learning how to upgrade this cv. For now, press (p) to proceed")
    user_input = input()

    if user_input.lower() == 'p':
        
        
                # Pers. info
        full_name = "Aksels Skuburs"
        email = "aksels.skuburs@outlook.com"
        phone = "0629157367 "
        address = "Amsterdam"
        linkedin= "https://www.linkedin.com/mwlite/in/aksels-skuburs-1a1abb1a0"
        
        # Summary 
        summary = " Fueled by a relentless pursuit of knowledge, I embrace challenges with an unyielding spirit, transforming obstacles into opportunities for growth and learning. My journey has been a tapestry of diverse experiences, weaving together moments of triumph, resilience, and self-discovery. Currently looking for a flexible position (24h)  that can be combined with Msc Information Studies (Information Systems)  from September."
        
        # Education
        education_current= [
            {
                "WO_MSc": "Information Studies, Track - IS",
                "UNI": "University of Amsterdam",
                "LOC": "Amsterdam",
                "YEAR_GRAD": "exp.2024"
            }
        ]
        
        education_done= [
            {
                "WO_BA": "Media and Information",
                "UNI": "University of Amsterdam",
                "LOC": "Amsterdam",
                "YEAR_GRAD": "2019"
            }
        ]
        
        # Work Experience
        work_experience = [
            {
                "position": "Customer Success Manager",
                "company": "AppXite",
                "location": "Riga, Latvia",
                "duration": "4mths",
                "description": " Maintained and optimized external communication channels & learned basic project tracking and develooement skills in Devops" 
                               "Collaborated with cross-functional teams to deliver streamlined, achievable project timelines internal & external. Azure fundamentals, level az-900. "
            },
            {
                "position": "Junior AML",
                "company": "SEB",
                "location": "Riga, Latvia",
                "duration": "6mths",
                "description": "Assisted in developing and testing scenarios for alerts. Excel and Neo4j "
                               "Participated in alert reviews and contributed to team projects."
            },
            {
                "position": "Screening Operations",
                "company": "Adyen ",
                "location": "Amsterdam",
                "duration": "6mths",
                "description": "CDD, KYC"
              
            }
        ]
        
        # Skills
        skills = ["basic Python", "Git basics", "Azure('az-900')", "HTML&CSS read", "writing clear documentation of functionality, writing engaging manuals for end user"]
        
        # Generating the CV
        def generate_cv():
            cv = f"""
            {full_name}
            {email} | {phone} | {address}
            LinkedIn: {linkedin}
            
            Summary:
            {summary}

            Current Education:
            {education_current[0]['WO_MSc']} - {education_current[0]['UNI']} |
            {education_current[0]['LOC']} , {education_current[0]['YEAR_GRAD']}
            
            Finished Education:
            {education_done[0]['WO_BA']} - {education_done[0]['UNI']} | 
            {education_done[0]['LOC']} , {education_done[0]['YEAR_GRAD']}
            
            Work Experience:
            {work_experience[0]['position']} - {work_experience[0]['company']} | {work_experience[0]['location']} | {work_experience[0]['duration']}
            {work_experience[0]['description']}
            
            {work_experience[1]['position']} - {work_experience[1]['company']} | {work_experience[1]['location']} | {work_experience[1]['duration']}
            {work_experience[1]['description']}
            
            Skills:
            {", ".join(skills)}
            
              """
            return cv
        
    # Test the function
        print(generate_cv())
    else:
        cat = show_cat()
        print("You didn't press 'p'. Here's an ASCII cat for you:")
        print(cat)

if __name__ == "__main__":
    main()