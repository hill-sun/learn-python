from sys import argv

script, filename = argv

txt = open(filename)

content =  txt.read()

content_new = content.split()

#content += 2

print content_new