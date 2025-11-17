import csv

# Input CSV file
csv_file = 'contacts.csv'
# Output VCF file
vcf_file = 'contacts.vcf'

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    # Write to the VCF file
    with open(vcf_file, 'w') as vcf:
        for row in reader:
            name = row[0]
            phone = row[1]

            vcf.write('BEGIN:VCARD\n')
            vcf.write('VERSION:3.0\n')
            vcf.write(f'FN:{name}\n')
            vcf.write(f'TEL;TYPE=CELL:{phone}\n')
            vcf.write('END:VCARD\n')

print(f'VCF file created: {vcf_file}')
