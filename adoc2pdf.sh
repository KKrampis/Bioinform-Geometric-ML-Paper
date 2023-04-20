#makes html
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex GeoDeepLearnBio.adoc
#makes docbook xml (as intermediate for pdf conversion)
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex -b docbook GeoDeepLearnBio.adoc
#pandoc used to convert docbook to pdf
pandoc -f docbook GeoDeepLearnBio.xml -o GeoDeepLearnBio.pdf
