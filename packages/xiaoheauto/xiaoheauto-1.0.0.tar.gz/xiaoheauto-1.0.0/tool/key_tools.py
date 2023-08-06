import random



def random_str(send_request,chars,lenth):
    return "".join(random.choices(chars,k=int(lenth)))


def random_int(send_request,star,end):
    return random.randint(int(star),int(end))

def phone(send_request):
    return "".join('18949458978')