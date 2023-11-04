from library.cNode import cNode
import binarytree

def tree(self)->binarytree:
    #primero creo todos los nodos y dsp las srelaciones entre ellos
    unevenBreathing = cNode(4,"unevenbreathing")
    hemorrhage=cNode(2, "hemorrhage")
    red=cNode(1,"red")
    orange=cNode(3,"orange")
    orange1=cNode(5,"orange")
    unconscious=cNode(6,"unconscious")
    orange2=cNode(7,"orange")
    agitatedPuslations=cNode(8,"agitatedPulsations")
    yellow=cNode(9,"yellow")
    blurryVision=cNode(10, "blurryVision")
    yellow1=cNode(11, "yellow")
    paleness=cNode(12,"paleness")
    yellow2=cNode(13, "yellow")
    fever=cNode(14, "fever")
    green=cNode(15, "green")
    pain=cNode(16, "pain")
    blue=cNode(17,"blue")

    #creamos el arbol relacionando los nodos
    unevenBreathing.left=hemorrhage
    unevenBreathing.rigth=unconscious
    hemorrhage.left=red
    hemorrhage.rigth=orange
    unconscious.left=orange1
    unconscious.rigth=agitatedPuslations
    agitatedPuslations.left=orange2
    agitatedPuslations.rigth=blurryVision
    blurryVision.left=yellow
    blurryVision.rigth=paleness
    paleness.left=yellow1
    paleness.rigth=fever
    fever.left=yellow2
    fever.rigth=pain
    pain.left=green
    pain.rigth=blue

    #devuelvo la raiz que tiene referencia al resto del arbol
    return unevenBreathing


        