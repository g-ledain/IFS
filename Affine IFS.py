import numpy as np
import matplotlib.pyplot as plt
import jsonschema as jschem
import json

filename="barnsley fern.txt"


def IFSplot(IFSFileName,iterations,initialpos=[0,0]):
    rng=np.random.default_rng()
    with open(IFSFileName) as IFSSpecFile:
        IFSSpec=json.loads(IFSSpecFile.read())

    with open("affine IFS schema.txt") as schemaFile:
        IFSschema=json.loads(schemaFile.read())

    jschem.validate(instance=IFSSpec,schema=IFSschema)#throws if validation fails

    matrices=[np.array(item["matrix"]) for item in IFSSpec]
    translations=[np.transpose(np.array([item["translation"]])) for item in IFSSpec]
    probabilities=[item["probability"] for item in IFSSpec]

    position=np.array([[initialpos[0]],[initialpos[1]]])

    xpositions=np.zeros(iterations)
    ypositions=np.zeros(iterations)

    for i in range(iterations):
        j=rng.choice(4,p=probabilities)
        
        position = np.dot(matrices[j],position)+translations[j]

        xpositions[i]=position[0]
        ypositions[i]=position[1]

    plt.plot(xpositions,ypositions,'.',markersize=0.25)
    plt.show()
