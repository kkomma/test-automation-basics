import concurrent.futures

def write_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')

file_path = './file.txt'
contents = ['Hello', 'World', 'GitHub', 'Copilot']

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(write_to_file, [file_path] * len(contents), contents)

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     executor.map(write_to_file, [file_path] * len(contents), contents)