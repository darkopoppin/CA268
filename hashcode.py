class Slide(object):

    def __init__(self, id1, n_tags, tags, id2=None):
        self.id1 = id1
        self.id2 = id2
        self.n_tags = n_tags
        self.tags = tags 

    def __str__(self):
        return 'id='+str(self.id1)+ ' id2='+str(self.id2) + ' n_tags='+ str(self.n_tags) +' tags='+ str(self.tags)

def sort_input(odd_v, even_v, odd_h, even_h, input_pics):
    for i in range(1, len(input_pics)):
        layout = input_pics[i][0]
        n_tags = int(input_pics[i][1])
        tags = set(input_pics[i][2:]) 
        if layout == 'V':
            if n_tags % 2 == 0: #if its even and vertical
                even_v.append(Slide(i, n_tags, tags))
            elif n_tags != 1: #if its odd and vertical
                odd_v.append(Slide(i, n_tags, tags))
        else:
            if n_tags % 2 == 0: #if its even and horizontal
                even_h.append(Slide(i, n_tags, tags))
            elif n_tags != 1: #if its odd and horizontal
                odd_h.append(Slide(i, n_tags, tags))

    return odd_v, even_v, odd_h, even_h

def vertical_pairing(odd_v, even_v):
    v_pairs = [] #list for paired vertical pics
    i = 1
    while len(odd_v) != 0 and len(even_v) != 0:
        i = 1
        ver1 = even_v.pop() #first vertical pic
        while i < len(even_v): #searches for pair of ver1
            even_pic = len(ver1.tags.intersection(even_v[-i].tags)) #ver1 intersected with pic from even_v
            odd_pic = len(ver1.tags.intersection(odd_v[-i].tags)) #ver1 intersected with pic from odd_v
            if even_pic > odd_pic and even_pic > 1: #compares number of intersected tags 
                ver2 = even_v.pop(-i)
                union = ver1.tags.union(ver2.tags)
                #print(even_pic)
                v_pairs.append(Slide(ver1.id1, len(union), union, ver2.id1))
                i = 1
                break
            elif odd_pic >= even_pic and odd_pic > 1: #compares number of intersected tags
                ver2 = odd_v.pop(-i)
                union = ver1.tags.union(ver2.tags)
                #print(odd_pic)
                v_pairs.append(Slide(ver1.id1, len(union), union, ver2.id1))
                i = 1
                break
            i += 1
    return v_pairs

def make_slideshow(even_h, odd_h):
    slideshow = []
    slide = even_h.pop()
    while len(odd_h) != 2 and len(even_h) != 2:
        i = 1
        while i < len(even_h):
            #print(len(even_h), len(odd_h))
            even_match = len(slide.tags.intersection(even_h[-i].tags))
            odd_match = len(slide.tags.intersection(odd_h[-i].tags))
            if even_match > odd_match and even_match > 0:
                slideshow.append(even_h.pop(-i))
                #print('even')
                break
            elif odd_match >= even_match and odd_match > 0:
                slideshow.append(odd_h.pop(-i))
                #print('odd')
                break
            elif abs(odd_match - even_match) <= 1:
                even_h.pop(-i)
                odd_h.pop(-i)
                break
            i += 1
    return slideshow

def main():

    with open ('1','r') as f: #read input
        line = f.readline()
        input_pics = []
        while len(line) != 0:
            input_pics.append(line.strip().split())
            line = f.readline()

    odd_v, even_v, odd_h, even_h = sort_input([],[],[],[],input_pics)
    odd_v.sort(key=lambda x: x.n_tags, reverse=False)
    even_v.sort(key=lambda x: x.n_tags, reverse=False)
    
    #print('odd',len(odd_v))
    #print('even', len(even_v))
    v_pairs = vertical_pairing(odd_v, even_v)
    print('odd',len(odd_h))
    print('even', len(even_h))
    print('v_pairs',len(v_pairs))
    

    for pair in v_pairs: #distributes the vertical pairs among the horizontal pics
        if pair.n_tags % 2 == 0:
            even_h.append(pair)
        else:
            odd_h.append(pair)
    slideshow = make_slideshow(even_h, odd_h)     
    print('odd',len(odd_h))
    print('even', len(even_h))
    print(len(slideshow))

    with open('output','a') as out:
        out.write(str(len(slideshow)) + '\n')
        for slide in slideshow:
            if slide.id2 == None:
                out.write(str(slide.id1) + '\n')
            else:
                out.write(str(slide.id1) + ' ' + str(slide.id2) + '\n')

main()
