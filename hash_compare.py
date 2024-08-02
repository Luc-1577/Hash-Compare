import hashlib as hs

md5_ = hs.md5()
sha1_ = hs.sha1()
sha224_ = hs.sha224()
sha256_ = hs.sha256()
sha384_ = hs.sha384()
sha512_ = hs.sha512()
sha3_224_ = hs.sha3_224()
sha3_256_ = hs.sha3_256()
sha3_384_ = hs.sha3_384()
sha3_512_ = hs.sha3_512()

def file_reader(path):
    words = ''
    
    with open(path, 'r') as fil:
        word = fil.read()

        while word:
            words += word
            word = fil.readline()
            
        words = words.split('\n')
        words = list(filter(lambda x: x.strip(), words))
        return words

def hashes_reader(path):
    hashes = ''
    
    with open(path, 'r') as fil:
        hash = fil.read()
        
        while hash:
            hashes += hash
            hash = fil.readline()
        
        hashes = hashes.split('\n')
        hashes = list(filter(lambda x: x.strip(), hashes))
        return hashes

def compare(crypto):
    passwords = file_reader(R2)
    hashes = hashes_reader(R3)
    encrypt = crypto.copy()
    
    for x in passwords:
        encrypt.update(x.encode())
        for i in range(len(hashes)):
            if encrypt.hexdigest() == hashes[i]:  
                print(x + ' --> ' + hashes[i] + '\n')
        encrypt = crypto.copy()


print('1 - md5',
      '2 - sha1',
      '3 - sha224',
      '4 - sha256',
      '5 - sha384',
      '6 - sha512',
      '7 - sha3_224',
      '8 - sha3_256',
      '9 - sha3_384',
      '10 - sha3_512',
      
      sep='\n', end='\n\n')

while True:
    R1 = input('Choose an option > ')
    R1 = R1.strip()
    if not R1.isdigit() or int(R1) > 10:
        print('Error \n')
        break
    print()
    
    R2 = input('Passwords\' file path > ')
    print()

    R3 = input('Hashes\' file path > ')
    print()
    
    match R1:
        case '1':
            compare(md5_)

        case '2':
            compare(sha1_, R2)
        
        case '3':
            compare(sha224_, R2)
        
        case '4':
            compare(sha256_, R2)
        
        case '5':
            compare(sha384_, R2)
        
        case '6':
            compare(sha512_, R2)
        
        case '7':
            compare(sha3_224_, R2)
        
        case '8':
            compare(sha3_256_, R2)

        case '9':
            compare(sha3_384_, R2)
        
        case '10':
            compare(sha3_512_, R2)