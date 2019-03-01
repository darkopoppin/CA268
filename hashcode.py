class Slide(object):

    def __init__(self, id1, n_tags, tags, id2=None):
        self.id1 = id1
        self.id2 = id2
        self.n_tags = n_tags
        self.tags = tags 

    def __str__(self):
        return 'id='+str(self.id1)+' n_tags='+ str(self.n_tags) +' tags='+ str(self.tags)

def sort_input(odd_v, even_v, odd_h, even_h,input_pics):
    for i in range(1, len(input_pics)):
        layout = input_pics[i][0]
        n_tags = int(input_pics[i][1])
        tags = set(input_pics[i][2:]) 
        if layout == 'V':
            if n_tags % 2 == 0: #if its even and vertical
                even_v.append(Slide(i, n_tags, tags))
            else: #if its odd and vertical
                odd_v.append(Slide(i, n_tags, tags))
        else:
            if n_tags % 2 == 0: #if its even and horizontal
                even_h.append(Slide(i, n_tags, tags))
            else: #if its odd and horizontal
                odd_h.append(Slide(i, n_tags, tags))

    return odd_v, even_v, odd_h, even_h

def vertical_pairing(odd_v, even_v):
    pass

def main():

    with open ('3','r') as f: #read input
        line = f.readline()
        input_pics = []
        while len(line) != 0:
            input_pics.append(line.strip().split())
            line = f.readline()

    odd_v, even_v, odd_h, even_h = sort_input([],[],[],[],input_pics)
    odd_v.sort(key=lambda x: x.n_tags, reverse=False)
    even_v.sort(key=lambda x: x.n_tags, reverse=False)
    
    print(len(odd_v))
    print(len(even_v))
main()
