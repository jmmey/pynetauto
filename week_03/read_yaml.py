import yaml

filename = input('Enter Filename: ')
with open(filename) as f:
    yaml_out = yaml.load(f)

print(yaml_out)
