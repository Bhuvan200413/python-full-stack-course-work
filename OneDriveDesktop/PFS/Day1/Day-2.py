# Day-2.py

def main():
    student = {
        "Student Name": "Kanukanti Bhuvan",
        "Student ID": "CGH2938",
        "Batch No": "PFS-HYD-050",
        "Email ID": "bhuvankanukanti2004@gmail.com",
        "Date of Birth": "2004-10-13",
        "Age": 21,
        "Gender": "Male",
        "Blood Group": "A+",
        "City": "Nizamabad",
        "State": "Telangana",
        "Student Phone Number": "+919392770983",
        "Parent Phone Number": "+919441060372",
        "Github Link": "https://github.com/Bhuvan200413",
    }

    academic = {
        "College Name": "Gitam University",
        "USN Number": "HU22CSEN0100270",
        "Qualification": "UG (Bachelor Degrees)",
        "Department": "B.Tech - Computer Science (CSE, Cybersecurity, AI & ML, IoT, Cloud Computing, Data Analytics, Data Science)",
        "Pass out Year": 2025,
        "Graduation Percentage": "72%",
        "Arrears": "No",
        "No of Arrears": 0,
        "10th Pass Year": 2020,
        "10th Percentage": "90.25%",
        "12th Pass Year": 2022,
        "12th Percentage": "86%",
        "Skills": "Python, Flask, HTML, CSS, Bootstrap, Javascript, MySQL",
    }

    print("=== Personal Information ===")
    for k, v in student.items():
        print(f"{k}: {v}")

    print("\n=== Academic Information ===")
    for k, v in academic.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()