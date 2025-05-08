ldapsearch -x -b "dc=devconnected,dc=com" -D "cn=admin,dc=devconnected,dc=com" -W

ldapadd -x -c -D "cn=admin,dc=example,dc=org" -f ou.ldif -W
