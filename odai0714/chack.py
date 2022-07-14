from PIL import Image 
import imagehash 
 
hash = imagehash.average_hash(Image.open('images/cry.png')) 
#print(hash) 
 
#otherhash = imagehash.average_hash(Image.open('images/cry.png')) 
otherhash = imagehash.average_hash(Image.open('images/iroha.png')) 
#print(otherhash) 
 
print(hash == otherhash) 
print(hash - otherhash)