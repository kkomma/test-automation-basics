import re

class IpAddressValidator:

    def __init__(self):
        pass

    def validateIp(self, ip):
        if ip.count('.') != 3:
            return False
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    
    def validateIpV6(self, ip):
        if ip.count(':') != 7:
            return False
        parts = ip.split(':')
        if len(parts) != 8:
            return False
        for part in parts:
            if len(part) > 4:
                return False
            if not part.isalnum():
                return False
        return True
    
    def ipv6validationregex(self, ip):
        pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
        return bool(pattern.match(ip))
    
    def ipv4validationregex(self, ip):
        pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        return bool(pattern.match(ip))
    
if __name__ == '__main__':
    ipv = IpAddressValidator()
    print(ipv.validateIp('122.122.3.0'))  # True  
    print(ipv.ipv4validationregex('122.122.3.0'))  # True  
    print(ipv.validateIp('0.0.0.0'))  # True
    print(ipv.validateIp('0.0.0.266'))  # False
    print(ipv.validateIpV6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))  # True
    print(ipv.ipv6validationregex('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))  # True