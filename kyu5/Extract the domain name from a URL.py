import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')
