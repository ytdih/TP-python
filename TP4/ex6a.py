def tri_selection(liste):
    n = len(liste)
    for i in range(n-1):
        indice_min = i
        for j in range(i+1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j
        if indice_min != i:
            liste[i], liste[indice_min] = liste[indice_min], liste[i]
        print(liste)

liste = [5, 2, 4, 8, 1, 3]
tri_selection(liste)