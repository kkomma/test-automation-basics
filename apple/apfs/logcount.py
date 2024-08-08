# def process_log(filename):
#     records = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.split()
#             hostname = parts[0]
#             request = parts[5]
#             response_code = parts[8]
#             if request.startswith('"GET') and response_code == '200':
#                 if hostname in records:
#                     records[hostname] += 1
#                 else:
#                     records[hostname] = 1

#     output_filename = 'records_' + filename
#     with open(output_filename, 'w') as file:
#         for hostname, count in records.items():
#             file.write(hostname + ';;;;' + str(count) + '\n')

# # Example usage:
# process_log('host_access_log_00.txt')


from collections import defaultdict
import re

def process(s: str) -> str:
    count = defaultdict(int)
    for line in s.split('\n'):
        host, method, response = re.match(r'([^\s]+).+"(GET|POST).+" (\d+)', line).groups()
        if response == '200' and method == 'GET':
            count[host] += 1
    return '\n'.join(f'{k} {v}' for k, v in count.items())

with open('host_access_log_00.txt') as f:
    result = process(f.read())
with open('records_host_access_log_00', 'w') as f:
    f.write(result)