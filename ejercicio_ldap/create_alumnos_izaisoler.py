import os

# Parámetros
base_dn = "dc=examensoler,dc=org"
ou = "alumnos"
group_dn = "cn=alumnos," + base_dn
num_alumnos = 2000  # Número de alumnos a crear

# Archivo de salida
ldif_filename = "alumnossoler.ldif"

# Crear el archivo LDIF
with open(ldif_filename, 'w') as ldif_file:
    # Crear el grupo 'alumnos' si no existe
    ldif_file.write(f"dn: {group_dn}\n")
    ldif_file.write("objectClass: posixGroup\n")
    ldif_file.write("cn: alumnos\n")
    ldif_file.write("gidNumber: 500\n\n")  # Puede cambiarse el gidNumber según se necesite

    # Crear los usuarios y agregar cada uno al grupo 'alumnos'
    for i in range(1999, num_alumnos + 1999):
        # Crear cada usuario
        uid = f"alumno{i}"
        uid_number = i + 1000  # UID único por alumno
        home_dir = f"/home/alumnos/{uid}"
        ldif_file.write(f"dn: uid={uid},ou={ou},{base_dn}\n")
        ldif_file.write("objectClass: inetOrgPerson\n")
        ldif_file.write("objectClass: posixAccount\n")
        ldif_file.write("objectClass: top\n")
        ldif_file.write(f"uid: {uid}\n")
        ldif_file.write(f"cn: Alumno {i}\n")
        ldif_file.write(f"sn: Soler{i}\n")
        ldif_file.write(f"uidNumber: {uid_number}\n")
        ldif_file.write("gidNumber: 500\n")  # Puede cambiarse el gidNumber según se necesite
        ldif_file.write(f"homeDirectory: {home_dir}\n")
        ldif_file.write("loginShell: /bin/bash\n\n")

        # Agregar el usuario al grupo 'alumnos'
        ldif_file.write(f"dn: {group_dn}\n")
        ldif_file.write("changetype: modify\n")
        ldif_file.write("add: memberUid\n")
        ldif_file.write(f"memberUid: {uid}\n\n")

print(f"LDIF file '{ldif_filename}' created successfully with {num_alumnos} students.")
