def get_uuid():
    #make a random string
    r_s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
    #return it in a 'uuid' format
    uuid = r_s[:8] + "-" + r_s[8:12] + "-" + r_s[12:16] + "-" + r_s[16:20] + "-" + r_s[20:32]
    return uuid