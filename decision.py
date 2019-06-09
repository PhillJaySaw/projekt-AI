from sklearn import tree
from random import randint
import matplotlib.pyplot as plt

print(["size", "water", "pest", "weed", "fertilizer"])
features = [[1,5,5,5,1],[1,2,3,3,0],[1,1,1,1,1],[1,3,2,3,1],
            [2,3,1,1,1],[2,1,3,2,1],[2,2,2,3,1],[2,3,3,3,0],
            [2,3,2,2,1],[2,2,3,2,1],[2,2,2,3,1],[2,2,2,2,0],
            [2,1,3,3,0],[2,3,3,3,0],[3,2,2,2,0],[2,1,2,2,0],
            [3,1,1,3,1],[2,1,1,2,1]]
labels = ['harvest', 'harvest', 'harvest', 'harvest', 'water',
          'pest', 'weed', 'fertilizer', 'water', 'pest', 'weed',
          'fertilizer', 'fertilizer', 'fertilizer', 'fertilizer',
          'fertilizer', 'weed', 'weed']
# harvest 1 znaczy ze dojrzała, na potrzeby programu od razu po zebraniu zasadzona jest nowa niedojrzała roślina
# weed pest weed od 1 do 3, im wyższa cyfra tym wieksza potrzeba danej akcji
# fertilizer 0 - trzeba nawozić, 1 - nie trzeba
# "priorytet" ma tutaj harvest, resztę wybiera mniej wiecej losowo przy takim samym stopniu potrzeby, trochę większą szansę ma fertilizer
# po wykonaniu czynności traktorem na: size - zmieniamy na 3, water,pest,weed - zmieniamy na 1, fert - zmieniamy na 1
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
# train
plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
plt.suptitle("Drzewo decycyjne AI project")
#print(len(features),len(labels))
#plt.legend(features,labels,loc='lower right', borderpad=0, handletextpad=0)
plt.axis("tight")
tree.plot_tree(clf, filled=True)


def dtree():

    # crop - to będą nasze dane zbierane z pola przez ciągnik
    crop = [randint(1,3), randint(1,3), randint(1,3), randint(1,3), randint(0,1)]
    print(crop)
    prediction = clf.predict([crop])
    print(*prediction)
    #plt.show() <- wizualizacja "drzewa"


dtree()
