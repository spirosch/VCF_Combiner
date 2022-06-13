import os

with open('combinedFile.vcf', 'w') as VCF_Final:
    VCF_Final.write('Create a new text file!')
    all_files = "VCF_Files"
    list_of_files = os.listdir(all_files)
    for file_name in list_of_files:
        print(file_name)
        if file_name == ".DS_Store":
            continue
        contacts_file = open(f"VCF_Files/{file_name}", "r")
        readfile = contacts_file.readlines()

        for line in readfile:
            VCF_Final.write(line)
    print(VCF_Final)
