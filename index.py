import os

with open('combinedFile.vcf', 'w') as VCF_Final:
    VCF_Final.write('Create a new text file!')
    all_files = "VCF_Files"
    list_of_files = os.listdir(all_files)
    print(list_of_files)
    for file_name in list_of_files:
        if file_name == ".DS_Store":
            continue
        contacts_file = open(f"VCF_Files/{file_name}", "r")
        readfile = contacts_file.readlines()
        count = 0
        for line in readfile:

            count += 1

            VCF_Final.write(line)
    print(VCF_Final)

#     contacts1 = open('VCF_Files/contacts.vcf', 'r')
    #     readfile = contacts1.readlines()
    # count=0
    # for line in readfile:
    #     count +=1
    #     VCF_Final.write(line)
    #     # print(line)
    # print(VCF_Final)
