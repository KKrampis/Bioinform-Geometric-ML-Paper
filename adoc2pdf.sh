#makes html
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex GeoDeepLearnBio.adoc
#makes docbook xml (as intermediate for pdf conversion)
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex -b docbook GeoDeepLearnBio.adoc
#pandoc used to convert docbook to pdf
pandoc -V geometry:margin=1.15in -f docbook GeoDeepLearnBio.xml -o GeoDeepLearnBio.pdf
#pandoc used to convert docbook to doc
pandoc -f docbook GeoDeepLearnBio.xml -o GeoDeepLearnBio.docx
