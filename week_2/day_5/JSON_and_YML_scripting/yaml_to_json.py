import json, os, sys, yaml

if len(sys.argv) > 1:

    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()

    else:
        print("Error: " + sys.argv[1] + " not found")
        exit(1)

else:
    print("Usage: json2yaml.py <source_file.json> [target_file.yaml]")

output = json.dumps(source_content, indent=4)

if len(sys.argv) < 3:
    print(output)

elif os.path.exists((sys.argv[2])):
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)

else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()
