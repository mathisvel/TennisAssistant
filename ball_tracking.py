import cv2
import numpy as np

# Charger la vidéo 
cap = cv2.VideoCapture('tennis_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break # Fin de la vidéo

    # Convertir l'image en espace HSV pour isoler des couleurs
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Définir la plage de couleur de la balle de tennis 
    lower_yellow = np.array([30, 40, 40])
    upper_yellow = np.array([60, 255, 255])

    #  Créer masque qui garde que les pixels jaunes
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Trouver les contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Rectangle autour
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50 and area < 1000: # Filtrer par taille pour ignorer le bruit et les gros objets
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Balle", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Résultat
    cv2.imshow('Tennis AI - Detection', frame)
    # cv2.imshow('Masque', mask) # Ce que l'ordi voit

    # Quitter
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
