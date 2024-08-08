# Zach Alderete
# Pseudo Code for CRM platform
# CIS 129 Mod 13 Final Project
# Purpose of CRM program is to track contact information, create invoices, and track project timelines

# Define Contact class
Class Contact
    Properties: Name, Email, Phone
    Methods:
        SetName(Name)
        SetEmail(Email)
        SetPhone(Phone)

# Define Invoice class
Class Invoice
    Properties: Client, Project, Amount, Status
    Methods:
        SetClient(Client)
        SetProject(Project)
        SetAmount(Amount)
        SetStatus(Status)

# Define Project class
Class Project
    Properties: Client, ProjectName, StartDate, EndDate
    Methods:
        SetClient(Client)
        SetProjectName(ProjectName)
        SetStartDate(StartDate)
        SetEndDate(EndDate)

# Adding a New Contact
Function AddContact(Name, Email, Phone)
    Create a new Contact object
    Set Contact properties
    Add Contact to contacts list
    Return success statement

# Creating an Invoice
Function CreateInvoice(Client, Project, Amount)
    Create a new Invoice object
    Set Invoice properties
    Add Invoice to invoices list
    Return success statement

# Tracking a Project Timeline
Function AddProject(Client, ProjectName, StartDate, EndDate)
    Create a new Project object
    Set Project properties
    Add Project to projects list
    Return success statement

# Example of using loops
Function ListContacts()
    For each Contact in contacts list
        Print Contact details