input_string = input("paste koro: ")
output_string = '_'.join(input_string.split()) 
output = output_string.replace(".", "") + ".py"

print(output)

