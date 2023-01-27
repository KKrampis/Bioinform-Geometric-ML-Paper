asciidoctor -r asciidoctor-bibtex -b docbook GeoDeepLearnBio.adoc
pandoc -f docbook GeoDeepLearnBio.xml -o GeoDeepLearnBio.pdf
zathura GeoDeepLearnBio.pdf
