# Face-Recognition
Un script de reconnaissance faciale qui se lance à partir de la webCam.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project 
### UTILISATION DE LA RECONNAISSANCE FACIALE AVEC OPENCV 
Cette réalisation fut faite dans le cadre d’un projet robotique. Le robot devant pouvoir se déplacer à distance, ou de manière autonome, grâce à des requêtes MQTT et un ESP32. Nous avons décidé d’ajouter à ce robot la possibilité de reconnaître des individus dont il a les photos.
Dans ce repo vous trouverez donc le code py à lancer avec la commande : py 'final.py'
Pensez à charger les photos des personnes à reconnaitre avant de lancer le script, et modifier dans le début du script les chemins de cez mêmes photos.
Pensez également à charger le fichier haarcascade_frontalface_default.xml afin que vous disposiez du modèle.


### Built With
* [haarcascade_frontalface_default de OpenCV](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
