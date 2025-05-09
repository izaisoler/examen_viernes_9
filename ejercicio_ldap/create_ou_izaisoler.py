def create_organizational_unit_ldif(filename, ou_name, base_dn):
    """Creates an LDIF file for an organizational unit."""
    ldif_content = f"""# organizational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""

    return ldif_content

def generate_ou_ldif_file(filename, base_dn, ous):
    """Generates an LDIF file for multiple organizational units."""
    try:
        with open(filename, "w") as f:
            for ou in ous:
                ldif_content = create_organizational_unit_ldif(filename, ou, base_dn)
                f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")

# List of OUs to create
ous = [
    "alumnos",
    "3esoA", "3esoB", "3esoC", "3esoD", "3esoE", "3esoF", "3esoG",
    "1bachA", "1bachB", "1bachC", "1bachD", "1bachE",
    "GSasir1", "GSasir2",
    "GSdaw1", "GSdaw2"
]

# Define the base DN for your LDAP server (replace with your actual base DN)
base_dn = "dc=izaisoler,dc=org"

# Name of the output LDIF file
filename = "ouizaisoler.ldif"

# Generate the LDIF file for all the OUs
generate_ou_ldif_file(filename, base_dn, ous)
