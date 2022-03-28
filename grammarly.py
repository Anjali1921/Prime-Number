# import TextBlob
from textblob import TextBlob

a = TextBlob("CampK12 is a good compny and alays walue ttheir employeees.")
b = TextBlob(" Python is not onnly a repptiile, buth a higghh- levelll proggraming languge as well.")

# using TextBlob.correct() method
a = a.correct()
b = b.correct()

print(a)
print(b)