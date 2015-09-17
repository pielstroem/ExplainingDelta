# Notizen #


## IPython/Jupyter ##

Installation über pip:

	pip install jupyter

Starten:

	jupyter notebook


## DARIAH NLP-Pipeline ##

Der DARIAH-DKPro-Wrapper ist auf Github verfügbar:
<https://github.com/DARIAH-DE/DARIAH-DKPro-Wrapper>. Unter
[releases](https://github.com/DARIAH-DE/DARIAH-DKPro-Wrapper/releases)
findet man veröffentlichte Versionen mit fertig gebautem jar-File.

Auf einem starken Rechner können wir mit GNU parallel auch mehrere
Pipeline-Prozesse gleichzeitig laufen lassen (hier bspw. 6):

	parallel -j6 -n1 java -jar de.tudarmstadt.ukp.dariah.pipeline-0.3.4-standalone.jar -language de -input {} -output /path/to/output ::: /path/to/input/*.txt

